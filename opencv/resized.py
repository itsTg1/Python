import cv2

path="opencv\pyth.png"

image=cv2.imread(path)
cv2.imshow("python image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

resized=cv2.resize(image,(150,150))
cv2.imshow("python image",resized)
cv2.waitKey(0)
cv2.imwrite("resized.png",resized)