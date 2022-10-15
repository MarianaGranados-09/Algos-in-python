import matplotlib.pyplot as plt

def ball_trayectory(x):
    location = 10*x-5*(x**2)
    return(location)

#Plotting a hypothetical ball trayectory between the moment it is thrown at x = 0 and when it hits the ground again at x = 2
xs = [x/100 for x in list(range(201))]
ys = [ball_trayectory(x) for x in xs]
plt.plot(xs,ys)
plt.title('The Trayectory of a Thrown Ball')
plt.ylabel('Vertical Position of Ball')
plt.axhline(y = 0)
plt.show()
