#User input the size
buyer_size = input ("Enter The size of the Item you want [S, SS, , SM, M, L, XL]: ")

#defining the available sizes
av_sizes = "S, SS, , SM, M, L, XL"

#def the formula for the search engine
def item_search (size):
    if size.isdigit(): 
        print ("We do not have sizes in digits. But: [", av_sizes, "]")
        print ("Please try again")
    elif size.lower() == "s":
        print ("Small = $6")
    elif size.lower() == "ss": 
        print ("Super Small = $4")
    elif size.lower() == "sm":
        print ("Small Medium = 6.7")
    elif size.lower() == "m":
        print ("Medium = $7")
    elif size.lower() == "l":
        print ("Large = 8")
    elif size.lower() == "xl":
        print ("Extra Large = 10")
    else: 
        print ("We currently don't carry Size "+size+". Would you like to place a Special order?")
        
#calling the funtion
item_search (buyer_size)
