"""
Plotting Utility
converts csv to img files
Plots overall intensity vs position if position file exists
Michael Douglass
"""

import matplotlib.pyplot as plt
from PIL import Image
import os
import numpy as np


def main():
    frames = []
    for file in os.listdir():
        if file.startswith('frame') and file.endswith('.csv'):
            frames.append(file)

    try:
        positions = np.loadtxt('positions.csv')
    except:
        print('There is no positions file.')
        positions = []

    if len(frames) > 0:
        if os.path.exists('Images') != True:
            os.mkdir('Images')

        sumIntensity = []
        for frame in frames:
            frameStr = frame.split('.')[0]
            frameData = np.loadtxt(frame, delimiter=',')
            sum = np.sum(frameData)
            sumIntensity.append(sum)
            img = Image.fromarray(frameData)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save('Images/'+frameStr+'.png', 'PNG')
    else:
        print('There are no frames to analyze.')

    if len(positions) > 0:
        np.savetxt('intensity.csv', sumIntensity, delimiter=',')
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(positions, sumIntensity)
        ax.set_xlabel('Position (mm)')
        ax.set_ylabel('Intensity')
        plt.tight_layout()
        plt.savefig('Images/intensityProfile.png')


if __name__ == '__main__':
    main()
