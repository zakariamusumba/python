products = ("eggs","milk","bread")
def market(product):
	if product not in products:	
		print("we do not sell such items")
	else:
		print("we sell this item")