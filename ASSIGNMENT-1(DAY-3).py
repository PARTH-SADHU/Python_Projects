# ASSIGNMENT-1(DAY-3)

# QUE-You all are pilots,you have to land a plane,the altitude req to land a plane is 1000fts , if it is less
# than that tell pilot to land the plane , or it is more than that but lesss than 5000ft ask the pilot to come
# down to 1000ft ,else if it is more than 5000ft ask the pilot to go around and try later.



altitude=int(input("enter the altitude you want"))
if altitude<=1000:
    print("there's a green signal pilot you can land safely")

elif 1000<altitude<=5000:
     print("you are at high altitude you have to come down till 1000fts ")

else:
    print("its not possible at the moment please try later")
