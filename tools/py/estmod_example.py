# -*- coding: utf-8 -*-

"""
This assumes you want to use the planetary model to calculate 
a *standard quantum TCF* of the form

  <A(0) B(t)>

where A and B are observables that can be expressed 
as functions of position and momentum variables, 

  A = A(q,p)
  B = B(q,p).

In order to determine the appropriate estimators for the
zero-time observable A, we define three alternative 'methods':

    0thorder_re
  ***Applicable when A is any function of q and p. Most accurate
  for linear operators.***
  Estimate only the real part of the TCF by simply evaluating A 
  at the position of the planet. This can be derived from the
  Wigner transform as the 0th order term following a Taylor expansion 
  about ∆ = 0 on the locally kharmonic potential.

    1storder_im
  ***Applicable when A is any function of ONLY q. Most accurate
  for operators linear in q.***
  Estimate only the imaginary part of the TCF from the gradient 
  of A at the position of the planet. Derived from a 1st order
  expansion about ∆ = 0.
 
    2ndorder_re
  ***Applicable when A is any function of ONLY q. Redundant for 
  linear operators.***
  Estimate only the real part of the TCF by evaluating A and its 
  hessian at the position of the planet. Derived from a 2st order
  expansion about ∆ = 0.

Written by Raz Benson
 
"""

import numpy as np

name = "my_tcf"        #   str      something descriptive

method = "0thorder_re" #   str      choice of "0thorder_re", "1storder_im", "2ndorder_re"
                       #            (see above)

Ashape = (3,)          #   tuple    dimension of the zero-time operator A, i.e. in the
                       #            TCF given by <A(0)B(t)>
                       #            e.g. if A is the total dipole moment then it is a 3D 
                       #            vector so Ashape = (3,)

Bshape = (3,)          #   tuple    dimension of the time-evolved operator B, i.e. in the
                       #            TCF given by <A(0)B(t)>
                       #            e.g. if B is the total dipole moment then it is a 3D 
                       #            vector so Bshape = (3,)

def Bfunc(qsum, psum):
    """
    Write a function which takes the planetary phase-space coordinates
    (centroid + fluctuation) and returns the value of B for each planet
    """
    nndof, npl = qsum.shape
    ans = np.zeros((npl,) + Bshape)
    for i in xrange(npl):
        ans[i] = 0.0 # Change this bit
    return ans

def Afunc0(qsum, psum):
    """
    (Only required if method is 0thorder_re or 2ndorder_re BUT useful 
    to include it anyway so the centroid TCF can be obtained at little
    extra cost)
    Write a function which takes the planetary phase-space coordinates
    (centroid + fluctuation) and returns the value of A for each planet
    (for an autocorrelation function Afunc0 is the same as Bfunc)
    """
    nndof, npl = qsum.shape
    ans = np.zeros((npl,) + Ashape)
    for i in xrange(npl):
        ans[i] = 0.0 # Change this bit
    return ans

def Afunc1(qsum):
    """
    (Only required if method is 1storder_im)
    Write a function which takes the planetary phase-space coordinates
    (centroid + fluctuation) and returns the gradient of A for each planet
    """
    nndof, npl = qsum.shape
    ans = np.zeros((npl,) + Ashape + (ndof,))
    for i in xrange(npl):
        ans[i] = 0.0 # Change this bit
    return ans

def Afunc2(qsum):
    """
    (Only required if method is 2ndorder_re)
    Write a function which takes the planetary phase-space coordinates
    (centroid + fluctuation) and returns the hessian of A for each planet
    """
    nndof, npl = qsum.shape
    ans = np.zeros((npl,) + Ashape + (ndof,ndof))
    for i in xrange(npl):
        ans[i] = 0.0 # Change this bit
    return ans

def corr(A, B, **kwargs):
    """
    Write a function to calculate the appropriate update to the
    TCF given estimates for A and B over a single trajectory
    """
    npts, npl = A.shape[:2]
    tcf = np.zeros(npts)
    for i in xrange(npl):
        tcf[:] += 0.0 # Change this bit
    return tcf
