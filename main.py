from face_detector import YOLOv8FaceDetector

def main():
    image_path = "path/to/your/image.jpg"  # Replace with your image path
    output_path = "path/to/your/output/result.jpg"  # Replace with your desired output path

    face_detector = YOLOv8FaceDetector()
    face_detector.detect_faces(image_path, output_path)

if __name__ == "__main__":
    main()
