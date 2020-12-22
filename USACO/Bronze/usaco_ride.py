"""
ID: anish151
LANG: PYTHON3
TASK: ride
"""

def number_for_str(str):
    str = str.encode()
    result = 1
    for i in str:
        result *= i-64
    return result%47

fin = open ('ride.in','r')
fout = open('ride.out','w')

cometname = fin.readline().strip()
groupname = fin.readline().strip()

cometnumber = number_for_str(cometname)
groupnumber = number_for_str(groupname)

if cometnumber == groupnumber:
    fout.write ("GO\n")
else:
    fout.write("STAY\n")

fout.close()