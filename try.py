import numpy as np
import matplotlib.pyplot as plt

# 物理常量
v0 = 16.0  # 初速度 m/s
g = 9.8    # 重力加速度 m/s^2
theta0_deg = 80.0  # 发射角
theta0 = np.radians(theta0_deg)

# 飞行总时间 T = 2 * v0 * sin(theta) / g
T = 2 * v0 * np.sin(theta0) / g

# 生成时间数组 (从0到T, 500个点)
t = np.linspace(0, T, 500)

# 计算位置 x, y
x = (v0 * np.cos(theta0)) * t
y = (v0 * np.sin(theta0)) * t - 0.5 * g * t**2

# 计算位置矢量的大小 r
r = np.sqrt(x**2 + y**2)

# 绘图
plt.figure(figsize=(8, 5))
plt.plot(t, r, color='blue', linewidth=2)
plt.axvline(x=3.11, color='red', linestyle='--', label='Max r at t ≈ 3.11 s')

# 设置图表文字
plt.title(f'Magnitude of Position Vector \(r\) vs Time (θ₀ = {theta0_deg}°)')
plt.xlabel('Time t (s)')
plt.ylabel('Position Magnitude r (m)')
plt.grid(True)
plt.legend()

# 显示图表
plt.show()