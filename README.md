# Laproscopy

A laparoscope, a tiny tube containing a camera and light, is inserted into the patient's body using a minimally invasive surgical method called laparoscopy. One of the key tools used in laparoscopic surgery is the grasper. During the procedure, they are used to grab, hold, and manipulate tissues, organs, or other things. 

Typically long and slender with a scissor-like form, the graspers used in laparoscopic surgery enable the surgeon to precisely grasp and cut tissue. They are employed in a variety of treatments, from straightforward surgery like biopsies to more difficult ones like organ removal.

Compared to open surgery, laparoscopic surgery using graspers offers a number of benefits. Because it is less intrusive, the patient recovers more quickly and experiences less pain and scars. Additionally, the use of graspers enables more accurate and controlled surgery, and the smaller incisions used in laparoscopic surgery lower the risk of infection and haemorrhage.

Overall, grasper-assisted laparoscopy surgery is a safe and successful surgical method that offers patients a number of advantages and is frequently utilised in a range of surgical operations.

Here, we will have images of the graspers at different angles and will be deducing the angles. 

## Angle Finder

This script calculates the angle between two points in an image. It uses the OpenCV library for image processing and Matplotlib for visualization.

Getting Started
To run this script, you will need Python 3 and the following libraries:

OpenCV
Matplotlib
You can install these libraries using pip:

``` bash
pip install opencv-python matplotlib
```

Clone this repository:

```
git clone https://github.com/aramcode/Laparoscopy.git
```

Change into the project directory:

```
cd anglefinder
```

## Usage

The script takes a single optional command-line argument --file, which specifies the file path of the image to be processed. If the argument is not provided, the default value is grasp_1.jpg.

Run the script:

```
python angle_finder.py --file <path_to_image_file>
```

The script displays the image in a window and listens for mouse events. The user can draw dots on the image by clicking the left mouse button, and the script will display the angle between the last three dots if they have been drawn. The script continues to listen for mouse events until the window is closed.

