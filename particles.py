#!/usr/bin/env python3
# physics129L capstone project;

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# create a class to define draggable buttons
class Drag(object):

    def __init__(self, fig, ax, circle):
        u"""Upon initiation the Drag class will input the relevant mpl \
        figure, axis, and circle elements and then it will \
        display them to the window."""

        # import mpl figures and axes
        self.fig = fig; self.ax = ax;
        self.ax.set_title('Preliminary Circle Module');

        # create data to track particle
        self.press = None;
        self.active = {};
        self.data = {};
        self.circ = circle;
        self.ax.add_artist(circle);
        self.connect();
        return None;
    

    def connect(self):
        u"The :connect: method uses the mpl_connect function to define functions to occur when the \
            mouse is clicked."
        self.cidpress = self.fig.canvas.mpl_connect('button_press_event', self.on_click);
        self.cidrelease = self.fig.canvas.mpl_connect('button_release_event', self.on_release);
        self.cidmotion = self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion);
        return 0;

    def on_click(self, event):
        u"""Upon clicking the, :on_click:, this  method will check if the mouse
        clicked within a circle (to allow for dragging) and will see if the click
        event is contained within the axes.
        
        Upon doing so, this method will save the data of where the circle originally was,
        and it will identify where the mouse clicked.
        """
        if event.inaxes != self.circ.axes:
            return None;
        contains, attrd = self.circ.contains(event);
        if not contains:
            return None;

        print(event.xdata, event.ydata)
        x0, y0 = self.circ.center;
        self.press = x0, y0, event.xdata, event.ydata;
        # drag integration variables below
        # global Initiate;
        # Initiate = (event.xdata, event.ydata);
        return 0;

    def on_motion(self, event):
        u"""The :on_motion: method undergoes a similar identification process as the
        above method, except now it constantly updates and redraws the figure as
        the user drags the circle around. """

        if self.press is None:
            return None;
        if event.inaxes != self.circ.axes:
            return None;

        x0, y0, xpress, ypress = self.press;
        dx = event.xdata - xpress;
        dy = event.ydata - ypress;
        self.circ.center = (x0+dx, y0+dy)
        self.fig.canvas.draw();
        return 0;

    def on_release(self, event):
        u"""Upon releasing the draggable circle, this method will record and pritn the final
        resting position of the circle. This is intended to return the final value to our 
        proj129 script to update the positions for each mass."""

        if event.inaxes != self.circ.axes:
            return None
        contains, attrd = self.circ.contains(event)
        if not contains:
            return None
        
        self.press = None;
        self.fig.canvas.draw();
        print(event.xdata, event.ydata)
        # drag integration variables below
        # global Terminate;
        # Terminate = (event.xdata, event.ydata);
        return 0;

    def disconnect(self):
        u"""Disconnects circles when not in use using the mpl_disconnect method"""
        self.fig.canvas.mpl_disconnect(self.cidpress);
        self.fig.canvas.mpl_disconnect(self.cidrelease);
        self.fig.canvas.mpl_disconnect(self.cidmotion);
        return 0;


if __name__ == '__main__':
    fig = plt.figure();
    ax = fig.add_subplot(111);
    ax.axis([0, 100, 0, 100]);
    ax.set_title('Click to move the circle');

    circle1 = Circle((20,20), 2, color='red');
    circle2 = Circle((40,40), 2, color='green');
    circle3 = Circle((60,60), 2, color='blue');
    circles = [circle1, circle2, circle3];

    active = [];
    for circle in circles:
         ic = Drag(fig, ax, circle);
         ic.connect();
         active.append(ic);

    plt.show();
