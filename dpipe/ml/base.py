import numpy as np
import sklearn as skl


def _print_regression_error(y_true, y_pred):
    print('Max error:', skl.metrics.max_error(y_true, y_pred))
    print('Mean absolute error:', skl.metrics.mean_absolute_error(y_true, y_pred))
    print('Mean squared error:', skl.metrics.mean_squared_error(y_true, y_pred))
    print('Root mean squared error:', np.sqrt(skl.metrics.mean_squared_error(y_true, y_pred)))


class _ModelSpec():
    def __init__(self, df):
        self.data = df
        self.original_data = df
        self.train = df
        self.X = self.data.iloc[:,:-1]
        self.y = self.data.iloc[:,-1]
        self.X_train = self.X.copy()
        self.y_train = self.y.copy()
        self.X_test = None
        self.y_test = None
        self.encoders = {}

    def train_test_split(self, X, y, **kwargs):
        self.X_train, self.X_test, self.y_train, self.y_test = skl.model_selection.train_test_split(X, y, **kwargs)
        return self.X_train, self.X_test, self.y_train, self.y_test

    def encode(self, Encoder, columns):
        enc_dict = {}
        for column in columns:
            enc = Encoder()
            self.data[column] = enc.fit_transform(self.data[column])
            enc_dict[column] = enc
        self.encoders.update(enc_dict)

        return encoded_df, enc_dict

    def instantiate_estimator(self, Estimator, **kwargs):
        self.estimator = Estimator(**kwargs)

    def predict(self):
        self.train_y_prediction = self.estimator.predict(self.X_train)
        if self.y_test is not None:
            self.test_y_prediction = self.estimator.predict(self.X_test)

    def evaluate(self, kind='regressor'):
        if kind=='regressor':
            if self.y_test is not None:
                print('\033[1mTraining set')
                print(len('Training set')*'-','\033[0m')
            _print_regression_error(self.y_train, self.train_y_prediction)
            print('\n')
            if self.y_test is not None:
                print('\033[1mTest set')
                print(len('Test set')*'-','\033[0m')
                _print_regression_error(self.y_test, self.test_y_prediction)
        elif kind=='classifier':
            if self.y_test is not None:
                # Plot roc auc curve.
                pass


