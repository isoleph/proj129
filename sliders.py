#!/usr/bin/python3
# this file defines the tkinter sliders to be used

import tkinter as tk

class sliders(tk.Frame):

   def render(self):

      def __init__(self, parent):
         self.render();
         return None;

      global entries;
      entries = {};
      color = ['red', 'green', 'blue'];
      variables = ('Mass A', 'Mass B', 'Mass C');
      m_A = tk.DoubleVar(); m_B = tk.DoubleVar(); m_C = tk.DoubleVar();

      global masses;
      masses = [m_A, m_B,m_C];

      for variable, color, mass in zip(variables,color,masses):
         row = tk.Frame();
         label = tk.Label(row, width=10, text=variable+": ", anchor='w');
         entry = tk.Scale(row,
                           from_=0,
                           to=500,
                           orient=tk.HORIZONTAL,
                           length=200,
                           showvalue=True,
                           troughcolor=color,
                           bg='grey',
                           variable=mass
            )

         # input positions and specs for the GUI
         row.pack(side=tk.TOP, fill=tk.X, padx=3, pady=3);
         label.pack(side=tk.LEFT);
         entry.pack(side=tk.LEFT, expand=False, fill=tk.X);
         entry.set(100);
         entries[variable] = entry.get();

      return 0;

   def get_input():
      massList = [mass.get() for mass in masses];
      print("Your mass inputs:");
      print(massList);
      return 0;
