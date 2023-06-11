import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

class show_chart(FigureCanvasQTAgg):
    def __init__(self, index):
        self.fig,self.ax = plt.subplots()
        super().__init__()
        self.index = index
        print("index",self.index)
        
        plt.close()
        plt.ion()
        self.loop()
        
    def loop(self):
        xp = np.array([1,2,3,4,5])
        yp = np.array([2,3,4,5,6])
        self.ax.plot(xp,yp)
        