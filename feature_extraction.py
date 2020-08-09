# USAGE
# python image_diff.py --first images/original_01.png --second images/modified_01.png

# import the necessary packages
from skimage import metrics
import imutils
import cv2

def process(obj1,obj2,threshold_frame):
    # load the two input images
    imageA = cv2.imread("Input Frame/{}.jpg".format(obj1.enter_frame+threshold_frame))
    imageB = cv2.imread("Input Frame/{}.jpg".format(obj2.enter_frame+threshold_frame))
    
    print("{}    {}".format(obj1.enter_frame+threshold_frame,obj2.enter_frame+threshold_frame))
    # convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    
    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = metrics.structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("\n\nSSIM Feature: {}".format(score))
    
    if(score>=0.55):
        # threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh = cv2.threshold(diff, 0, 255,
        	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        	cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        
        # loop over the contours
        for c in cnts:
        	# compute the bounding box of the contour and then draw the
        	# bounding box on both input images to represent where the two
        	# images differ
        	(x, y, w, h) = cv2.boundingRect(c)
        	cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
        	cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
        return score
    else:
        return 0
    