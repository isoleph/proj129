#!/usr/bin/env python3
# physics129L capstone project

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection
from particles import Drag, PointData
import numpy as np

# define a GUI class with sliders and buttons
class GUI(object):

    # initiation upon GUI being called
    def __init__(self, fig, ax):
        u"Program initiates by creating figure and axes, then initiating \
        the sliders and plot methods"
        print('\nInitiating Interactive Module!')
        global idn; idn = 0; # keep track of launch number in terminal
        # define matplotlib figure and axis
        self.fig = fig; self.ax = ax;
        # call on methods to make this work!
        self.sliders();
        self.plot();
        return None;

    # function to plot contours
    def plot(self):
        u"Method to update masses from sliders and show \
        results on GUI."
        global idn;
        print("[{}] Calculating...".format(idn));

        ax.clear();  # prevents contours from stacking
        # checks update to get masses from sliders
        massR, massG, massB = GUI.update(self);

        # get data from tokens
        GUI.DataArray = PointData.getArray(self);
        x_a, y_a = GUI.DataArray['red'];
        x_b, y_b = GUI.DataArray['green'];
        x_c, y_c = GUI.DataArray['blue'];

        print("\tmassR = {} at coordinates {}, {}".format(massR, x_a,y_a));
        print("\tmassG = {} at coordinates {}, {}".format(massG, x_b, y_b));
        print("\tmassB = {} at coordinates {}, {}".format(massB, x_c, y_c));
        # create contour specs for each mass
        x = np.arange(1, 10**2); y = x.copy();
        X, Y = np.meshgrid(x, y); Z = np.sqrt(X**2+Y**2);

        xa_disp = (x_a-X)**2; ya_disp = (y_a-Y)**2;
        ra_disp = np.sqrt(xa_disp + ya_disp);

        xb_disp = (x_b-X)**2; yb_disp = (y_b-Y)**2;
        rb_disp = np.sqrt(xb_disp + yb_disp);

        xc_disp = (x_c-X)**2; yc_disp = (y_c-Y)**2;
        rc_disp = np.sqrt(xc_disp + yc_disp);

        with np.errstate(all='ignore'):
            Potential = massR/ra_disp + massG/rb_disp + massB/rc_disp;
        l = ax.contour(X, Y, Potential, 100, zorder=1);

        idn += 1;
        plt.show();
        return 0;

    # mass sliders for GUI
    def sliders(self):
        u"Method that creates the mass sliders on the bottom of the GUI"
        axcolor = 'lightgoldenrodyellow'
        axMassR = plt.axes([0.2, 0.17, 0.65, 0.03], facecolor=axcolor);
        axMassG = plt.axes([0.2, 0.12, 0.65, 0.03], facecolor=axcolor);
        axMassB = plt.axes([0.2, 0.07, 0.65, 0.03], facecolor=axcolor);

        global s_massR; global s_massG; global s_massB;
        s_massR = Slider(axMassR, 'Mass R', 0., 500.0, valinit=50, valstep=10, \
                         color='red');
        s_massG = Slider(axMassG, 'Mass G', 0., 500.0, valinit=50, valstep=10, \
                         color='green');
        s_massB = Slider(axMassB, 'Mass B', 0., 500.0, valinit=50, valstep=10, \
                         color='blue');


        resetax = plt.axes([0.8, 0.9, 0.1, 0.04]);
        self.resetButton = Button(resetax, 'Reset', color=axcolor, \
                         hovercolor='0.975')
        self.resetButton.on_clicked(GUI.reset);

        calcax = plt.axes([0.65, 0.9, 0.15, 0.04]);
        self.calcButton = Button(calcax, 'Calculate', color=axcolor, \
                        hovercolor='0.975');
        self.calcButton.on_clicked(GUI.plot);
        return 0;

    # reset function to be called
    def reset(self):
        u"Method that defines the Reset Button on the GUI"
        print("Resetting!");
        global s_massR; global s_massG; global s_massB;
        s_massR.reset(); s_massG.reset(); s_massB.reset();
        GUI.DataArray['red'] = (20,20)
        GUI.DataArray['green'] = (60,60)
        GUI.DataArray['blue'] = (80,80)
        GUI.plot(self);

        return 0;

    # update mass from sliders
    def update(self):
        u"Method that updates all mass values from mass sliders"
        global s_massR; global s_massG; global s_massB;
        try:
            mR = s_massR.val; # update all values from slider if possible
            mG = s_massG.val;
            mB = s_massB.val;
            return mR, mG, mB;
        except Exception:
            return 50, 50, 50; # if sliders not yet activated, give this tuple



if __name__ == '__main__':
    fig, ax = plt.subplots(figsize=(6,6));
    fig.canvas.set_window_title("Interactive Gravitational Contours");
    plt.subplots_adjust(left=0.15, bottom=0.25);
    plt.axis([0, 100, 0, 100]);

    circle1 = Circle((20, 20), 5, color='red', zorder=50);
    circle2 = Circle((40, 40), 5, color='green', zorder=50);
    circle3 = Circle((60, 60), 5, color='blue', zorder=50);
    circles = [circle1, circle2, circle3];

    active = [];
    for circle in circles:
         ic = Drag(fig, ax, circle);
         ic.connect();
         active.append(ic);
    
    g = GUI(fig, ax);
    plt.show();
