# Unsupervised Learning



- Feature: An input variable used in making predictions.
- Predictions: A model’s output when provided with an input example.
- Example: One row of a data set. An example contains one or more features and possibly a label.
- Label: Result of the feature

## Models

- Clustering
  - K-means Clustering
  - Hierarchical Clustering

## Algorithms


## Linear Regression

### Use Cases

## K-means Clustering

## Hierarchical Clustering

Algorithm builds a hierarchy of clusters beginning with all the data assigned to a cluster of their own. Then two closest clusters are joined into the same cluster. In the end, this algorithm ends when there is only a single cluster left. The completion of hierarchical clustering can be shown using dendrogram.

time complexity is quadratic i.e. O(n^2)

## t-SNE Clustering (t-distributed Stochastic Neighbor Embedding)

It maps high dimensional space into a 2 or 3 dimensional space which can be visualised. Specifically, it models each high-dimensional object by a two- or three-dimensional point in such a way that similar objects are modeled by nearby points and dissimilar objects are modeled by distant points with high probability.

## DBSCAN Clustering (Density-Based Spatial Clustering of Applications with Noise)

used as an replacement to K-means in predictive analytics. It doesn’t require that you input the number of clusters in order to run. But in exchange, you have to tune two other parameters.
