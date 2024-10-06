from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__)

camera = cv2.VideoCapture(0)

def generate_frames(filter_type=None):
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Adding other filters
            if filter_type == 'gray':
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            elif filter_type == 'canny':
                frame = cv2.Canny(frame, 100, 200)
            elif filter_type == 'gaussian':
                frame = cv2.GaussianBlur(frame, (15, 15), 0)
            elif filter_type == 'laplacian':
                frame = cv2.Laplacian(frame, cv2.CV_64F)
                frame = cv2.convertScaleAbs(frame)
            elif filter_type == 'sobel':
                frame = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
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
    return Response(generate_frames(filter_type), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/original_feed')
def original_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
