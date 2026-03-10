import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
transform = transforms.ToTensor()
trainset = torchvision.datasets.MNIST(
    root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(
    trainset, batch_size=64, shuffle=True)
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28*28, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
loss_function = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

loss_values = []

for epoch in range(3):

    total_loss = 0

    for images, labels in trainloader:

        optimizer.zero_grad()

        output = model(images)

        loss = loss_function(output, labels)

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    loss_values.append(total_loss)

    print("Epoch:", epoch+1, "Loss:", total_loss)

print("Training Completed")
plt.plot(loss_values)
plt.title("Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()
