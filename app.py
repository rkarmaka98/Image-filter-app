from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__)

camera = cv2.VideoCapture(0)

def generate_frames(filter_type=None, param1=0, param2=0):
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Adding other filters
            if filter_type == 'gray':
                intensity = float(param1) / 100.0
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.addWeighted(frame, 1 - intensity, cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR), intensity, 0)
            elif filter_type == 'canny':
                frame = cv2.Canny(frame, int(param1), int(param2))
            elif filter_type == 'gaussian':
                ksize = int(param1) if int(param1) % 2 == 1 else int(param1) + 1
                frame = cv2.GaussianBlur(frame, (ksize, ksize), 0)
            elif filter_type == 'laplacian':
                scale = float(param1) / 10.0
                frame = cv2.Laplacian(frame, cv2.CV_64F, scale=scale)
                frame = cv2.convertScaleAbs(frame)
            elif filter_type == 'sobel':
                ksize = int(param1) if int(param1) % 2 == 1 else int(param1) + 1
                ksize = min(ksize, 31)
                frame = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=int(param1))
                frame = cv2.convertScaleAbs(frame)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    filter_type = request.args.get('filter', 'none')
    param1 = request.args.get('param1', 0)
    param2 = request.args.get('param2', 0)
    return Response(generate_frames(filter_type, param1, param2), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/original_feed')
def original_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
