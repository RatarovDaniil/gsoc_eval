import h5py
import argparse
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import medfilt

# parse arguments
parser = argparse.ArgumentParser(description='Create .csv file with all of the groups and datasets.')
parser.add_argument('input', help='path to the input file')

args = parser.parse_args()

with h5py.File(args.input, 'r') as file:
    img_data = file['/AwakeEventData/XMPP-STREAK/StreakImage/streakImageData']
    width = file['/AwakeEventData/XMPP-STREAK/StreakImage/streakImageWidth'][0]
    height = file['/AwakeEventData/XMPP-STREAK/StreakImage/streakImageHeight'][0]

    # reshape image data
    img = np.reshape(img_data, (height, width))

    # filter image data
    filt_img = medfilt(img)

    # showing image
    plt.imshow(filt_img)
    
    # saving image
    plt.savefig('streak_image.png')
    plt.show()