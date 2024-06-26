import torch.nn as nn
import torch.optim as optim


x1 = torch.tensor([1.0])
w1 = torch.tensor([3.0])
x2 = torch.tensor([2.0])
w2 = torch.tensor([4.0])

b = torch.tensor([5.0])

x1.requires_grad = True
x2.requires_grad = True
w1.requires_grad = True
w1.requires_grad = True

n = x1 * w1 + x2 * w2  + b
o = torch.tanh(n)


print(o.data.item())
#create nodes
#assigne values to nodes, could be a value node or weight node
#have add or multiply operation
#have forward and backward operation
#For backward operation, need to put in a topological order and reverse the order then do the backward operation

#have a loss function
