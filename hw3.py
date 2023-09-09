with open(file='buoi 3\Iris.csv', mode='r') as file_csv:
    data = file_csv.readlines()
file_csv.close()

for row in data[1:]:
    #print(row)  (string)
    
    text = str(row).split(sep=",") # change the value to string then split it. The data will be in list
    #print(text)
    sepalLength = text[1]
    sepalWidth = text[2]

# Iris Setosa - Average value of sepal Length and sepal Width
count = 0
totalLength = 0
totalWidth = 0
maxLength = 0
maxWidth = 0

for row in data[1:51]: 
    
    text = str(row).split(sep=",") # change the value to string then split it. The data will be in list
    totalLength += float(text[1])   # added the sepal length value
    totalWidth += float(text[2])     # added the sepal width value
    count+=1                            # count the number of Iris Setosa
    # FIND THE MAX VALUE OF SEPAL LENGTH AND SEPAL WIDTH
    if maxLength < float(text[1]) :
        maxLength = float(text[1]) 
    if maxWidth < float(text[2]):
        maxWidth = float(text[2])
aveLength = totalLength/count           # find the average length value
aveWidth = totalWidth/count
print("The average length value of Iris-setosa is: ")
print('{:.2f}'.format(aveLength))
print("The average width value of Iris-setosa is: ")
print('{:.2f}'.format(aveWidth))
print("The max length value of Iris-setosa: ", maxLength)
print("The max width value of Iris-setosa is: ", maxWidth)

# Iris-versicolor - Average value of sepal Length and sepal Width
count = 0
totalLength = 0
totalWidth = 0
maxLength = 0
maxWidth = 0
for row in data[51:101]:
    text = str(row).split(sep=',')
    totalLength += float(text[1])
    totalWidth += float(text[2])
    count += 1
    # FIND THE MAX VALUE OF SEPAL LENGTH AND SEPAL WIDTH
    if maxLength < float(text[1]):
        maxLength = float(text[1]) 
    if maxWidth < float(text[2]):
        maxWidth = float(text[2])
aveLength = totalLength/count
aveWidth = totalWidth/count
print("The average length value of Iris-versicolor is: ")
print('{:.2f}'.format(aveLength))
print("The average width value of Iris-versicolor is: ")
print('{:.2f}'.format(aveWidth))
print("The max length value of Iris-versicolor: ", maxLength)
print("The max width value of Iris-versicolor is: ", maxWidth)
    
# Iris-virginica - Average value of sepal Length and sepal Width
count = 0
totalLength = 0
totalWidth = 0
maxLength = 0
maxWidth = 0

for row in data[101:]:
    text = str(row).split(sep=',')
    totalLength += float(text[1])
    totalWidth += float(text[2])
    count += 1
    # FIND THE MAX VALUE OF SEPAL LENGTH AND SEPAL WIDTH
    if maxLength < float(text[1]):
        maxLength = float(text[1]) 
    if maxWidth < float(text[2]):
        maxWidth = float(text[2])

aveLength = totalLength/count
aveWidth = totalWidth/count
print("The average length value of Iris-virginica is: ")
print('{:.2f}'.format(aveLength))
print("The average width value of Iris-virginica is: ")
print('{:.2f}'.format(aveWidth))
print("The max length value of Iris-virginica: ", maxLength)
print("The max width value of Iris-virginica is: ", maxWidth)

