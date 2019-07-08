alpha = 1000000000000
scaleFactor = (1-alpha) / (1 + alpha)

v1 = 0.0
v2 = -1.0

#print("Momentum = ", v1 + alpha*v2)

piCount = 0

while((v2 < v1) or (v1 < 0)):
  piCount += 1
  #print("Momentum = ", v1 + alpha*v2)
  #print("Energy * 2 = ", v1**2 + (v2**2)*alpha)
  if (v1 == 0):
    v2 = scaleFactor
    v1 = (v2 - 1)
    #print("Momentum = ", v1 + alpha*v2)
    # First hit
  elif (v1 < 0):
    v1 = - v1
    #print("New momentum = ", v1 + alpha*v2)
    # Ball hits wall
  else:
    # General case, small ball catches up
    v1, v2 = v1 - (v1 - v2)*((2*alpha) / (alpha + 1)), v1 - (v1-v2)*((alpha - 1) / (alpha + 1))
    #print("Momentum = ", v1 + alpha*v2)


print(piCount)
