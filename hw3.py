import cv2
import numpy as np

# 读取输入图片并获取图片的像素高度与 宽度
input = cv2.imread('301.jpeg', 1)
num_rows = input.shape[0]
num_cols = input.shape[1]

output = np.zeros((num_rows*2+1, int(num_cols*1.5), 3), dtype=np.uint8)
output[0: num_rows, 0: num_cols] = input[:, :]
# 根据光束照射方向知投影后
# x1=x0，y1=(1/2)z0，z1=0
for row in range(num_rows):
    col_idx = int(1/2*(num_rows-row))
    output[2*num_rows-row, col_idx: col_idx+num_cols] = input[row, :]

# 显示输 出图片
cv2.imshow('output.jpeg', output)
cv2.waitKey(0)