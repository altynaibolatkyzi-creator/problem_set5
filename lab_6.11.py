f = open("mailbox.txt", "r")
fout=open("output.txt", "w")
lines=f.readlines()
a=[]
for line in lines:
    if "(Cyrus " in line:
        v=line.split("(Cyrus ")[1].split(")")[0]
        if v not in a:
            a.append(v)
a.sort()
for v in a:
    fout.write(v+"\n")
f.close()
fout.close()