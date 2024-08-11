import cv2
import matplotlib.pyplot as plt

image = cv2.imread('C:\\Users\\G_BOOTS\\Desktop\\PROJECTS\\ff\\images\\001.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
plt.imshow(image)
plt.show()

