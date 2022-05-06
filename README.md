# coloject
coloject is a Flask web application that enables a user to generate a color pallet chart and object analysis from any image. 

![coloject Home Page](/static/readme-1.png "coloject Home Page")

## About
coloject represents our final project for CS 461 at the University of Southern Indiana. Abstractly, we were tasked with designing an AI agent with real-world applications. As such, we decided to work with images and colors, which spawned coloject. When considering the project's tech stack, we decided to write it in Python due to its ease-of-use and numerous AI supporting libraries.

## Sample Usage
Below is an example output for the color generator. 

![coloject Sample Color](/static/readme-2.png "coloject Sample Color")

Below is a sample API request to recieve hexcodes in JSON.

![coloject Sample API](/static/readme-3.png "coloject Sample API")

## Dependencies
coloject relies on Python 3.7 to function. Particularly, Python 3.7 for the image processing. 

The Python libraries coloject relies on are as follows:
* flask
* pandas
* numpy
* matplotlib
* scikit-image
* opencv-python
* tensorflow 2.4.0
* keras 2.4.3
* pillow
* h5py
* imageai

## Contributors
Zak Pruitt - Color Recognition, Back-End, and Deliverables.
Vincenet Parsons - Color Recognition, Front-End, and Deliverables.
Yosep Almazade - Image Recognition, Object Recognition, and Deliverables.
