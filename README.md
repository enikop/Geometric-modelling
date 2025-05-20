# Geometric modelling coursework and assignment
**Name:** Palencsár Enikő \
**Neptune:** YD11NL \
**Semester:** 2024/25/II

## Coursework
* JavaScript 2D curve implementations:
    * Lagrange interpolation
    * de Casteljau algorithm with a slider to set parameter (resulting Bezier curve traced)
    * NURBS approximation
* Python surface implementation:
    * visualize a given surface and its normal vector
    * calculations by hand for the same surface and its tangent plane

## Assignment - Learnable activation functions in MLPs
Investigation of different approximation and interpolation curves as activation functions in MLPs.

### Plan
* Implement B-spline activation function
* Implement NURBS activation function
* Implement interpolation curve-based activation functions (Lagrange, Catmull-Rom and other Hermite splines etc.)
* Visualize activations
* Compare these learnable alternatives to ReLU:
    * training time
    * loss, accuracy
    * number of parameters
    * minimal network structure needed for the NN to perform well
* Compare these learnable activation functions to each other
* Investigate the role of weights on edges
    * hypothesis: they are necessary

## Progress
- [x] B-spline activation layer
- [x] NURBS activation layer
- [x] Lagrange activation layer
- [ ] Catmull-Rom or Overhauser spline activation layer
- [x] Visualizations
- [x] Simple example approximating a sine function, without weights in linear layers
- [x] Simple experiment with a few features ([Graduate Admissions dataset](https://www.kaggle.com/datasets/mohansacharya/graduate-admissions))
- [ ] Complex experiment (on MNIST?) with measurements recorded for all learnable activations + ReLU

## Other interesting things to see
* Is NURBS activation more effective in separating circularly separable 2D points (concentric circles) than B-spline?
    * guess: not necessarily
* Are spline activations more effective in separating circularly separable 2D points (concentric circles) than ReLU?
    * guess: they must be - Is the time penalty worth it?

## Result summary
* [Report on the results](/assignment/README.md)
* [Experiments with same curve parameters per layer](/assignment/Learnable_activation_functions_per_layer.ipynb)
* [Experiments with different curves on each neuron](/assignment/Learnable_activation_functions_per_neuron.ipynb)
* [Failed attempt at creating a Catmull-Rom activation function](/assignment/The_big_catmull_rom_failure.ipynb) (Abandoned for now, will try again later)