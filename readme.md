# Testing Project for ASPP 2023 Mexico

## Exercise 1 -- @parametrize and the logistic map

Make a file `logistic.py` and `test_logistic.py` in the same folder as this
readme and the `plot_logfun.py` file. Implement the code for the logistic map
in the `logistic.py` file:

a) Implement the logistic map f(𝑥)=𝑟∗𝑥∗(1−𝑥) . Import pytest and use
`@pytest.mark.parametrize` to test the function for the following cases:
```
  x=0.1, r=2.2 => f(x, r)=0.198
  x=0.2, r=3.4 => f(x, r)=0.544
  x=0.75, r=1.7 => f(x, r)=0.31875
```

b) Implement the function `iterate_f` that runs `f` for `it`
iterations, each time passing the result back into f.
Use `@pytest.mark.parametrize` to test the function for the following cases:
```
  x=0.1, r=2.2, it=1 => iterate_f(it, x, r)=[0.198]
  x=0.2, r=3.4, it=4 => iterate_f(it, x, r)=[0.544, 0.843418, 0.449019, 0.841163]
  x=0.75, r=1.7, it=2 => iterate_f(it, x, r)=[0.31875, 0.369152]
```

c) Import and call the `plot_trajectory` function from the `plot_logfun`
module to look at the trajectories generated by your code. The `plot_logfun`
imports and uses your `logistic.py` code. Import the module
and call the function in a new `plot_script.py` file.

Try with values `r<3`, `r>4` and `3<r<4` to get a feeling for how the function
behaves differently with different parameters. Note that your input x0 should
be between 0 and 1.

## Exercise 2 -- Check the convergence of an attractor using random testing
a) Write a randomized test that checks that, for `r=1.5`, all
starting points x0 converge to the same value (attractor) `f(x, r) = 1/3`.

b) Use `pytest.mark` to mark the tests from the previous exercise with one mark
(they relate to the correct implementation of the logistic map) and the
test from this exercise with another (relates to the behavior of the logistic
map). Try executing first the first set of tests and then the second set of
tests separately.

## Exercise 3 -- Chaotic behavior
Some r values for `3<r<4` have some interesting properties. A chaotic
trajectory doesn't diverge but also doesn't converge.

## Visualize the bifurcation diagram
a) Use the `plot_trajectory` function from the `plot_logfun` module using your
implementation of `f` and `iterate_f` to look at the bifurcation diagram.

The script generates an output image, `bifurcation_diagram.png`.

b) Write a test that checks for chaotic behavior when r=3.8. Run the
logistic map for 100000 iterations and verify the conditions for
chaotic behavior:

1) The function is deterministic: this does not need to be tested in
this case
2) Orbits must be bounded: check that all values are between 0 and 1
3) Orbits must be aperiodic: check that the last 1000 values are all
different
4) Sensitive dependence on initial conditions: this is the bonus
exercise below

The test should check conditions 2) and 3)!


## Bonus Exercise 4 -- The Butterfly Effect
For the same value of `r`, test the sensitive dependence on initial
conditions, a.k.a. the butterfly effect. Use the following definition of SDIC.

>`f` is a function and `x0` and `y0` are two possible seeds.
>If `f` has SDIC then:
>there is a number `delta` such that for any `x0` there is a `y0` that is not
>more than `init_error` away from `x0`, where the initial condition `y0` has
>the property that there is some integer n such that after n iterations, the
>orbit is more than `delta` away from the orbit of `x0`. That is
>|xn-yn| > delta

