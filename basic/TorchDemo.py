import torch

# 从 Python 列表创建
a = torch.tensor([1, 2, 3])           # 一维：向量
b = torch.tensor([[1, 2], [3, 4]])     # 二维：矩阵

# 常用创建函数
zeros = torch.zeros(3, 4)             # 3×4 的全零矩阵
ones = torch.ones(2, 3)               # 2×3 的全一矩阵
rand = torch.randn(2, 768)            # 2×768 的随机正态分布（模拟词嵌入）

# 查看形状
print(rand.shape)                      # torch.Size([2, 768])
print(rand.dtype)                      # torch.float32（默认数据类型）
