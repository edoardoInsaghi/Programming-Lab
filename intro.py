file=open("shampoo_sales.csv", "r")
total_values=[]
sum=0

for line in file:
    elements=line.split(",")

    if elements[0] != "Date":
        date=elements[0]
        value=elements[1]

        sum+=float(value)

        total_values.append(float(value))


print(round(sum,1))        

