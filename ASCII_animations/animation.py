import os, time
os.system('clear')
filenames = []
frames = []

for x in range(0,156):
    if x < 10:
        x = str("00"+str(x))
    elif 9<x<100:
        x = str("0"+str(x))

    filenames.append(str(x)+".txt")


for name in filenames:
    with open(name,"r",encoding="utf8") as f:
        frames.append(f.readlines())


while True:
    for frame in frames:
        print("".join(frame)) 
        time.sleep(0.05)
        os.system("clear")
