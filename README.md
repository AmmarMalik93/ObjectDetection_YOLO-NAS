# Atlantics vs Humpback salmon fish detection using YOLO-NAS

## Dataset
There were two directories named **humpback** and **atlantic** containing images.
1) **Humpback** -- 961 images
2) **Atlantic** -- 962 images

The annotations were provided in **COCO** format in ```annotations.json``` file.

## Directory structure
Since I decided to use **YOLO** algorithm to address this problem, it is necessary to format the directory into appropriate **Yolo** format.
The directory structure is as follows:
```
├── homedir
│  ├── data
│  │  ├── train
│  │  ├── val
│  ├── labels
│  │  ├── train
│  │  ├── val
```
```data``` directory will contain _training_ and _validation_ images (80-20 split).

```label``` directory will contain _training_ and _validation_ labels (80-20 split).

## YOLO algorithm
YOLO (You Only Look Once) is an object detection algorithm that performs object detection and localization in a single pass through an input image. A brief explanation of YOLO is as follows:

1) **Dividing the image:** YOLO divides the input image into a grid of cells. Each cell is responsible for predicting bounding boxes and class probabilities for objects present in that cell.

2) **Predictions at each grid cell:** For each grid cell, YOLO predicts multiple bounding boxes along with the probability that an object exists in each bounding box and the class of the object. These predictions are made using a convolutional neural network (CNN).

3) **Single pass prediction:** Unlike traditional object detection algorithms that require multiple passes through the image, YOLO performs all predictions in a single pass. This makes YOLO faster and more efficient.

4) **Non-max suppression:** After making predictions, YOLO uses a technique called non-max suppression to filter out overlapping bounding boxes and select the most confident ones.

5) **Final detection:** The final output of YOLO is a set of bounding boxes, each with a corresponding class label and confidence score. These bounding boxes represent the detected objects in the input image.

YOLO was proposed by [Redmon et al. 2016](https://arxiv.org/abs/1506.02640). Since then various modifications to the original YOLO algorithm have been proposed. I have used YOLO-NAS  (You Only Look One - Neural Architecture Search) [algorithm]( https://deci.ai/blog/yolo-nas-object-detection-foundation-model/) published in May 2023.

YOLO-NAS is an extension of the YOLO algorithm that incorporates Neural Architecture Search (NAS) techniques to automatically search for the optimal architecture of the YOLO model. YOLO-NAS is designed to detect small objects, improve localization accuracy, and enhance the performance-per-compute ratio, making it suitable for real-time edge-device applications. YOLO-NAS has three architectures called YOLO-NASS (small), YOLO-NASM (medium), and YOLO-NASL (large), with varying number of parameters. I have used the _small_ version due to less time and computational resources.

## Training Procedure
The script for training is provided [here](https://github.com/AmmarMalik93/ObjectDetection_YOLO-NAS/blob/main/training.ipynb) ```training.ipynb```.

I trained the algorithm for **50 Epochs** only due to time limitations. It took almost 1 whole day to train due to limited computational resources. 

The **best model** achieved **mAP@[0.50:0.95]** of 0.704.

**mAP@[0.50:0.95]** refers to mean Average Precision (mAP), across a range of confidence thresholds from 0.50 to 0.95.

0.704 is a decent result in my opinion considering that we trained a small network and that too for only 50 epochs.

## Predictions
The prediction script is provided [here](https://github.com/AmmarMalik93/ObjectDetection_YOLO-NAS/blob/main/prediction.ipynb) ```prediction.ipynb```.

The prediction results on validation data are provided in ```val_pred_with_labels``` directory. The **red box** is the _ground truth_ bounding box.
