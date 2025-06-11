import numpy as np

x = np.array([10, 20, 30, 40])
y = np.array([4, 5, 6, 1])



x_reshaped = x[None,:]
print("使用 x[:, None] 后的数组:")
print(x_reshaped)
print("使用 x[:, None] 后的形状:", x_reshaped.shape)

y_reshaped = y[:,None]
print("使用 x[:, None] 后的数组:")
print(y_reshaped)
print("使用 x[:, None] 后的形状:", y_reshaped.shape)
# print(x[None, :] * y[:, None])

z =  y_reshaped * x_reshaped

print(y_reshaped * x_reshaped)

print(x_reshaped * y_reshaped)