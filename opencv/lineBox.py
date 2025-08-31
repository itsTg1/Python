import cv2

path="opencv\pyth.png"

image=cv2.imread(path)
cv2.imshow("python image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.line(image,(400,300),(800,300),(255,0,0),9)
cv2.imshow("python image",image)
cv2.waitKey(0)

cv2.rectangle(image,(100,100),(900,600),(0,255,0),5)
cv2.imshow("python image",image)
cv2.waitKey(0)

# if thickness is -1 then it is a fill 
# cv2.circle(image_name,centre(x,y),radius,color,thickness)

# putText(image,text,org(leftbottom corner(x,y)),font type,font scale , color,thickness)