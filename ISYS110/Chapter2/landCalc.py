#var to hold area of land
landArea = 0.00
feetinAcre = 43560

#var to hold total acres
totalAcres= 0.00

landArea= float(input("Enter the total area of land in square feet: "))

#calculate / conver the acres

totalAcres = landArea/feetinAcre

print(f"The user entered {landArea} square feet. Which is {totalAcres} acres.")