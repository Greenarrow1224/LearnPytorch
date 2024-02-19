import torch
from torchvision import models



def print_version():
    print(torch.__version__)
    print(torch.cuda.is_available())
    print(models.resnet152())
    # print(models.resnet101(pretrained=True))


if __name__ == '__main__':
    print_version()