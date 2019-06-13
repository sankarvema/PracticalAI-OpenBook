

# Viola-Jones Object Detection Framework

The Viola-Jones algorithm has 4 main steps, and you’ll learn more about each of them in the sections that follow:

1. Selecting Haar-like features
- Creating an integral image
- Running AdaBoost training
- Creating classifier cascades
Given an image, the algorithm looks at many smaller subregions and tries to find a face by looking for specific features in each subregion. It needs to check many different positions and scales because an image can contain many faces of various sizes. Viola and Jones used Haar-like features to detect faces.
