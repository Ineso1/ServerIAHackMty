# ServerHackMty

## Artificial Intelligence and Server

A project is proposed that detects and organizes garbage through artificial vision, which is composed of two parts of the project:

* Python files with trained artificial intelligence
* Server to interpret in react
* Matlab scripts to analyze training

**Images**<br><br>
![image](https://user-images.githubusercontent.com/84602829/212252108-178e2720-a5ec-4758-bf11-bb8722b873ff.png)

![image](https://user-images.githubusercontent.com/84602829/212252218-fa3d170f-23f0-47f3-80a0-59ca7902146c.png)

# Project Description

## Inspiration
We realized that a very common problem is not knowing which container to put the garbage in, and often even though there are different bins for organic, plastics, paper, others, etc., people end up throwing waste in the wrong place.
## What it does
Classifies garbage through an AI to correctly sort it, and with hardware it can then separate and deposit the waste in the correct place.
## How we built it
We trained a GoogleNet deep learning model for image recognition to distinguish between different types of garbage (organic, plastics, paper, others, etc.) and designed a prototype system for automated control with catFiles of what will be the proposed intelligent garbage bin.
## Challenges we ran into
First, we faced the problem of finding appropriate datasets to train the model because we couldn't find specifically what we needed for the problem.
Complications linking technologies such as React with Flask and developing a backend using various programming languages (Python, JS, and Matlab).
## Accomplishments that we're proud of
-AI\
-Catfiles

## What we learned
AI, deep learning, tensorflow, web design
## What's next for IA reconocimiento de desechos (AI recognition of waste)
Completely develop a prototype to be mass-produced.

# Installation

## Run the server
To run the server you need to clone the repository and initialize the file manage.py and start the server.

```bash
  npm start
```

## Try the Python script
To try the Python script, run the following commands:

```bash
  pip install ./IA/requirements.txt
  python ./IA/camera.py
```
Once it starts, the camera will pop-up and you should press the spacebar with the garbage item you want to classify. Then another image will pop-up with the classification made by the model

# Contributors
- [@Armandotrsg](https://github.com/Armandotrsg)
- [@HugoGoHe](https://github.com/HugoGoHe)
- [@Inseo1](https://github.com/Ineso1)
- [@DanielMunoz4190](https://github.com/DanielMunoz4190)
