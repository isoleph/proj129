#!/usr/bin/env python3
# physics129L capstone project

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection
from particles import Drag, PointData # custom class
import numpy as np

# define a GUI class with sliders and buttons
class GUI(object):

    # initiation upon GUI being called
    def __init__(self, fig, ax):
        u"Program initiates by creating figure and axes, then initiating \
        the sliders and plot methods"
        print('Initiating Interactive Module!');
        print('\n\tClick and drag one of the masses to relocate it to a new point.');
        print("\tAdjust the mass sliders as desired, and when you're finished click 'Calculate'\n");
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

        # get data from particles
        GUI.DataArray = PointData.getArray(self);
        x_a, y_a = GUI.DataArray['red'];
        x_b, y_b = GUI.DataArray['green'];
        x_c, y_c = GUI.DataArray['blue'];

        print("\tMass A = {} at coordinates {}, {}".format(massR, round(x_a,2),round(y_a,2)));
        print("\tMass B = {} at coordinates {}, {}".format(massG, round(x_b, 2), round(y_b, 2)));
        print("\tMass C = {} at coordinates {}, {}".format(massB, round(x_c,2),round(y_c,2)));
        # newton eqns for contours
        x = np.arange(1, 100); y = x.copy();
        X, Y = np.meshgrid(x, y); Z = np.sqrt(X**2+Y**2);

        xa_disp = (x_a-X)**2; ya_disp = (y_a-Y)**2;
        ra_disp = np.sqrt(xa_disp + ya_disp);

        xb_disp = (x_b-X)**2; yb_disp = (y_b-Y)**2;
        rb_disp = np.sqrt(xb_disp + yb_disp);

        xc_disp = (x_c-X)**2; yc_disp = (y_c-Y)**2;
        rc_disp = np.sqrt(xc_disp + yc_disp);

        # to not display DivideByZero warning
        with np.errstate(all='ignore'):
            Potential = massR/ra_disp + massG/rb_disp + massB/rc_disp;
        l = ax.contour(X, Y, Potential, 150, zorder=1, cmap=plt.cm.get_cmap('Spectral')); # zorder command not functioning
        ax.patch.set_facecolor('black');
        # make text boxes
        ax.text(x_a, y_a+10, 'Mass A', bbox=dict(facecolor='white', alpha=0.5));
        ax.text(x_b, y_b+10, 'Mass B', bbox=dict(facecolor='white', alpha=0.5));
        ax.text(x_c, y_c+10, 'Mass C', bbox=dict(facecolor='white', alpha=0.5));
        
        idn += 1;
        return 0;

    # mass sliders for GUI
    def sliders(self):
        u"Method that creates the mass sliders on the bottom of the GUI"
        # define slider positions
        axcolor = 'lightgoldenrodyellow';
        axMassR = plt.axes([0.2, 0.17, 0.65, 0.03], facecolor=axcolor);
        axMassG = plt.axes([0.2, 0.12, 0.65, 0.03], facecolor=axcolor);
        axMassB = plt.axes([0.2, 0.07, 0.65, 0.03], facecolor=axcolor);

        # globalize values from sliders
        global s_massR; global s_massG; global s_massB;
        s_massR = Slider(axMassR, 'Mass A', 0., 1000.0, valinit=500, valstep=10, \
                         color='red');
        s_massG = Slider(axMassG, 'Mass B', 0., 1000.0, valinit=500, valstep=10, \
                         color='green');
        s_massB = Slider(axMassB, 'Mass C', 0., 1000.0, valinit=500, valstep=10, \
                         color='blue');

        # make buttons
        resetax = plt.axes([0.8, 0.9, 0.1, 0.04]);
        self.resetButton = Button(resetax, 'Reset', color=axcolor, \
                         hovercolor='0.975');
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
        GUI.DataArray['red'] = (20,20);
        GUI.DataArray['green'] = (40,40);
        GUI.DataArray['blue'] = (60,60);
        # PointData.resetAll(fig,ax,Circle)
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
            return 500, 500, 500; # if sliders not yet activated, give this tuple

# run module directly and apply plot preferences
if __name__ == '__main__':
    fig, ax = plt.subplots(figsize=(6,6));
    fig.canvas.set_window_title("Interactive Gravitational Contours");
    plt.subplots_adjust(left=0.15, bottom=0.25);
    plt.axis([0, 100, 0, 100]);

    circle1 = Circle((20, 20), 5, color='red', zorder=50); # zorder commands not functioning
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
