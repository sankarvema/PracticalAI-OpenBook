# Feature

A feature is a piece of information in an image that is relevant to solving a certain problem. It could be something as simple as a single pixel value, or more complex like edges, corners, and shapes. You can combine multiple simple features into a complex feature.

# Cascade

In machine learning (especially computer vision), identifying a feature could be a series of tasks which look for and analyze a pattern to identify the feature. These tasks are like waterfall to be done one after another based on the outcome of a given (current) task.

For example, OpenCV face recognition cascade breaks the problem of detecting faces into multiple stages. For each block, it does a very rough and quick test. If that passes, it does a slightly more detailed test, and so on. The algorithm may have 30 to 50 of these stages or cascades, and it will only detect a face if all stages pass.
