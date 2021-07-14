# A very simple webapp
This webapp has been setup for you to easily run a local server. But you still need to set up your local environment first. You can preview what your app will look like at the end of my guide here: https://basilapp.xyz

**NOTE**: I have not uploaded the machine learning model to this repository, as Git shouldn't really be used for large objects.

## Setup
I recommend that you fork this to your own account first, and then clone it. This way you can push updates to your own repo!

To set this up, make sure you have Python 3.7.9 installed - don't use 3.9 because certain libraries aren't available for the version yet. You can get it from here:
https://www.python.org/downloads/release/python-379/ - be careful of your existing python installation! Might be a good idea to uninstall your old one first.


You can use GitHub Desktop to easily clone this - or the command line if you're feeling adventurous.

### Virtual Environment

Open up a terminal or cmd/powershell and type

`python -m venv venv` or `python3 -m venv venv` or possibly `python.exe -m venv venv` if your installation is a little strange.

What this does is it sets up a 'virtual environment' called 'venv' which is stored in the venv folder. This will contain all the libraries, the python executable etc that is specific to this project.

You can then activate it with:

`.\venv\Scripts\activate`

or `source venv/Scripts/activate` if you're on a Mac.

Now, any `pip install` or `python` commands will be installing into/using the venv folder!

### Installing dependencies

Now you can install your requirements, which I've separated into Windows and Mac - note: I'm using an older version of PyTorch because the newer one is way bigger for some reason, and we don't need the new features.

Now you can run:

`pip install -r requirements.txt`

or `pip install -r requirements-mac.txt` if you're on a Mac.

This will read the requirements file and then install the required dependencies into your venv folder.

## Run it!

Great, now you're *nearly* ready to load your model!**IMPORTANT: Place your model (named `dogscats.pt`) under a new folder called `models` at the root of your project** and then you should be able to run:

`flask run`

Now if you go to http://localhost:5000 you should be able to see a very very simple webapp! You can upload an image and predict the class! Nice.


### Improve it!

...But it kinda looks bad, so here are the next steps to making it look more gooder:
https://docs.google.com/document/d/1uS1obu0A6CJKWx8NC8B1Ejw_6cQsub9bA6AItjyjzXY/edit?usp=sharing

### Potential problems
- Make sure you activate your virtual environment! Otherwise you won't have access to the libraries you need (`flask run` will not work).
