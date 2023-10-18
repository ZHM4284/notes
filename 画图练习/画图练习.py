import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-50,50,1000)
y=x**2
plt.figure("测试",figsize=(8,5))
plt.plot(x,y)
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 将 bottom 即是 x 坐标轴设置到 y=0 的位置。
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))

# 将 left 即是 y 坐标轴设置到 x=0 的位置。
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.set_title('y = x^2',fontsize=14,color='r')

plt.show()