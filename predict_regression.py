# Import Library
import numpy
import scipy
from sklearn import linear_model
# Load Train and Test datasets
# Identify feature and response variable(s) and values must be numeric and numpy arrays


#x_train = numpy.array([[1],[2],[8],[9],[11],[14],[16],[18],[22],[25],[26]])                   # input_variables_values_training_datasets
#y_train = numpy.array([[1],[5],[10],[4],[14],[9],[16],[11],[18],[15],[24]])                  # target_variables_values_training_datasets

x_train = [[26],[2],[4],[25],[7],[16],[9],[14],[11],[8],[18],[22],[6],[1]]
y_train = [[24],[5],[3],[15],[5],[16],[4],[9],[14],[10],[11],[18],[8],[1]]


x_test = numpy.array([[1],[2],[3]])                                   # input_variables_values_test_datasets


# x_train = x_train.reshape(1, -1)
# y_train = y_train.reshape(1, -1)
# x_test = x_test.reshape(1, -1)

# Create linear regression object
linear = linear_model.LinearRegression()
# Train the model using the training sets and check score
linear.fit(x_train, y_train)
linear.score(x_train, y_train)
# Equation coefficient and Intercept
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)
# Predict Output
predicted = linear.predict(x_test)
print("Predict your Future")
# seperator not working
print(predicted, sep=", ")