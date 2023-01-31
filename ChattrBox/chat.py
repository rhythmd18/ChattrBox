# Importing the desired libraries
import random
import json
import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

# Check for gpu support
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the intents.json file
with open('intents.json', 'r') as f:
    intents = json.load(f)

FILE = 'data.pth'
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()