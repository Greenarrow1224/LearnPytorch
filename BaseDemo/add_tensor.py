import torch





def add_one():
    random_a = torch.rand(4, 2)
    random_b = torch.rand(4, 2)
    print(random_a + random_b)


def add_two():
    random_a = torch.rand(7, 5)
    random_b = torch.rand(7, 5)
    print(torch.add(random_a,random_b))

def add_three():
    random_a = torch.rand(6, 3)
    random_b = torch.rand(6, 3)
    print(random_a.add_(random_b))



if __name__ == '__main__':
    add_three()