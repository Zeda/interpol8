import sys

def ncr(x,y):
  # compute x!/(y!*(x-y)!)
  z = 1
  if x < y:
    return 0
  elif x == y:
    return 1
  elif x>y+y:
    y = x-y

  k = 0
  while y<x:
    k += 1
    y += 1
    z *= y
    z /= k

  return z

def interp(f,x=[]):
  k = 1
  fact = 1
  poly = [0]*len(f)
  y = poly[0:]
  poly[0]=1
  y[0] = f[0]
  while k < len(f):
    i = k
    acc = 0
    s = 1
    while i>=0:
      acc += s*ncr(k,i)*f[i]
      s = -s
      i -= 1

    # generate the new polynomial
    # multiply by (x-k+1)
    i = k
    while i>0:
      poly[i] = poly[i-1]-poly[i]*(k-1)
      i -= 1
    poly[0] = 0

    #now add acc*poly/fact to y
    acc = acc*1.0/fact
    while i<=k:
      y[i] += acc*poly[i]
      i += 1

    k += 1
    fact *= k

  return y

def cf(x):
  c = []
  i = 0
  while i<20 and abs(x-int(x))>1e-8:
    y = int(x)
    c += [y]
    x -= y
    x = 1.0/x
    i += 1
  return c + [int(x)]

def gcd(n,m):
  e = 1
  while ((n|m)&1)==0:
    n >>= 1
    m >>= 1
    e <<= 1


  # make sure that n is the even one, if either are even
  if (m&1)==0:
    n,m = m,n

  while n != 0:
    #remove all factors of 2 from n
    while (n&1)==0:
      n >>= 1

    #now n and m are odd
    #make sure m is the smaller of the two
    if m>n:
      n,m = m,n
    
    #Subtract m from n. N is now even.
    n -= m
  return m*e

def cf2r(l):
  n = 1
  m = 0
  for i in l[::-1]:
    n,m = m,n
    n = m*i + n
    x = gcd(n,m)
    m = int(m/x)
    n = int(n/x)
  return [n,m]

def interpol8(l):
  y = interp(l)
  l = []
  s = ''
  e = 0
  for i in y:
    if i!=0:
      if i<0:
        s+='-'
        i = -i
      else:
        s+='+'

      m = cf2r(cf(i))
      if m[1]>1e5:
        # just write i
        m = [i,1]

      if m[0]!=1 or e==0:
        s += str(m[0])

      if e!=0:
        s += "x"
        if e!=1:
          s += "^"+str(e)
      if m[1]!=1:
        s += "/"+str(m[1])
    e += 1
  s = s.strip("+")

  return s

l = []
for i in sys.argv[1:]:
  l += [float(i)]

s = interpol8(l)
print("f(x) = %s" % (s))
