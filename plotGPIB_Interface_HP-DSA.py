# Simple plotter utility for DSA to be used
# when measuring two traces.
# Michael Douglass

import visa
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import csv

# Make a directory to put the data we collect
if os.path.exists('Plots') != True:
    os.mkdir('Plots')

# Names of csv files to be saved
fn1 = 'TRACEA'
fn2 = 'TRACEB'

# Open csv files
# Will overwrite any previous data of same name
f1 = open('Plots/'+fn1+'.csv', 'w', newline='\n')
f2 = open('Plots/'+fn2+'.csv', 'w', newline='\n')

# Initialize csv writers from files
trace1Writer = csv.writer(f1)
trace2Writer = csv.writer(f2)

# Open up the resource manager
rm = visa.ResourceManager()

# and use that to find our GPIB
# ls is the list of all currently connected resources
ls = rm.list_resources()
print(ls)

# connect to our GPIB
# The instrument of interest is always listed first
# This is why ls[0] is used
instr = rm.open_resource(ls[0])

# Query the y-values for TRACE A (y1) and TRACE B (y2)
y1 = instr.query_ascii_values('CALC1:DATA?')
y2 = instr.query_ascii_values('CALC2:DATA?')

# Query the x-query_ascii_values
x1 = instr.query_ascii_values('CALC1:X:DATA?')
x2 = instr.query_ascii_values('CALC2:X:DATA?')

# Common csv writing sequence
# Ordered x and y values
tr1 = zip(x1, y1)
tr2 = zip(x2, y2)
for val in tr1:
    trace1Writer.writerow(val)
for val in tr2:
    trace2Writer.writerow(val)

# Plot on semilogx axes
fig = plt.figure()

ax = fig.add_subplot(211)
ax.semilogx(x1, y1)
ax.grid()
ax.set_xlabel('Frequency')
ax.set_ylabel('TRACE A')

ax2 = fig.add_subplot(212)
ax2.semilogx(x2, y2)
ax2.grid()
ax2.set_xlabel('Frequency')
ax2.set_ylabel('TRACE B')

plt.tight_layout()
plt.savefig('Plots/DSA_Trace.png')
plt.show()
