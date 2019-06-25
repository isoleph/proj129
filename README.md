
# <img src="/img/snek.jpg" width="25"> proj129 
*Capstone project for UCSB Physics 129L*

<div align="center">

<img src="/img/GUI.png" width = 450> 
  
  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/isoleph/proj129.svg)](https://github.com/isoleph/proj129/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/isoleph/proj129.svg)](https://github.com/isoleph/proj129/pulls)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
  [![Tweet](https://img.shields.io/twitter/url/https/shields.io.svg?style=social)](https://twitter.com/risvoi)

</div>

The goal of this program is to simulate 3 masses in 2 dimensions and graph the gravitational contours among them. This was initially done with the [tkinter](https://github.com/python/cpython/tree/master/Lib/tkinter) library but we preferred to use the matplotlib functionality to do it. The script creates a UI where the mass of each particle can be adjusted using a slider and where its position may also be dragged through the GUI.

This project takes inspiration from this [Maple script](https://climate.ucdavis.edu/GravityProblem.pdf) from UC Davis. 

We also invite people to use the particles.py file for click and drag in matplotlib. I couldn't personally find a nice, readable version to make draggable buttons, so feel free to use this code!

# Completed Tasks

- [X] Tokens for each particle
- [X] Position Tracking for each Mass
- [x] Mass sliders for input in GUI
- [x] Writing in Newtonian equations
- [x] Matplotlib render of contour plots
- [x] Integration of Particle Tracking and Graphing
- [ ] Positioning Bug when pressing Reset button
