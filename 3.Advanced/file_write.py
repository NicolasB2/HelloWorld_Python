#Write all txt
f=open("../sources/write.txt","w")
f.write("first example\nof write file\n")
f.close()

#Add line in txt file
f = open ("../sources/write.txt", "a")
f.write("by Nicolas\n")
f.write("05/04/2019\n")
f.write("icesi university")
f.close()
