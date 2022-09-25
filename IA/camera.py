import torch
#model = torch.hub.load('pytorch/vision:v0.10.0', 'googlenet', pretrained=True)
from googlenet_pytorch import GoogLeNet
model = GoogLeNet.from_pretrained('googlenet')
model.eval()

# Open the camera
import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
    
    k = cv2.waitKey(1)
    if k%256 == 32:
        # SPACE pressed
        img_name = "foto.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        break

cam.release()

cv2.destroyAllWindows()

filename = img_name

from PIL import Image
from torchvision import transforms
input_image = Image.open(filename)
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
input_tensor = preprocess(input_image)
input_batch = input_tensor.unsqueeze(0) # create a mini-batch as expected by the model

# move the input and model to GPU for speed if available
if torch.cuda.is_available():
    input_batch = input_batch.to('cuda')
    model.to('cuda')

with torch.no_grad():
    output = model(input_batch)
# Tensor of shape 1000, with confidence scores over Imagenet's 1000 classes
#print(output[0])
# The output has unnormalized scores. To get probabilities, you can run a softmax on it.
probabilities = torch.nn.functional.softmax(output[0], dim=0)
#print(probabilities)

# Download ImageNet labels
#Check if the file exists
import os
if not os.path.exists('imagenet_classes.txt'):
    import wget
    url = 'https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt'
    filename = wget.download(url)

# Read the categories
with open("imagenet_classes.txt", "r") as f:
    categories = [s.strip() for s in f.readlines()]
# Show top categories per image
top5_prob, top5_catid = torch.topk(probabilities, 5)
for i in range(top5_prob.size(0)):
    print(categories[top5_catid[i]], top5_prob[i].item())

food = """
ice cream
ice lolly
French loaf
bagel
pretzel
cheeseburger
hotdog
mashed potato
head cabbage
broccoli
cauliflower
zucchini
spaghetti squash
acorn squash
butternut squash
cucumber
artichoke
bell pepper
cardoon
mushroom
Granny Smith
strawberry
orange
lemon
fig
pineapple
banana
jackfruit
custard apple
pomegranate
hay
carbonara
chocolate sauce
dough
meat loaf
pizza
potpie
burrito
red wine
espresso
cup
eggnog
"""

food = food.split()

if "paper" in str(categories[top5_catid[0]]) or "tissue" in str(categories[top5_catid[0]]) or "envelope" in str(categories[top5_catid[0]]):
    tipo = "paper"
elif "beer" in str(categories[top5_catid[0]]) or "glass" in str(categories[top5_catid[0]]):
    tipo = "glass"
elif "plastic" in str(categories[top5_catid[0]]) or "bottle" in str(categories[top5_catid[0]]):
    tipo = "plastic"
elif " can" in str(categories[top5_catid[0]])  or "can " in str(categories[top5_catid[0]]) or "hair spray" in str(categories[top5_catid[0]]):
    tipo = "metal"
elif "carton" in str(categories[top5_catid[0]]) or "box" in str(categories[top5_catid[0]]):
    tipo = "carton"
elif str(categories[top5_catid[0]]) in food:
    tipo = "organic"
else:
    for i in range(5):
        if "paper" in str(categories[top5_catid[i]]) or "tissue" in str(categories[top5_catid[i]]):
            tipo = "paper"
            break
        elif "beer" in str(categories[top5_catid[i]]) or "glass" in str(categories[top5_catid[i]]):
            tipo = "glass"
            break
        elif "plastic" in str(categories[top5_catid[i]]) or "bottle" in str(categories[top5_catid[i]]):
            tipo = "plastic"
            break
        elif " can" in str(categories[top5_catid[i]])  or "can " in str(categories[top5_catid[i]]) or "hair spray" in str(categories[top5_catid[0]]):
            tipo = "metal"
            break
        elif "carton" in str(categories[top5_catid[0]]) or "box" in str(categories[top5_catid[0]]):
            tipo = "carton"
        elif str(categories[top5_catid[0]]) in food:
            tipo = "organic"
        else:
            tipo = "trash"



# open image with title
import matplotlib.pyplot as plt
plt.imshow(input_image)
plt.title(tipo) #+" "+str(int(top5_prob[0].item()*100))+"%"
#Remove the ticks
plt.xticks([])
plt.yticks([])
plt.show()





