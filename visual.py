# -*- coding: utf-8 -*-
# @Author: Chen Renjie
# @Date:   2020-08-26 21:58:05
# @Last Modified by:   Chen Renjie
# @Last Modified time: 2020-09-02 22:07:01


import os
import logging
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

FPS = 15
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s @ %(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %I:%M:%S')
logger = logging.getLogger(__name__)

logger.debug("Program Start")


class Draw3DSkeleton(object):
    def __init__(self, file_path, name="SBU", save_path='./out_skeleton'):
        self.name = name
        self.file_path = file_path
        self.save_path = save_path
        self.__xyz = self.read_xyz()

        if self.save_path and not os.path.exists(self.save_path):
            os.mkdir(self.save_path)

    def read_xyz(self):
        """
        read the 3D skeleton data from file
        :return: Numpy ndarray (T, M, V, C)
                T: number of frames
                M: number of peoples
                V: number of joints
                C: number of dimensions
        """
        with open(self.file_path, 'r') as f:
            data = f.readlines()
        frames = []
        for row in data:
            joints = [x.strip() for x in row.split(',')][1:]
            assert len(joints) % 3 == 0
            frame = []
            for i in range(2):
                subject = []
                for j in range(15):
                    subject.append(
                        [float(joints[45 * i + 3 * j]), float(joints[45 * i + 3 * j + 1]), float(joints[45 * i + 3 * j + 2])])
                frame.append(subject)
            frames.append(frame)
        frames = np.array(frames, dtype=np.float)

        return frames

    def info(self):
        return self.__xyz.shape

    def visual_skeleton(self, FPS=15):
        trunk_joints = [0, 1, 2]
        arm_joints = [5, 4, 3, 6, 7, 8]
        leg_joints = [11, 10, 9, 2, 12, 13, 14]

        fig = plt.figure()
        ax = Axes3D(fig)
        # ax.view_init(0, 45)

        def plotSubject(frame_idx, sid, color):
            x = self.__xyz[frame_idx, sid, :, 0]
            y = self.__xyz[frame_idx, sid, :, 2]
            z = -self.__xyz[frame_idx, sid, :, 1]

            ax.plot(x[trunk_joints], y[trunk_joints], z[trunk_joints], color=color, marker='o', markerfacecolor=color)
            ax.plot(x[arm_joints], y[arm_joints], z[arm_joints], color=color, marker='o', markerfacecolor=color)
            ax.plot(x[leg_joints], y[leg_joints], z[leg_joints], color=color, marker='o', markerfacecolor=color)

        def update(frame_idx):
            plt.cla()
            plt.title("%s (Frame: %d/%d)" % ("SBU", frame_idx + 1, self.__xyz.shape[0]))
            ax.set_xlim3d([-0.5, 1.5])
            ax.set_xticks([-0.5, -0.0, 0.5, 1.0, 1.5])
            ax.set_xlabel('X')
            ax.set_ylim3d([0, 2])
            ax.set_yticks([0, 1, 2, 3, 4])
            ax.set_ylabel('Y')
            ax.set_zlim3d([-1.5, 0.5])
            ax.set_zticks([-1.5, -1.0, -0.5, 0.0, 0.5])
            ax.set_zlabel('Z')
            plotSubject(frame_idx, 0, 'purple')
            plotSubject(frame_idx, 1, 'lightseagreen')
        ani = animation.FuncAnimation(fig, func=update, frames=self.__xyz.shape[0], interval=1000 / FPS, blit=False)
        plt.show()

if __name__ == "__main__":
    root = os.getcwd()
    path = os.path.join(root, "dataset", "SBU")
    files = os.listdir(path)
    file_path = os.path.join(path, files[0])

    obj = Draw3DSkeleton(file_path)
    obj.visual_skeleton()
# =========================================================

