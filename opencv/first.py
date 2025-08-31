import cv2
path="opencv\pyth.png"
image=cv2.imread(path)
cv2.imshow("pyth",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

height,width,channel=image.shape
print(f"{height},{width},{channel}")
img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("pyth",img)
cv2.waitKey(0)
cv2.destroyAllWindows()