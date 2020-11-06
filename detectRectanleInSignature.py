import cv2
import fitz


# PDF Reader "PyPDF2"
# PDF converter
pdffile = "sqPDF.pdf"
doc = fitz.open(pdffile)
page = doc.loadPage(0)
pix = page.getPixmap()
output = "output.png"
pix.writePNG(output)

# Get the png file from pdf
img=cv2.imread('output.png')

# Preparation
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
canny = cv2.Canny(blur,10,50)
cv2.imwrite("gray.png", gray)
cv2.imwrite("blur.png", blur)
cv2.imwrite("canny.png", canny)

#Find contours
contours = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)[0]

#Loop through contours to find rectangles and put them in a list
cntrRect = []
for i in contours:
        approx = cv2.approxPolyDP(i,0.01*cv2.arcLength(i,True),True)
        # Rectangle
        if len(approx) == 4:
            print(cv2.contourArea(i))
            if (cv2.contourArea(i) < 6000):
                cv2.drawContours(img,cntrRect,-1,(0,255,0),2)
                cv2.imshow('Roi Rect ONLY',img)
                cntrRect.append(approx)


cv2.imwrite("result.png", img)
