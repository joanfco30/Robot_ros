import cv2

path = r'imagen2.bmp'

  
# Reading an image in default mode
image = cv2.imread(path)
original = image.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,5),3)

#cv2.imshow('bm1p',blur)



thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cnts = cnts[0] if len(cnts) == 2 else cnts[1]
print(cnts)

#cv2.imshow('bmp',thresh)
#cv2.waitKey(0) 
  
#closing all open windows 
cv2.destroyAllWindows()