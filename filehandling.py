#1. creating a txt file
def create(name):
    try:
        with open(name,"x")as c:
            print(c)
    except Exception as e:
        print(e)

# create("cars.txt")

# 2. writing a  text file 
def write(name,cont):
    with open(name,"w") as w:
        w.write(cont)
        
write("cars.txt","BMW")


