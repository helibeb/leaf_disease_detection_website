from flask import Flask, request, render_template, jsonify
import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image
from ultralytics import YOLO

app = Flask(__name__)

# Load YOLO model (make sure best.pt is in your project folder)
model = YOLO('best.pt')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    try:
        data = request.get_json()
        # Remove the "data:image/png;base64," header and decode the image
        image_data = data['image'].split(',')[1]
        image_bytes = base64.b64decode(image_data)
        
        # Convert bytes to a PIL image
        try:
            pil_image = Image.open(BytesIO(image_bytes)).convert("RGB")
        except Exception as e:
            print("Error opening image:", e)
            return jsonify({"error": "Invalid image data"})
        
        # Convert the PIL image to an OpenCV BGR image
        frame = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
        
        # Run YOLO detection on the frame
        results = model(frame)
        
        # Get the annotated frame with bounding boxes and labels
        annotated_frame = results[0].plot()
        
        # Optionally: if your bounding boxes still don’t appear, try converting the image.
        # Some versions of YOLO may return an image in BGR, so converting to RGB might help.
        # Uncomment the following line if needed:
        annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        
        # Encode the annotated image using PIL
        pil_annotated = Image.fromarray(annotated_frame)
        buffered = BytesIO()
        pil_annotated.save(buffered, format="PNG")
        encoded_image = base64.b64encode(buffered.getvalue()).decode()
        
        return jsonify({
            "result": "Detection complete",
            "annotated_image": f"data:image/png;base64,{encoded_image}"
        })
        
    except Exception as e:
        print("Error in /detect:", e)
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
