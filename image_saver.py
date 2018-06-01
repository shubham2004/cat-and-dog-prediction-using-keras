# importing urllib.request library
import urllib.request

i=0
#opening file of url list downloaded by imagenet
with open("imagenet_cats.txt") as f:
# reading file
    for line in f:
        if line[0]=='h':
            i=str(i)
            #i use try because many urls are either defective or are not present now so it will skip those urls
            try:
                #opening and saving image in the current folder as integer names
                urllib.request.urlretrieve(line, i+".jpg")
            except Exception as e:
                print(e)
            i=int(i)
            i=i+1
