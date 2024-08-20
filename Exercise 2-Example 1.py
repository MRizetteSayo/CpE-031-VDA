import pandas

mydataset = {'animals': ["Cat","Dog","Rabbit"],
             'height': [13,17,8]
            }
myvar = pandas.DataFrame(mydataset)

print(myvar)