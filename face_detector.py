from ultralytics import YOLO
import cv2

class YOLOv8FaceDetector:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def detect_faces(self, image_path, output_path):
        # Predict on an image
        results = self.model(image_path)

        # Get bounding boxes
        boxes = results.xyxy[0].cpu().numpy()

        # Load the image using OpenCV
        image = cv2.imread(image_path)

        # Draw bounding boxes on the image
        self.draw_boxes(image, boxes)

        # Save or display the result
        cv2.imwrite(output_path, image)
        cv2.imshow('Detected Faces', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def draw_boxes(self, image, boxes):
        for box in boxes:
            x1, y1, x2, y2 = map(int, box[:4])
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
