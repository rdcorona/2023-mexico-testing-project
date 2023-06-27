from plot_logfun  import plot_trajectory

rs = [2.2, 2.9, 3.1, 3.6, 4.0, 4.4]

for r in rs:
  plot_trajectory(100, r, 0.7, fname=f"single_trajectory_{r}.png")
