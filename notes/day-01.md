# Day 1 - Automatic Differentation

## What I Built

I built the beginning of a scalar automatic differentiation engine.

The Value object can currently track:

- Scalar values
- Addition
- Multiplication
- Parent operations
- Computational graphs
- Gradients
- Reverse-mode backpropagation

## What I Learned

A computational graph records how values were produced.

Backpropagation works backward through this graph using derivatives and the chain rule.

A gradient describes how changing one value affects the final output.

## Connection to Calculus

For:

c = ab

the derivatives are:

dc/da = b

dc/db = a

These derivative rules can be encoded into each mathematical operation, allowing the computer to automatically calculate gradients.

## Questions I Still Have

- Why is reverse-mode differentiation preferred for neural networks?
- How does the chain rule work through a large network?
- Why do neural networks need nonlinear activation functions?
- How does gradient descent use these gradients to actually learn?