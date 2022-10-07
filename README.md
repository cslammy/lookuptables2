What is this? Python script to create lookup tables
but of a strange kind: each array entry is a frequency

Take a look at what to enter (edit the main.py file)

     ########## change these values##############################
     cents_between_entries = 3  #how many cents do you want between each entry?
     starting_value = 'C0'  #what semitone do you want to start at?
     stop_value = 'C10'      #what semitone do you want to stop at?
     output_filename = "list.csv"
     output_filename_reversed = "list.rev.csv"
     output_trunc_filename = "list.trunc_floats.csv"
     output_trunc_filename_reversed = "list.trunc_floats_reverse.csv"
     precision = 2
     ############################################################

Output is 4 CSV files saved to the same directory you run
the script in  

Precision is the # of decimel places you want for each
frequency entry.

The data above creates files with about 4000 floats in a CSV.

The distance between each float is 3 cents.

the range of the file is C0 to C10 (10 octaves).

Hence the creation about about 4K entries into the array.

one application for this is lookup tables for devices like the AD9833 IC.
the lookup table finds a 12 bit entry from a ADC and returns a frequency for the chip to send to its output.
