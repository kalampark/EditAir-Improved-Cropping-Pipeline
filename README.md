# EditAir-Improved-Cropping-Pipeline
Smart Crop Pipeline Development using Yolov8

## **Objectives**

1. **Speed**: The current process takes approximately 30% of the video's duration to process. We're looking for an implementation that maintains or improves this runtime.
2. **Accuracy**: The cropped video should accurately focus on the active speaker, ideally switching between speakers when the active speaker changes.

### **YOLOv8 (Facial Detection)**

Use YOLOv8 for facial detection to identify the location of faces in each frame. This will be crucial for cropping the video appropriately. (state of the art for facial detection)

###
