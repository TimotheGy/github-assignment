"""Assignment - making a sklearn estimator.

The goal of this assignment is to implement by yourself a scikit-learn
estimator for the OneNearestNeighbor and check that it is working properly.

The nearest neighbor classifier predicts for a point X_i the target y_k of
the training sample X_k which is the closest to X_i. We measure proximity with
the Euclidean distance. The model will be evaluated with the accuracy (average
number of samples corectly classified). You need to implement the `fit`,
`predict` and `score` methods for this class. The code you write should pass
the test we implemented. You can run the tests by calling at the root of the
repo `pytest test_sklearn_questions.py`.

We also ask to respect the pep8 convention: https://pep8.org. This will be
enforced with `flake8`. You can check that there is no flake8 errors by
calling `flake8` at the root of the repo.

Finally, you need to write docstring similar to the one in `numpy_questions`
for the methods you code and for the class. The docstring will be checked using
`pydocstyle` that you can also call at the root of the repo.
"""
import numpy as np
from sklearn.base import BaseEstimator
from sklearn.base import ClassifierMixin
from sklearn.utils.validation import check_X_y
from sklearn.utils.validation import check_array
from sklearn.utils.validation import check_is_fitted
from sklearn.utils.multiclass import check_classification_targets
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics import accuracy_score


class OneNearestNeighbor(BaseEstimator, ClassifierMixin):
    """OneNearestNeighbor classifier."""

    def __init__(self):  # noqa: D107
        pass

    def fit(self, X, y):
        """Prepare the data to be used for classification.

        Parameters
        ----------
        X: Training array where each row is a sample and each column is
        a feature
        y: Vector containing the target feature (y has as many rows as X)

        Returns
        -------
        The "fit" step is training the data we have and makes
        them ready to be used for our prediction
        """
        X, y = check_X_y(X, y)
        check_classification_targets(y)
        self.classes_ = np.unique(y)
        self.X_ = X
        self.y_ = y
        self.n_features_in_ = X.shape[1]

        return self

    def predict(self, X):
        """From a given array, return the vector of predictions.

        Parameters
        ----------
        X: Array containing the data for which we want to approximate
        the target

        Returns
        -------
        y_pred: The vector containing the y_k of the training sample which
        are the closest to the points of X
        """
        check_is_fitted(self)
        X = check_array(X)
        y_pred = np.full(
            shape=len(X), fill_value=self.classes_[0],
            dtype=self.classes_.dtype
        )

        distances = euclidean_distances(X, self.X_)

        """Distances contains the distances between the row vectors
        of X and the row vectors of our training array.
        """

        nearest_neighbor_indices = np.argmin(distances, axis=1)

        y_pred = self.y_[nearest_neighbor_indices]

        return y_pred

    def score(self, X, y):
        """Return the accuracy of our prediction.

        Parameters
        ----------
        X: Array containing the data for which we want to approximate
        the target
        y: Vector containing the target feature for our training data

        Returns
        -------
        The proportion of points that were correctly predicted/classified
        """
        X, y = check_X_y(X, y)
        y_pred = self.predict(X)

        return accuracy_score(y_pred, y)
