import matplotlib.pyplot as plt
from matplotlib.patches import Circle


class InteractiveCircle(object):

    def __init__(self):
        self.fig = plt.figure();
        self.ax = self.fig.add_subplot(111);
        self.ax.axis([0, 100, 0, 100]);
        self.press = None;
        
        self.create_token((20,20), 'red');
        self.ax.set_title('Click to move the circle')
        self.connect();
        return None;
        
    def create_token(self, coord, color):
        token = Circle(coord, 10, color=color);
        self.ax.add_artist(token);
        self.circ = token;
        return 0;

    def connect(self):
        self.cidpress = self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.cidrelease = self.fig.canvas.mpl_connect('button_release_event', self.on_release);
        self.cidmotion = self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)
        return 0;

    def on_click(self, event):
        if event.inaxes != self.circ.axes:
            return None;
        contains, attrd = self.circ.contains(event);
        if not contains:
            return None;

        print("Click detected")
        x0, y0 = self.circ.center;
        self.press = x0, y0, event.xdata, event.ydata;
        return 0;

    def on_motion(self, event):

        if self.press is None:
            return None;
        if event.inaxes != self.circ.axes:
            return None;

        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress;
        dy = event.ydata - ypress;
        self.circ.center = (x0+dx, y0+dy)
        self.fig.canvas.draw();
        return 0;

    def on_release(self, event):
        self.press = None;
        self.fig.canvas.draw();
        return 0;

    def disconnect(self):
        self.fig.canvas.mpl_disconnect(self.cidpress);
        self.fig.canvas.mpl_disconnect(self.cidrelease);
        self.fig.canvas.mpl_disconnect(self.cidmotion);
        return 0;

    def show(self):
        plt.show()


ic = InteractiveCircle();
plt.show();
