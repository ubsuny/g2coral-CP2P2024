# Closed Cycle Helium Refrigerator [1]

The cooling cycle of a Closed Cycle Refrigerator (CCR) is analogous to that of a household refrigerator, with a few key additions. In a household refrigerator, a working fluid is compressed, the heat of compression is removed by an air/water-cooled heat exchanger, and the fluid is then expanded to achieve cooling below ambient temperature. However, such a system can only produce cooling that is a few degrees below zero degrees centigrade. But we are interested in cooling and maintaining our load at about 10K. Therefore, we need very efficient heat exchange and helium as a working fluid, because helium remains fluid at temperatures approaching absolute zero.

## The Principles of Operation
The compressor used is air/water cooled and oil lubricated, with an oil separation system. The compressor is separated from the refrigeration unit which helps in reducing vibrations.

![1 Cycle](https://github.com/ubsuny/g2coral-CP2P2024/blob/main/midterm/stage1.PNG)

Figure 1 shows the schematic diagram of the refrigeration unit. A source of compressed gas is connected to intake valve A. Valve B is the exhaust valve leading to the low-pressure side of the compressor. If valve B is closed, and valve A is opened, then the piston will move up and the cylinder will fill up with compressed gas. Now we close valve A and open valve B, causing the compressed gas in the cylinder to expand into the discharge line and cool down, which will lead to heat transfer from the load to the gas. Thereby the load will cool down, and the gas will be heated. The piston is then lowered, which discharges the remaining gas to the discharge line, completing the cycle.

A regenerator is a type of heat exchanger that allows helium to flow back and forth through it. It is filled with a material that has a large surface area, high specific heat capacity, and low thermal conductivity. This material efficiently absorbs heat from the helium that is coming in from valve A, stores the heat, and then transfers that heat to the helium exiting through the discharge line. Without the regenerator, one would not be able to achieve the desired low temperatures.

The system shown in Figure 1 can only reach temperatures in the 33-70K range. To reach the required temperature of 6-10K, we can add a second stage, as shown in Figure 2.

![2 Cycles](https://github.com/ubsuny/g2coral-CP2P2024/blob/main/midterm/stage2.PNG)

# Imaging an Object in a Cryostat.

A CCR will inherently produce vibration. There are a few things that can be done to reduce vibrations. However, vibrations will always be there. Therefore, imaging the inside of the cryostat can be challenging. This project is aimed at finding a solution to imaging an object inside the cryostat.

The proposed solution is to place an LED on one side of the sample holder, and the sample on the opposite side. A high-speed camera can then be used to capture an image of the LED as it is moving inside the cryostat. The images can then be processed to obtain the position of the LED, and the time at which the LED was at that position. On the other side, the sample is excited by a function generator, and the photoluminescence (PL) spectra are recorded by a spectrometer. One can then reconstruct a PL image of the sample by matching the recorded PL spectra with the position of the LED. A disadvantage of this imaging method is that some pixels will not be imaged, so one will not have the full image of the sample.

The tracking code is available in `midterm/motion_track.py`, and an example data set is available in `midterm/data_vib.csv`. Both were provided by reference [2].

# References
[1] “Janis Closed Cycle Refrigerator System Manual,” Applied Cryogenics, [Online]. Available:[ http://appliedcryogenics.com/CRYO%20DOC/Janis%20Closed%20Cycle%20Refrigerator%20System%20Manual.pdf](http://appliedcryogenics.com/CRYO%20DOC/Janis%20Closed%20Cycle%20Refrigerator%20System%20Manual.pdf). [Accessed: March 29, 2024].

[2] C. Mudiyans, GitLab, 2024.
