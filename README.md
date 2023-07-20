# ChattrBox

## Demo Link:  https://rb.gy/u556c

## Description: 
ChattrBox is a simple and lightweight conversational AI chatbot which has been built primarily using Flask as the main backend framework. It uses the PyTorch library which has been used to train the data and the nltk(Natural Language Toolkit) library for Natural Language Processing. It uses a Feed Forward Neural Network with two hidden layers.
For the frontend, technologies used are HTML, CSS, and JavaScript with BootStrap for the aesthetics.
It's a very basic chatbot, and so conversations that accurately replicate a real world conversation is not to be expected. Nonetheless, it should still be pretty enjoyable!

## Technologies Used:
### Backend:
1) Python
2) Flask
3) PyTorch
4) nltk
5) SQLite (for storing user's data)
### Frontend:
1) HTML
2) CSS
3) JavaScript
4) BootStrap 5

## Files and Folders used:
### app.py
This is the main file that runs at the backend and handle each and every functionality of the application.
### chat.py
This is the file that contains the implementation of the actual chatting. The trained model is loaded here and depending upon the question asked by the user, it generates adequate response using the trained machine learning model.
### model.py
This is the main machine learning model which implements the Feed Forward Neural Network with two hidden layers and is used by train.py and chat.py files to train the machine learning model and use that model for realizing the notion of chatting.
### train.py
This is the file that is used to train the machine learning model. It implements the actual NLP(Natural Language Processing) algorithm i.e.:
1) Tokenization
2) Stemming
3) Excluding punctuations
4) Creating the bag of words

Using these steps, the train.py file trains on the data.
### nltk_utils.py
This is the file where the implementation of the above functions takes place. The functions are then imported within the train.py file to train the model on the data
### intents.json
This is the actual data which the machine learning model is trained on. It contains all possible questions and their corresponding responses which could possibly make up a conversation between two subjects.
### static folder
This is a folder that contains all the image files that have been used in the application, styling, and the code for the overall aesthetics of the application. Within this folder, there is a file named app.js which contains the JavaScript code for the implementation of the notion of chatting with the bot.
### templates folder
This folder contains all the templates that have been used for the frontend UI. These templates have been stitched together, so to speak, using Flask.

## Features/Walkthrough (Check out the demo video for a detailed walkthrough)
### Sign In/Register
This is the page where the user can sign themselves in (or register if they don't have an account by clicking on the register button)
### Welcome page
After signing in (or registering) the user is welcomed by the bot to join the chat.
### Chat room
After accepting the invitation, the user is redirected to the chat room to the chat with the bot. The user may start their conversation with the bot simply by typing on the text box provided below and click on the send button (or press Enter) and the bot should give an appropriate response.
### Changing password
The user is given the ability to change their password if they want to. They, however will need to type in their current password and then the new password with a confirmation.
### Deleting account
If the user wants to discontinue using ChattrBox, they may wish to delete their account. They simply need to type in their password to continue with the process of deletion.
### About Section
This is the page where the user is gets to know about the application more. Users can give their feedback by going on the link provided on this page and also can get access to the entire source code of this application if they wish to by another link.
### Changing Color modes
Users have been given the ability to toggle the color mode between light and dark as per their preference. They can do so before and after logging in whenever they wish.

## Courtesies:
1) This repo was taken as a reference for the implementation of the chatbot: https://github.com/patrickloeber/chatbot-deployment
2) ChatGPT: For some styling and aesthetics, and some debugging
