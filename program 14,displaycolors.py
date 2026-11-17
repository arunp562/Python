text = input("enter colors seperated by commas")

colors = text.split(',')

colors = [color.strip() for color in colors]

print("forst color ",colors[0])

print("last color :", colors[-1])
