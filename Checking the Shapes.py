# removing the target column Revenue from dataset and assigning to X
X = dataset.drop(['Revenue'], axis = 1)
# assigning the target column Revenue to y
Y = dataset['Revenue']
# checking the shapes
print("Shape of X:", X.shape)
print("Shape of Y:", Y.shape)