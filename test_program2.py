mylist=list(input("Enter list   ").split(","))

out={}

for ele in mylist:
    out[ele]=out.get(ele,0)+1
    
for ele in out.keys():
    print(ele + " = "+ str(out[ele]))