import sys

# Checks to see if a line in file1 is NOT present in file2
# This does not take into account order of the lines within each file
with open(sys.argv[1], 'r') as file1:
    with open(sys.argv[2],'r') as file2:
    	# Protip: If you want to reverse this, and see what lines in file1 are present in file2
    	# change .difference() to .intersection()
        same = set(file1).difference(file2)
        
#optional
#same.discard('\n')

with open('some_output_file.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)
