# Cryostat Tracking
Project for 2024 spring CP2

# Closed Cycle Helium Refrigerator [1]

The cooling cycle of a Closed Cycle Refrigerator (CCR) is analogous to that of a household refrigerator, with a few key additions. In a household refrigerator, a working fluid is compressed, the heat of compression is removed by an air/water-cooled heat exchanger, and the fluid is then expanded to achieve cooling below ambient temperature. However, such a system can only produce cooling that is a few degrees below zero degrees centigrade. But we are interested in cooling and maintaining our load at about 10K. Therefore, we need very efficient heat exchange and helium as a working fluid, because helium remains fluid at temperatures approaching absolute zero.

## The Principles of Operation
The compressor used is air/water cooled and oil lubricated, with an oil separation system. The compressor is separated from the refrigeration unit which helps in reducing vibrations.

![1 Cycle](https://github.com/ubsuny/g2coral-CP2P2024/blob/main/stage1.1.PNG)

Figure 1 shows the schematic diagram of the refrigeration unit. A source of compressed gas is connected to intake valve A. Valve B is the exhaust valve leading to the low-pressure side of the compressor. If valve B is closed, and valve A is opened, then the piston will move up and the cylinder will fill up with compressed gas. Now we close valve A and open valve B, causing the compressed gas in the cylinder to expand into the discharge line and cool down, which will lead to heat transfer from the load to the gas. Thereby the load will cool down, and the gas will be heated. The piston is then lowered, which discharges the remaining gas to the discharge line, completing the cycle.

A regenerator is a type of heat exchanger that allows helium to flow back and forth through it. It is filled with a material that has a large surface area, high specific heat capacity, and low thermal conductivity. This material efficiently absorbs heat from the helium that is coming in from valve A, stores the heat, and then transfers that heat to the helium exiting through the discharge line. Without the regenerator, one would not be able to achieve the desired low temperatures.

The system shown in Figure 1 can only reach temperatures in the 33-70K range. To reach the required temperature of 6-10K, we can add a second stage.

# Imaging an Object in a Cryostat.

The current experiment we are running requires that we cool down the sample to about 10K. That is because the sample would burn if we ran a current through it at a high temperature. Furthermore, the low temperature allows for a reliable spin injection to the active region. Finally, we need to test the effect of temperature on the electroluminescence circularly polarized light that is emitted by the sample. 

A CCR will inherently produce vibration. There are a few things that can be done to reduce vibrations. However, vibrations will always be there. Therefore, imaging the inside of the cryostat can be challenging. This project is aimed at finding a solution to imaging an object inside the cryostat.

The proposed solution is to place an LED on one side of the sample holder, and the sample on the opposite side. A high-speed camera can then be used to capture an image of the LED as it is moving inside the cryostat. The images can then be processed to obtain the position of the LED, and the time at which the LED was at that position. On the other side, the sample is excited by a function generator, and the photoluminescence (PL) spectra are recorded by a spectrometer. One can then reconstruct a PL image of the sample by matching the recorded PL spectra with the position of the LED. A disadvantage of this imaging method is that some pixels will not be imaged, so one will not have the full image of the sample.

The tracking code is available in `midterm/motion_track.py`, and an example data set is available in `midterm/data_vib.csv`. Both were provided by reference [2].

# Tracking

## Bright Tracking

The first attempt at tracking the LED in the cryostat was done by [1]. It involved finding the brightest spot in the image and recording those coordinates. This method was very quick (~0.2 ms per frame). However, upon closer examination, it was found that racking the bright spot is very inaccurate. Therefore, we had to move on to different methods.

## Machine Learning

A CNN tracking code was attempted. It produced accurate results. However, it was quickly abandoned because of speed issues.

## OpenCV Template Matching [3]

OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. It is designed to provide a common infrastructure for computer vision applications. OpenCV contains over 2500 optimized algorithms that can be used for a variety of tasks, including detecting and recognizing faces, identifying objects, classifying human actions in videos, tracking camera movements, tracking moving objects, extracting 3D models of objects, and stitching images together to produce a high-resolution image of an entire scene. Furthermore, it supports various programming languages like C++, Python, Java, and MATLAB.

Template matching is a technique in computer vision used to find a specific part of an image that matches a template image. This method is commonly used for object detection. It works by selecting a smaller image, known as the template, which is the pattern you want to find in the larger image (referred to as the source or search image). The template is slid over the source image (from left to right and top to bottom), and at each position, a similarity measure is calculated between the template and the region of the source image under the template. Several methods can be used to measure how similar the template is to the region in the source image. Common methods include: TM_SQDIFF, TM_SQDIFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_CCOEFF, and TM_CCOEFF_NORMED.

OpenCV Template matching is simple and effective. However, it tends to perform poorly with noisy images, and it can take a long time to process large images.

All the above algorithms have been tested. All six of them provided good detection results. However, only TM_CCORR and TM_SQDIFF were the fastest. When the fast algorithms were tested on large images (480 x 640), it took ~8ms per frame. However, when the same algorithms were tested on 256 x 256 images, it only took ~0.5 ms per frame. It is also worth noting that running those algorithms from a .ipynb file takes almost three times longer than running them from a .py file.

### Improving OpenCV Template Matching

Thus far the fastest tracking achieved was ~0.5 ms per frame. However, the camera we use can take up to 5000 fps. Therefore, we strive to reach a tracking speed of ~0.2 ms per frame, which will allow us to calculate as much data as possible. Therefore, future tests will be conducted on 64 x 64 images. Moreover, we will experiment with running the template matching algorithms on a GPU instead of a CPU.

# References
[1] “Janis Closed Cycle Refrigerator System Manual,” Applied Cryogenics, [Online]. Available:[ http://appliedcryogenics.com/CRYO%20DOC/Janis%20Closed%20Cycle%20Refrigerator%20System%20Manual.pdf](http://appliedcryogenics.com/CRYO%20DOC/Janis%20Closed%20Cycle%20Refrigerator%20System%20Manual.pdf). [Accessed: March 29, 2024].

[2] C. Mudiyans, GitLab, 2024.

[3] “OpenCV: Object Detection,” docs.opencv.org. https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html#ga586ebfb0a7fb604b35a23d85391329be (accessed May 11, 2024) ‌
