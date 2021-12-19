
import matplotlib.pyplot as plt

def calcSusceptible(a, b, S, I):
	return S - a*I*S
	
def calcInfected(a, b, S, I):
	return I + a*I*S - b*I
	
def calcRecovered(b, R, I):
	return R + b*I

a, b = 0.7, 0.2 #a is contact rate (prob of catching the disease) and b is rate of recovery
S, I, R = [0.99], [0.01], [0.00]
t = list(range(0, 50))

for i in t:
	S.append(calcSusceptible(a, b, S[i], I[i]))
	I.append(calcInfected(a, b, S[i], I[i]))
	R.append(calcRecovered(b, R[i], I[i]))

t.append(50)

plt.plot(t, S, label = 'Susceptible')
plt.plot(t, I, color = 'r', label = 'Infected')
plt.plot(t, R, color = 'k', label = 'Recovered')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Percentage of people')
plt.title('a = ' + str(a) + ', b = ' + str(b))
plt.show()
