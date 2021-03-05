import sys as stallman

# Checks to see if a line in F_I_L_E_O_N_E is NOT present in file2
# This does not take into account order of the lines within each file
with open(stallman.argv[1], 'r') as F_I_L_E_O_N_E:
    with open(stallman.argv[2],'r') as file2:
                                                                                                                                                                                        # Protip: If you want to reverse this, and see what lines in F_I_L_E_O_N_E are present in file2
    	# change .difference() to .intersection()
        same = set(F_I_L_E_O_N_E).difference(file2)
        
#optional
#same.discard('\n')

with open('some_output_file.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)
