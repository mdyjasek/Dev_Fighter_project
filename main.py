print("Relative Gravity for each planet for the fights")

print(" 1. Venus-0.91   2. Mars-0.38    3. Jupiter-2.34 ")
print(" 4. Saturn-1.06  5. Uranus-0.92  6. Neptune-1.19 ")
print(" ")
 
weight = int(input("What is your weight fighter?\n"))

planet = 3

# Write an if statement below:
jupiter_3 = 2.34
neptune_6 = 1.19
saturn_4 = 1.06
uranus_5 = 0.92
venus_1 = 0.91
mars_2 = 0.38

print(" Welcome to the big leagues Beautiful! ")
print(" ")

if weight >= jupiter_3 * weight:
  print("You can attend all fights!")
elif weight >= neptune_6 * weight:
  print("You can attend all fights exept planet 3")
elif weight >= saturn_4 * weight:
  print("You can attend all fights exept planets 3 & 6")
elif weight >= uranus_5 * weight:
  print("You can attend all fights exept planets 3,4 & 6")
elif weight >= venus_1 * weight:
  print("You can attend all fights exept planets 3-6")
elif weight >= mars_2 * weight:
  print("You can only attend mars_2")
else:
  print("Lose some weight THICC BOI, You are unable to attend all fights")

  #Hey this Devin, i add this line below
  hey_matt = "you suck"