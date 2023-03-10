import json
from nltk_utils import tokenize, stem, bag_of_words
import numpy as np

# Importing PyTorch library
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from model import NeuralNet

# Load intents.json file
with open('intents.json', 'r') as f:
    intents = json.load(f)

all_words = [] # Collecting all of the tokenized words
tags = [] # Collecting all the different patterns
xy = [] # Creating an empty list that will hold both of our patterns and the tags

# Iterating through all the contents of the intents.json
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag) # Appending the tags to the tags array
    # Iterating through all the patterns in the intents.json file
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w) # Extending the all_words array to include the tokenized words
        xy.append((w, tag)) # Appending words and their corresponding tags to the xy array

# Creating a list of punctuation marks that are to be excluded from the all_words array
ignore_words = ['?', '!', '.', ',']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))


# Creating the training data
x_train = [] # Creating an array that would contain the bag of words
y_train = [] # Creating an array that would contain an associated number for each tag
# Iterating through the xy array
for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    # Appending the bag to the x_train array
    x_train.append(bag)
    
    label = tags.index(tag) # Creating a number associated with each tag
    y_train.append(label) # Appending the label to the y_train array

# Converting the training data to numpy arrays
x_train = np.array(x_train)
y_train = np.array(y_train)

# Creating a dataset class
class Chatdataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    # Supporting indexing such that dataset[i] can be used to get ith sample
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    # Calling the len(dataset to return the size)
    def __len__(self):
        return self.n_samples


# Hyperparameters
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(x_train[0])
learning_rate = 0.001
num_epochs = 1000

# Use the gpu if available else use the cpu
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Creating a dataset instance
dataset = Chatdataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=2)

model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Create the actual training loop
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(device)
    
        # Forward
        outputs = model(words)
        loss = criterion(outputs, labels)

        # Backward and optimizer step
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'epoch {epoch + 1}/{num_epochs}, loss={loss.item():.4f}')

print(f'final loss, loss={loss.item():.4f}')


# Saving the data
data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "output_size": output_size,
    "hidden_size": hidden_size,
    "all_words": all_words,
    "tags": tags
}
# Creating the file to store the data
FILE = "data.pth" # Naming the file
torch.save(data, FILE)

print(f'Training complete. File saved to {FILE}')