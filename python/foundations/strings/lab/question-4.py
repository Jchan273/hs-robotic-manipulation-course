def rect(width, length):
	"""
	Create a rectangle made of "#" with the dimensions width by length.
	
	>>> rect(4, 1)
	####

	>>> rect(6, 3)
	######
	######
	######
	"""
	for x in range(length):
		print("#"*width)
rect(4,1)
rect(6,3)
