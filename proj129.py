#!/usr/bin/python3

import tkinter as tk
import tokens
from tokens import drag
from sliders import *

def data():
    sliders.get_input();
    print("Your coordinates: ")
    print("{}; {}; {}".format(tokens.posR, tokens.posG, tokens.posB));

    return 0;


if __name__ == "__main__":

    # initialize tk
    master = tk.Tk();

    # set window name
    master.wm_title("Gravitational Contour Plot");

    # set window size
    master.geometry("1080x720");

    # determine entries from sliders module
    ents = sliders.render(master);

    # create buttons with commands
    b1 = tk.Button(master, text='Calculate', \
                  command=data);
    b1.pack(side=tk.BOTTOM);

    b2 = tk.Button(master, text='Quit', command=master.quit);
    b2.pack(side=tk.RIGHT);
    drag(master).pack(fill="both", expand=True);

    # Drive!
    master.mainloop();
