def f(x,r):
  return r*x*(1-x)

def iterate_f(it, x, r):
    from numpy import array
    out = []
    for i in range(it):
        out.append(f(x, r))
        x = out[i]
    return array(out)


if __name__ == '__main__':
    print(iterate_f(4,0.2,3.4))
