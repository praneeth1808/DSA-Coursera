

s = "GAGAGAGA$"
array_suffix = []
for i in range(len(s)):
    testString=s*2
    array_suffix.append(testString[i:i+4])


partial = sorted(array_suffix)
print(partial)
classes={}
FinalArray_class = []
count=-1
for i in partial:
    keys=classes.keys()
    found = 0
    for key in keys:
        if key == i:
            FinalArray_class.append(classes[key])
            found=1
    if(found==0):
        count +=1
        FinalArray_class.append(count)
        classes[i] = count

print(FinalArray_class)
