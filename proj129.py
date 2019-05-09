import tkinter as tk

masses = ('Mass A', 'Mass B', 'Mass C');

global L, M; # starting coordinates
L = [(100,100), (200,200), (300,200)];
M = [];

def main():
    return 0;

# create a dictionary of values in the list
def form(master, masses):

   entries = {};
   for mass in masses:
      row = tk.Frame(master);
      label = tk.Label(row, width=10, text=mass+": ", anchor='w');

      entry = tk.Entry(row);
      entry.insert(0, "0");

     # input positions and specs for the GUI
      row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5);
      label.pack(side=tk.LEFT);
      entry.pack(side=tk.LEFT, expand=False, fill=tk.X);
      entries[mass] = entry 

   return entries;


# creates a class to specify dragging a tk element
class drag(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent);

        # create a canvas
        self.canvas = tk.Canvas(width=620, height=380);
        self.canvas.pack(fill="both", expand=True);

        # create dictionaries for drag data (to be updated by motion)
        self.collectData = {"x": 0, "y": 0, "item": None};

        # create three bodies; createToken is specified below
        self.createToken((100, 100), 'black');
        self.createToken((200, 100), 'black');
        self.createToken((300,200), 'black');

        # define binding for clicking, dragging, and releasing; spec'd below
        self.canvas.tag_bind("token", "<ButtonPress-1>", self.onPress);
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.onRelease);
        self.canvas.tag_bind("token", "<B1-Motion>", self.onMotion);

        return None;

    # make a circle for each token with coordinates
    def createToken(self, coord, color):
    
        (x, y) = coord 
        self.canvas.create_oval(x-10, y-10, x+10, y+10,
                 outline=color, fill=color, tags="token");
        # send out initial coordinates 
        return 0;

    # collect position when clicked
    def onPress(self, event):
        self.collectData["item"] = self.canvas.find_closest(event.x, event.y)[0];
        self.collectData["x"] = event.x;
        self.collectData["y"] = event.y;
        M.insert(0, (event.x, event.y))

        return 0;

    # collect position when released
    def onRelease(self, event):
        self.collectData["item"] = None;
        L.insert(0,(event.x,event.y));
        return 0;

    # collect position as moved
    def onMotion(self, event):
        # calculate how much mouse has moved from last pos
        dx = event.x - self.collectData["x"];
        dy = event.y - self.collectData["y"];

        # move the object by dx, dy
        self.canvas.move(self.collectData["item"], dx, dy);

        # record the new position
        self.collectData["x"] = event.x;
        self.collectData["y"] = event.y;

        return 0;


if __name__ == "__main__":

    # initialize tk
    master = tk.Tk();
    # set window size
    master.geometry("720x480");
    # determine entries from function waaay above
    ents = form(master, masses);
    master.bind('<Return>', (lambda event, e=ents: fetch(e)));

    # create buttons with commands! 
    b1 = tk.Button(master, text='Reset',
                  command=(lambda e=ents: main()));
    b1.pack(side=tk.BOTTOM, padx=5, pady=5);

    b2 = tk.Button(master, text='Calculate',
                  command=(lambda e=ents: main()));
    b2.pack(side=tk.BOTTOM, padx=5, pady=5);

    b3 = tk.Button(master, text='Quit', command=master.quit);
    b3.pack(side=tk.RIGHT, padx=5, pady=5);
    drag(master).pack(fill="both", expand=True);

    # Drive!
    master.mainloop();

print(L);
print(M);
