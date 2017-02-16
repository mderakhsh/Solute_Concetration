# print "This program is written to compute concentration of " \
#       "solute in Molar unit with a given box size and number of solutes"

# X is box size, N is number of molecules, C is concentration
N=24
X=15.65

C=(N/((X**3)*(1e-27)))*(1./1000.)*(1./6.02e23)


# print "For a box size of", X,"and", N, "molecules of solute","the molar concentration is:", C
print "\n"
print "\nNumber of molecules =", N
print "\nBox size =", X, "^ 3 (nm)^3"
print "\nMolar concentration =", C, "M"
print "\nMolar concentration = %.2f" % (C*1000), "mM"
