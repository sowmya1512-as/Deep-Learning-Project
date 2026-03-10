# Deep-Learning-Project
Company : CODETECH IT SOLUTIONS

Name : Sowmya GS

Intern ID : CTIS6512

Domain : Data Science

Duration : 4 Weeks

Mentor : Neela Santhosh

Description about the Task :
Description of the Program (≈500 Words)

This program demonstrates the implementation of a simple deep learning model for image classification using PyTorch, along with supporting libraries such as Torchvision and Matplotlib. The main objective of the program is to train a neural network to recognize handwritten digits from the MNIST Dataset and visualize the training performance using a graph.

The program begins by importing the necessary libraries. PyTorch is a popular deep learning framework used for building and training neural networks. Torchvision is a library that provides access to commonly used datasets and image transformation tools. Matplotlib is used for visualizing data in the form of graphs and plots.

In the first step, the program loads the MNIST dataset using the torchvision.datasets.MNIST function. The MNIST dataset is a widely used dataset in machine learning and deep learning research. It consists of 70,000 grayscale images of handwritten digits ranging from 0 to 9. Each image has a resolution of 28×28 pixels. In this program, the dataset is automatically downloaded and stored locally if it is not already available. Before feeding the images into the neural network, they are converted into tensor format using transforms.ToTensor(). Tensors are the basic data structures used by PyTorch to perform numerical computations.

After loading the dataset, a DataLoader is created using torch.utils.data.DataLoader. The DataLoader helps in loading the dataset in smaller batches instead of processing the entire dataset at once. In this program, a batch size of 64 is used, which means that 64 images are processed in each iteration during training. The shuffle parameter is set to true so that the training data is randomly shuffled in every epoch, which helps improve the learning performance of the model.

Next, the program defines a simple neural network using nn.Sequential. The neural network consists of multiple layers. The first layer is a Flatten layer, which converts the 28×28 pixel image into a one-dimensional vector of size 784. This flattened vector is then passed to a fully connected linear layer with 128 neurons. A ReLU activation function is applied to introduce non-linearity into the model, allowing it to learn complex patterns in the data. Finally, another linear layer maps the 128 neurons to 10 output neurons, representing the ten possible digit classes from 0 to 9.

Once the neural network is defined, the program specifies a loss function and an optimizer. The loss function used is CrossEntropyLoss, which is commonly used for multi-class classification problems. The optimizer used in the program is the Adam optimizer, which updates the weights of the neural network during training to minimize the loss.

The model is then trained for three epochs using a training loop. During each epoch, the images are passed through the network to generate predictions. The loss between the predicted values and the actual labels is calculated using the loss function. The gradients are then computed through backpropagation, and the optimizer updates the model parameters accordingly. The total loss for each epoch is stored and printed to the console.

Finally, the program visualizes the training progress by plotting the loss values using Matplotlib. The graph shows how the training loss decreases across epochs, indicating that the model is learning and improving its predictions. This visualization helps in understanding the performance of the model during the training process.

output :
<img width="1445" height="863" alt="Image" src="https://github.com/user-attachments/assets/5516266a-2229-4eb2-9fb3-4165cf886e3d" />
