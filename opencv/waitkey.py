# if no key pressed image will close after 6 seconds
# if key pressed then immediately image will close

import cv2
path="opencv\pyth.png"
image=cv2.imread(path)
cv2.imshow("our-image",image)

key=cv2.waitKey(6000)

if key!=-1:
    print("key pressed")
    cv2.destroyAllWindows()
else:
    print("no key pressed")

# if we add two lines these then it will wait indefinitely after 6s of wait 
cv2.waitKey(0)
cv2.destroyAllWindows()