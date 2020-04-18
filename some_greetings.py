#introductory lines
print ("This is a program to say your Greetings")
greeting= input("would you like to say [Hello][Y] or [somethig else][N]?")

#logic coding with nesting
if greeting.isdigit():
    print ("This answer is a Number. Please answer correctly under the parameters in your next try.")
    print ("Thanks (>.<)")
elif greeting.isalpha():
    if greeting.lower() == "something else" or greeting.lower() == "n":
        print ("you have entered 'Something Else'")
        greeting_1 = input ("Write the custom greeting you would like to send: ")
        send_to = input ("write the name of the person you want to send this greeting: ")
        print ("")
        print ("-------------------------------------------------------")
        print ("            " + greeting_1 , send_to)
        print ("-------------------------------------------------------")
        print ("")
        print ("END")
    elif greeting.lower() == "hello" or greeting.lower() == "y":
        print ("you have entered 'Hello'")
        greeting_2 = input ("would you like to send a [Full Hello][Y] or [Hi][N]")
        if greeting_2.lower() == "hi" or greeting_2.lower() == "n":
            greeting_3 = "Hi"
            print ("")
            print ("you have entered 'Hi'")
            print ("-------------------------------------------------------")
            print ("                " + greeting_3)
            print ("-------------------------------------------------------")
            print ("")
            print ("END")
        else:
            print ("you have entered 'Full Hello'")
            greeting_4 = "Hello"
            print ("")
            print ("-------------------------------------------------------")
            print ("                 " + greeting_4)
            print ("-------------------------------------------------------")
            print ("")
            print ("END")
else:
    print ("")
    print ("I don't know what you are writing but please try to use English or Spanish!")
    print ("Try responding with one of the options offered")
    print ("Try Again")
    
