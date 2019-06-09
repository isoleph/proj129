#!/usr/bin/python3
# this file specifies the token class to be used later

import tkinter as tk
# creates a class to specify dragging a tk element

global posR; global posG; global posB;
posR = (100,100); posG = (200,100); posB = (300, 200);



class drag(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent);

        # create a canvas
        self.canvas = tk.Canvas(width=1080, height=720);
        self.canvas.pack(fill="both", expand=True);

        # create dictionaries for drag data (to be updated by motion)
        self.collectData = {"x": 0, "y": 0, "item": None};

        # create three bodies; createToken is specified below
        self.createToken(posR, 'red');
        self.createToken(posG, 'green');
        self.createToken(posB, 'blue');

        # binds functions to clicking, dragging, and releasing
        self.canvas.tag_bind("token", "<ButtonPress-1>", self.onPress);
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.onRelease);
        self.canvas.tag_bind("token", "<B1-Motion>", self.onMotion);

        return None;

    # update posR, posG, and posB
    def update(self, x):

        global posR; global posG; global posB;

        if x == 1:
            posR = (self.collectData["x"], self.collectData["y"]);
        elif x == 2:
            posG = (self.collectData["x"], self.collectData["y"]);
        elif x == 3:
            posB = (self.collectData["x"], self.collectData["y"]);

        return 0;
        
    # make a circle for each token with coordinates
    def createToken(self, coord, color):

        (x, y) = coord
        self.canvas.create_oval(x-10, y-10, x+10, y+10, \
                                outline=color, fill=color, tags="token");

        return 0;

    # collect position when clicked
    def onPress(self, event):
        self.collectData["item"] = self.canvas.find_closest(event.x, event.y)[
            0]
        self.collectData["x"] = event.x;
        self.collectData["y"] = event.y;

        return 0;

    # collect position when released
    def onRelease(self, event):
        global posR;
        a = self.collectData["item"];
        self.update(a);
        
        return 0;

    # collect position as moved
    def onMotion(self, event):
        # calculate how much token has moved from last pos
        dx = event.x - self.collectData["x"];
        dy = event.y - self.collectData["y"];

        # move the object by dx, dy
        self.canvas.move(self.collectData["item"], dx, dy);

        # record the new position
        self.collectData["x"] = event.x;
        self.collectData["y"] = event.y;

        return 0;
