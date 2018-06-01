import urllib.request

i=0
with open("imagenet_cats.txt") as f:
    for line in f:
        if line[0]=='h':
            i=str(i)
            try:
                urllib.request.urlretrieve(line, i+".jpg")
            except Exception as e:
                print(e)
            i=int(i)
            i=i+1
