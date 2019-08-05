# Simulation of some SPDEs


- We use a Galerkin approximation to simulate the stochastic heat equation with
  additive noise:
  \[ \partial_t u = \Delta u + \xi \]
  for space-time white noise \(\xi\).

- We simulate a sample path of the Brownian sheet

- We simulate to solutions <img src="/tex/b0084c5cb64e36b653b726facedd2f08.svg?invert_in_darkmode&sanitize=true" align=middle width=40.17511904999999pt height=22.831056599999986pt/> to the KPZ equation:
  \[\partial_t h_i =\Delta h_i + (\partial_x h_i)^2 + \xi \]
  for space time white noise <img src="/tex/85e60dfc14844168fd12baa5bfd2517d.svg?invert_in_darkmode&sanitize=true" align=middle width=7.94809454999999pt height=22.831056599999986pt/> and two initial conditions <img src="/tex/14149e7a18f6b1c55af4d61165f677e3.svg?invert_in_darkmode&sanitize=true" align=middle width=83.00631734999999pt height=24.65753399999998pt/>
  and we can observe that the solutions synchronize (see
  https://arxiv.org/abs/1907.06278).


