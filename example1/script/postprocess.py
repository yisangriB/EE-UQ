#!/usr/bin/python
#EDP:Disp_Node_4;Disp_Node_3
# written: fmk 01/18

import sys
import re

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

EDPs = ['Node_4_Disp', 'Node_3_Disp']

inputArgs = sys.argv

#outFile = open('results.out','w')

#
# process output file "SimCenterOut.txt" for nodal displacements
#

with open ('node.out', 'rt') as inFile:
    line = inFile.readline()
    line = inFile.readline()
    line = inFile.readline()
    print(line)
    print(line.split())
    displ = line.split()
    numNode = len(displ)

print(numNode)

inFile.close

#
# now process the input args and write the results file
#

outFile = open('results.out','w')

#
# note for now assuming no ERROR in user data
#
#for i in inputArgs[1:]:

for i in EDPs[0:]:
    print i
    theList=i.split('_')

    if (theList[0] == 'Node'):
        nodeTag = int(theList[1])

        if (nodeTag > 0 and nodeTag <= numNode):
            if (theList[2] == 'Disp'):
                nodeDisp = displ[nodeTag-1]
                outFile.write(nodeDisp)
                outFile.write(' ')
            else:
                outFile.write('0. ')
        else:
            outFile.write('0. ')
    else:
        outFile.write('0. ')

outFile.close