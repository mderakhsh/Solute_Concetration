# X is box size, N is number of molecules, C is concentration
N=24
X=15.65

C=(N/((X**3)*(1e-27)))*(1./1000.)*(1./6.02e23)


print "For box size of", X,"and", N, "molecules","the concentration in Molar unit is:", C