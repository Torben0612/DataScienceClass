#Start code here
import random

jury_pool_population = []
probabilities_population = [67, 806, 1, 43, 2, 81]
black_jurrors_population = []
white_jurrors_population = []
pacific_islander_jurrors_population = []
asian_jurrors_population = []
native_american_jurrors_population = []
other_jurrors_population = []



for i in range(probabilities_population[0]):
  jury_pool_population.append("Black")

for i in range(probabilities_population[1]):
  jury_pool_population.append("White")

for i in range(probabilities_population[2]):
  jury_pool_population.append("Pacific Islander")

for i in range(probabilities_population[3]):
  jury_pool_population.append("Asian")

for i in range(probabilities_population[4]):
  jury_pool_population.append("Native American")

for i in range(probabilities_population[5]):
  jury_pool_population.append("Other")

print("Here is the jury pool based on the overall community demographics:")
print(jury_pool_population)
print("")

for j in range(200):
  jury = []
  black_counter = 0
  white_counter = 0
  pacific_counter = 0
  asian_counter = 0
  native_counter = 0
  other_counter = 0
  for k in range(12):
    juror = random.choice(jury_pool_population)
    jury.append(juror)
    if juror == "White":
      white_counter += 1
    elif juror == "Black":
      black_counter += 1
    elif juror == "Pacific Islander":
      pacific_counter += 1
    elif juror == "Asian":
      asian_counter += 1
    elif juror == "Native":
      native_counter += 1
    elif juror == "Other":
      other_counter += 1
  print("Here is jury " + str(j + 1) + " :")
  print(jury)
  white_jurrors_population.append(white_counter)
  black_jurrors_population.append(black_counter)
  pacific_islander_jurrors_population.append(pacific_counter)
  asian_jurrors_population.append(asian_counter)
  native_american_jurrors_population.append(native_counter)
  other_jurrors_population.append(other_counter)
print("")
print("Here is the count of jurors based on demographic on each jury using the actual community demographics:")
print("white: " + str(white_jurrors_population))
print("Black: " + str(black_jurrors_population))
print("Pacific Islander: " + str(pacific_islander_jurrors_population))
print("Asian: " + str(asian_jurrors_population))
print("NativeL " + str(native_american_jurrors_population))
print("Other: " + str(other_jurrors_population))
print("")
