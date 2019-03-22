import numpy as np
import matplotlib.pyplot as plt
import itertools
import functools
np.random.seed(1234)

# Create training data and test data
def createSin(x):
    return np.sin(2 * np.pi * x)

def createTrainData(createSin, sample_size, std):
    x = np.linspace(0, 1, sample_size)
    t = createSin(x) + np.random.normal(scale = std, size = x.shape)
    return x, t

x_train, y_train = createTrainData(createSin, 11, 0.25)
x_test = np.linspace(0, 1, 100)
y_test = createSin(x_test)

# compute X
def createX(x, degree):
    x_t = x.transpose()
    X = [np.ones(len(x))]
    for i in range(degree):
        for items in itertools.combinations_with_replacement(x_t, i):
            X.append(functools.reduce(lambda x, y: x*y, items ))
    return np.asarray(X).transpose()

degree = 9
X_train = createX(x_train, degree)
X_test = createX(x_test, degree)

# solve equation, return w
def solve(X, t, learnrate):
    return np.linalg.solve(learnrate * np.eye(np.size(X, 1)) + X.T @ X, X.T @ t)
    
# predict, return t
def predict(X, w):
    return X @ w

learnrate = 1e-3
w = solve(X_train, y_train, learnrate)
y = predict(X_test, w)

# plot
plt.scatter(x_train, y_train, facecolor="none", edgecolor="b", s=50, label="training data")
plt.plot(x_test, y_test, c="g", label="$\sin(2\pi x)$")
plt.plot(x_test, y, c="r", label="fitting")
plt.ylim(-1.5, 1.5)
plt.legend()
plt.annotate("M=9", xy=(-0.15, 1))
plt.show()