#!/usr/bin/env python

from skimage.exposure import histogram
import math

def image_entropy(img):
	''' Calculate the entropy of an image
	
	Parameters
	----------
	img must be in the form of a ndarray
	
	Returns
	-------
	value of the image entropy (float)
	
	'''
	histo,bins=histogram(img, nbins=255)
	histogram_length = sum(histo)
	
	samples_probability = [float(h) / histogram_length for h in histo]
	entropy = -sum([p * math.log(p, 2) for p in samples_probability if p != 0])
	return entropy



def entropy_crop(img, targetWidth, targetHeight, maxSteps=10):
	''' Return the best starting point for a crop based on a target width an target height.
	Image is not resized so, a small crop size with a big original image could lead to weird (not optimal) results
	
	Parameters
	----------
	TargetWidth, targetHeight : dimensions of the cropped image
	MaxSteps : maximum number of iteration. More iteration means more precision but less speed (default=10)
	
	'''
	originalHeight, originalWidth = img.shape
	rightX = originalWidth
	bottomY = originalHeight
	topY = 0 # offset value from image top to estimate
	leftX = 0 # offset value from image top to estimate*
	
	sliceSize = int(round((originalWidth - targetWidth) / maxSteps)) #calculate slice size based on max steps
	if sliceSize == 0 :
		sliceSize = 1

	leftSlice = None
	rightSlice = None


	# cut left or right slice of image based on min entropy value until targetwidth is reached
	while ((rightX - leftX - sliceSize) > targetWidth): # while there still are uninvestigated slices of the image (left and right)
		
		if (leftSlice == None):
			leftSlice = img[0:originalHeight+1,leftX:leftX+sliceSize+1]
		
		if (rightSlice == None):
			rightSlice = img[0:originalHeight+1, rightX - sliceSize:rightX+1]
		
		if (image_entropy(leftSlice) < image_entropy(rightSlice)):
			leftX = leftX + sliceSize
			leftSlice = None
		else:
			rightX = rightX - sliceSize
			rightSlice = None
		

	topSlice = None
	bottomSlice = None

	sliceSize = int(round((originalHeight - targetHeight)/maxSteps)) #calculate slice size based on max steps
	if sliceSize == 0 :
		sliceSize = 1

	# cut upper or bottom slice of image based on min entropy value until targetheight is reached	
	while ((bottomY - topY - sliceSize) > targetHeight): # while there still are uninvestigated slices of the image (top and bottom)
		if (topSlice == None):
			topSlice = img[topY:topY+sliceSize+1, 0:originalWidth+1]
		
		if (bottomSlice == None):
			bottomSlice = img[bottomY - sliceSize:bottomY+1, 0:originalWidth+1]	
		
		if (image_entropy(topSlice) < image_entropy(bottomSlice)):
			topY = topY + sliceSize
			topSlice = None
		else:
			bottomY = bottomY - sliceSize
			bottomSlice = None

	return(leftX, topY)
