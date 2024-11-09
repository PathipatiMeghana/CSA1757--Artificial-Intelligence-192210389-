class DecisionTree:
    def __init__(self):
        self.tree = None

    def fit(self, X, y):
        self.tree = self._build_tree(X, y)

    def _build_tree(self, X, y):
        if len(set(y)) == 1:  
            return y[0]
        
        best_split = self._find_best_split(X, y)
        if not best_split:
            return max(set(y), key=y.count) 

        left_X, left_y, right_X, right_y = best_split
        left_tree = self._build_tree(left_X, left_y)
        right_tree = self._build_tree(right_X, right_y)

        return {"left": left_tree, "right": right_tree}

    def _find_best_split(self, X, y):
       
        for i in range(len(X[0])):  
            left = [y[j] for j in range(len(X)) if X[j][i] == 0]
            right = [y[j] for j in range(len(X)) if X[j][i] == 1]
            if left and right:
                return X[:len(left)], left, X[len(left):], right
        return None

    def predict(self, X):
        return [self._predict_sample(self.tree, sample) for sample in X]

    def _predict_sample(self, tree, sample):
        if type(tree) != dict:  
            return tree
        if sample[0] == 0:
            return self._predict_sample(tree["left"], sample[1:])
        else:
            return self._predict_sample(tree["right"], sample[1:])


X = [[0, 0], [0, 1], [1, 0], [1, 1]]  
y = [0, 0, 1, 1]  
dt = DecisionTree()
dt.fit(X, y)
print(dt.predict([[0, 1], [1, 0]])) 