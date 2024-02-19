# 导入PyTorch
import torch



"""
    官方文档地址：https://pytorch.org/docs/2.1/torch.html#creation-ops
"""


#
def create_empty_torch(a,b):
    """
    Args:
    a:
    b:
    创建一个 [a] x [b] 的未初始化的 Tensor
    :return: Returns a tensor filled with uninitialized data.
    """

    empty = torch.empty(a,b)
    print(empty)



def create_zero_torch():
    """
    创建一个 7x5 的 long 类型全是 0 的 Tensor
    Returns:
        Returns a tensor filled with the scalar value 0, with the shape defined by the variable argument size
    """

    zero = torch.zeros(7,5,dtype=torch.long)
    print(zero)

def create_data_torch():
    """
    Constructs a tensor with no autograd history (also known as a "leaf tensor", see Autograd mechanics) by copying data
    :return:
    """
    data = torch.tensor([12.5,7])
    print(data)

def create_data_2_torch():
    data = torch.tensor([12.5, 7])
    # 返回的 tensor 默认具有相同的 torch.dtype 和 torch.device
    data = data.new_ones(2, 1, dtype=torch.float64)
    print(data)
    # 指定新的数据类型
    data = torch.randn_like(data, dtype=torch.float)
    print(data)


if __name__ == '__main__':
    create_data_2_torch()