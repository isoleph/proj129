#!/usr/bin/env python3
# physics129L capstone project;

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from scipy.spatial import distance

global data;
data = {'red': (20, 20), 'green': (60, 60), 'blue': (80, 80)};

# ad hoc class to access data array from other script
class PointData(object):
    def __init__(self):
        return None;

    def getArray(self):
        global data;
        return data;



# create a class to define draggable buttons
class Drag(object):

    def __init__(self, fig, ax, circle):
        u"""Upon initiation the Drag class will input the relevant mpl \
        figure, axis, and circle elements and then it will \
        display them to the window."""

        # import mpl figures and axes
        self.fig = fig; self.ax = ax;

        # create data to track particle
        self.press = None;
        self.circ = circle;
        self.ax.add_patch(circle);
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

        Drag.Initiate = event.xdata, event.ydata
        self.identify(event)

        x0, y0 = self.circ.center;
        self.press = x0, y0, event.xdata, event.ydata;
        # drag integration variables below
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
        self.fig.canvas.draw_idle();
        return 0;

    def on_release(self, event):
        u"""Upon releasing the draggable circle, this method will record and print the final
        resting position of the circle. This is intended to return the final value to our 
        proj129 script to update the positions for each mass."""

        if event.inaxes != self.circ.axes:
            return None
        contains, attrd = self.circ.contains(event)
        if not contains:
            return None
        
        self.press = None;
        self.fig.canvas.draw_idle();
        # drag integration variables below
        self.Terminate = (event.xdata, event.ydata);

        global data;
        data[Drag.identify(self,event)] = self.Terminate;
        print("data:", data);
        return 0;

    def disconnect(self):
        u"""Disconnects circles when not in use using the mpl_disconnect method"""
        self.fig.canvas.mpl_disconnect(self.cidpress);
        self.fig.canvas.mpl_disconnect(self.cidrelease);
        self.fig.canvas.mpl_disconnect(self.cidmotion);
        return 0;

    # update locations after motion
    def identify(self, event):
        global data;
        values = list(data.values() );
        closest_index = distance.cdist([self.Initiate], values).argmin();
        print(closest_index)

        if closest_index == 0:
            return 'red';
        elif closest_index == 1:
            return 'green';
        elif closest_index == 2:
            return 'blue';


if __name__ == '__main__':
    fig = plt.figure();
    ax = fig.add_subplot(111);
    ax.axis([0, 100, 0, 100]);
    ax.set_title('Preliminary Circle Module');

    circle1 = Circle((20,20), 2, color='red');
    circle2 = Circle((40,40), 2, color='green');
    circle3 = Circle((60,60), 2, color='blue');
    circles = [circle1, circle2, circle3];

    active = [];
    for circle in circles:
         ic = Drag(fig, ax, circle);
         active.append(ic);

    plt.show();
