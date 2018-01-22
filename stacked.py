import matplotlib.pyplot as plt

A = [5., 30., 45., 22.]
B = [5., 25., 50., 20.]

X = range(4)

plt.bar(X, A, color = (7,105,79)/255) #provide color as a tuple with RGB values - this is green
plt.bar(X, B, color = (221,147,58)/255, bottom = A) # orange color
plt.show()
