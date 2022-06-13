# import pandas as pd
# import cv2
# import os
# dir = "/home/mounted/AMain_codes/AMain/wholehere.csv"
# df = pd.read_csv(dir)
# # cols = ["image_name", "tags"]
# dfVal = pd.DataFrame()
# for (t), group in df.groupby(['tags']):
    

#         df_t = df.loc[df['tags'] == str(t)]
#         dfVal = pd.concat([dfVal,df_t.sample(n = round(0.2*(df_t.shape[0])))])
#         print("df_tShape", df_t.shape[0])
#         print("round", round(0.2*(df_t.shape[0])))
        
# dfVal = dfVal.sort_values(by ="tags")
# # print(dfVal)
# # dfVal.to_csv('test.csv', index=False)
# dftrain = df.drop(dfVal.index)

# print(dfVal)
# print(dftrain)
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------##
# import scipy
# from scipy import ndimage
# import matplotlib
# import matplotlib.pyplot as plt
# import matplotlib.colors as colors
# import numpy as np
# import scipy.misc
# import imageio
# import glob
# from scipy.signal import find_peaks_cwt
# from scipy.signal import find_peaks

# def CalculateHistValuse(img):

#     array=np.asarray(img)
#     # convert, but this is buggy 
#     im_hsv = matplotlib.colors.rgb_to_hsv(array[...,:3])
#     # pull out just the h channel
#     lu=im_hsv[...,0].flatten()
#     lu = lu * 360
#     # pd.DataFrame(lu).to_csv("sample.csv")
#     return lu

# # Totallu = np.ndarray([])
# Totallu = []
# path = '/home/mounted/Adataset/Train/histTest/garbage'
# for filename in glob.glob(path + '/*.png'):
#     img = imageio.imread(filename)
#     lu = CalculateHistValuse(img)
#     # print(len(lu))
#     for i in range(len(lu)):
#         Totallu.append(lu[i])
#     # lu = lu.tolist()
#     # Totallu.append(lu)

# h = plt.hist(Totallu,360)
# peaks, _ = find_peaks(h[0], height = 600000)
# print(peaks)
# # print(h)
# plt.title("Hue")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------##
import os
import glob



class myobj:
    def __init__(self):
        print("")

    def add(self):
        return 1+2
        
         

# def calculateIncorrects(auto, manual):
#     incorect = 0
#     with open(auto) as f1, open(manual) as f2:
#         lines1 = f1.readlines()
#         lines2 = f2.readlines()


#         for line in lines1:
#             if lines1[int(line)] != lines2[int(line)]:
#              print('yes')



# calculateIncorrects('/home/mounted/Adataset/ex/auto/20220420-144503197-13731-7J0AC6DPAK00016-f.txt', '/home/mounted/Adataset/ex/manual/20220420-144503197-13731-7J0AC6DPAK00016-f.txt')
        # for line1, line2 in zip(f1, f2):
            # print('line1', line1)
            # print
            # print(line1)
            # print(line2)
            # if line1[0] != line2[0]:
            #     incorect+=1

            
    # print('incorect is: ',incorect)
    # return incorect


# incorect = 0
# autoPath = '/home/mounted/Adataset/ex/auto'
# manualPath = '/home/mounted/Adataset/ex/manual'


# autolist = []
# manuallist = []
# for filename1 in glob.glob(autoPath + '/*.txt'):
#     autolist.append(filename1)
#     manuallist.append(os.path.join(manualPath, os.path.basename(filename1)))
#     for i in range(len(autolist)):
#         incorect = calculateIncorrects(autolist[i], manuallist[i]) + incorect




# print(incorect)
# print(autolist)
# print(manuallist)



