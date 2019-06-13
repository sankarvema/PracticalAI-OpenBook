# Recommendation Engine

Categorized as
- Content-based Methods
  - Uses attributes based of items / users
  - Recommend items based on past profile or history
- Collaborative Filtering Methods
  - Recommend items liked to similar users
  - Enable exploration of diverse content


## Algorithms

### User based k-Nearest Neighbours

- Compute similarity of the users
- Find k users most similar to user a
- Recommend items not picked user a in the past

The simplest algorithm computes cosine or correlation similarity of rows (users) or columns (items) and recommends items that k — nearest neighbors enjoyed.

### Matrix Factorization

Matrix factorization based methods attempt to reduce dimensionality of the interaction matrix and approximate it by two or more small matrices with k latent components.

### Association rules

Association rules can also be used for recommendation. Items that are frequently consumed together are connected with an edge in the graph. You can see clusters of best sellers (densely connected items that almost everybody interacted with) and small separated clusters of niche content.

### Deep Neural Networks


## Reference:

https://medium.com/recombee-blog/machine-learning-for-recommender-systems-part-1-algorithms-evaluation-and-cold-start-6f696683d0ed
