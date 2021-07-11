import torchvision 
import torch.nn as nn 
import torch 
import torch.nn.functional as F 
from torchvision import transforms,models,datasets 
import matplotlib.pyplot as plt 
from PIL import Image 
import numpy as np 
from torch import optim
from collections import OrderedDict 

class DogsCatsPredictor:
    transform = transforms.Compose([transforms.Resize(255), 
                                transforms.CenterCrop(224), 
                                transforms.ToTensor()]) 

    model = models.densenet121(pretrained = False)

    """Initialise our own model, using the DenseNet class as a base"""
    def __init__(self, modelPath):
        for params in self.model.parameters(): 
            params.requires_grad = False 

        classifier = nn.Sequential(OrderedDict([ 
            ('fc1',nn.Linear(1024,500)), 
            ('relu',nn.ReLU()), 
            ('fc2',nn.Linear(500,2)), 
            ('Output',nn.LogSoftmax(dim=1)) 
        ]))

        self.model.classifier = classifier 
        #Load our model parameters, we are using the CPU now
        self.model.load_state_dict(torch.load(modelPath, map_location=torch.device('cpu')))
        self.model.eval()
    
    """Takes a PIL image and predicts if it's a cat or dog"""
    def predictCatOrDog(self, image):
        input = self.transform(image)
        #Transforming the image tensor into something model expects (unsqueeze)
        input_batch = input.unsqueeze(0)

        #This a bunch of probabilities for each class i.e. for cat or dog
        output = self.model(input_batch)
        #Get the "max" probability out of the two classes
        pred = torch.argmax(output, dim=1) 
        #Convert it into a general Python number instead of a PyTorch tensor
        pred = [p.item() for p in pred]

        #Note: this depends on what data set you loaded! 
        #use dataset.class_to_idx on the dataset on the Google Colab file to see the mapping
        labels = {0:'Cat', 1:'Dog'}

        #Map the class index (idx) to the name
        #print(labels[pred[0]])
        return labels[pred[0]]