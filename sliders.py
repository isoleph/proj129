#!/usr/bin/python3
# this file defines the tkinter sliders to be used

import tkinter as tk

color = ['red','green','blue'];
variables = ('Mass A', 'Mass B', 'Mass C');

def sliders(master, variables=variables, color=color):

   entries = {};

   for variable, color in zip(variables,color):
      row = tk.Frame(master);
      label = tk.Label(row, width=10, text=variable+": ", anchor='w');
      entry = tk.Scale(row,
                       from_=0,
                       to=500,
                       orient=tk.HORIZONTAL,
                       length=200,
                       showvalue=True,
                       troughcolor=color
        )

     # input positions and specs for the GUI
      row.pack(side=tk.TOP, fill=tk.X, padx=3, pady=3);
      label.pack(side=tk.LEFT);
      entry.pack(side=tk.LEFT, expand=False, fill=tk.X);
      entries[variable] = entry;

   return entries
