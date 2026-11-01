f = open("mailbox.txt", "r")
fout=open("output.txt", "w")
lines=f.readlines()
domains=[]
for line in lines:
   if "From:" in line:
       email=line.strip().split()[1]
       d=email.split("@")[1].split('>')[0]
       if d not in domains:
           domains.append(d)
sd=sorted(domains)
for d in sd:
    fout.write(d+"\n")
f.close()
fout.close()