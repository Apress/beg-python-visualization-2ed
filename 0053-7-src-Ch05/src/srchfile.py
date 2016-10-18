# for the solution to the exercise
from math import ceil, log10

def srchfile(filename, substr):
    """Searches for a substring in a file."""
    for index, line in enumerate(open(filename, encoding='latin-1')):
        if line.find(substr) != -1:
            try:
                print("%4d:%s" % (index, line.rstrip()))
            except UnicodeEncodeError:
                print("%4d: --- encoding error ---" % index)
 
def srchfile_ex(filename, substr):
    """Searches for a substring in a file."""
    lines = open(filename, encoding='latin-1').readlines()
    fmt = r'%' + str(int(log10(len(lines)))+1) + r'd:%s'
    for index, line in enumerate(lines):
        if line.find(substr) != -1:
            try:
                print(fmt % (index, line.rstrip()))
            except UnicodeEncodeError:
                print("%d: --- encoding error ---" % index)
