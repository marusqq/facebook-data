# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"

import random

"""class used to generate plots and graphs for later use for data visualisation in reports"""

# generic
import parser.util as util


# class specific
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
import pandas as pd


class Plotter:
    def __init__(self, name, data, arg_to_plot, dir_to_save_plot=None):

        plt.style.use("dark_background")
        self.name = name
        self.data = data
        self.arg_to_plot = arg_to_plot
        self.dir_to_save_plot = dir_to_save_plot

        # self.plot_count = plots

        self.fig = plt.figure()
        self.ax = plt.axes()

        self._customise_plots(suptitle_name=self.name)

    def _customise_plots(self, suptitle_name):

        self.fig.set_size_inches(16, 5)
        self.fig.suptitle(suptitle_name)
        self.fig.patch.set_facecolor("#121212")

        # for i in range(self.plot_count):
        #
        #     self.ax[i].patch.set_facecolor("#121212")
        #     self.ax[i].yaxis.tick_right()
        #     self.ax[i].get_yaxis().set_major_locator(LinearLocator(numticks=7))

        return

    def plot_bar_dict_multiple_bars(self, name, data, colors=None, total_width=0.8, single_width=1, legend=True):
        """Draws a bar plot with multiple bars per data point.

        Parameters
        ----------
        ax : matplotlib.pyplot.axis
            The axis we want to draw our plot on.

        data: dictionary
            A dictionary containing the data we want to plot. Keys are the names of the
            data, the items is a list of the values.

            Example:
            data = {
                "x":[1,2,3],
                "y":[1,2,3],
                "z":[1,2,3],
            }

        colors : array-like, optional
            A list of colors which are used for the bars. If None, the colors
            will be the standard matplotlib color cyle. (default: None)

        total_width : float, optional, default: 0.8
            The width of a bar group. 0.8 means that 80% of the x-axis is covered
            by bars and 20% will be spaces between the bars.

        single_width: float, optional, default: 1
            The relative width of a single bar within a group. 1 means the bars
            will touch eachother within a group, values less than 1 will make
            these bars thinner.

        legend: bool, optional, default: True
            If this is set to true, a legend will be added to the axis.
        """
        print(name)
        # Check if colors where provided, otherwhise use the default color cycle
        if colors is None:
            colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

        # Number of bars per group
        n_bars = len(data)

        # The width of a single bar
        bar_width = total_width / n_bars

        # List containing handles for the drawn bars, used for the legend
        bars = []

        # Iterate over all data
        for i, (name, values) in enumerate(data.items()):
            # The offset in x direction of that bar
            x_offset = (i - n_bars / 2) * bar_width + bar_width / 2

            # Draw a bar for every value of that type
            for x, y in enumerate(values):
                bar = self.ax.bar(x + x_offset, y, width=bar_width * single_width, color=colors[i % len(colors)])

            # Add a handle to the last drawn bar, which we'll need for the legend
            bars.append(bar[0])

        plt.xticks(range(data.keys()), data.keys())

        # Draw legend if we need
        if legend:
            self.ax.legend(bars, data.keys())

        plt.show()

    def plot_bar(self):

        colors = ["white", "red", "blue", "yellow", "green", "cyan"]

        current_color = random.choice(colors)
        self.data[self.arg_to_plot].plot(kind='bar', color=current_color)
        # self.ax.plot(self.data.index, self.data[arg_to_plot], current_color, kind='bar')
        self.ax.legend([self.arg_to_plot], loc="lower left")
    # self.ax[0].plot(df.index, df.Close, color="white")
        # self.ax[0].legend(["Close"], loc="lower left")
        #
        # self.ax[1].plot(df.index, df.RSI, color="#33FFFF")
        # self.ax[1].legend(["RSI"], loc="lower left")
        #
        # self.ax[2].plot(df.index, df.MACD, color="yellow")
        # self.ax[2].plot(df.index, df.MA, color="#6600CC")
        # self.ax[2].bar(df.index, df.MACD_BAR, color="white")
        # self.ax[2].legend(["MACD", "MA", "MACD_BAR"], loc="lower left")

        plt.show()

        if self.dir_to_save_plot:
            saved_dir = self._save_plot(
                name=self.name,
                dire=self.dir_to_save_plot,
                file_ext=".png",
            )

            return saved_dir
        return None

    def _save_plot(self, dire, name, file_ext=".png"):
        saving_dir = dire + "/" + name + file_ext
        self.fig.savefig(saving_dir)
        return saving_dir
