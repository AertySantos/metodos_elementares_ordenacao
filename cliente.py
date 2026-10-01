import sys
import time

from sorts import insertion_sort, selection_sort, bubble_sort, shaker_sort

def main():
    # reading the input data

    # example of time counting for reading the input data

    #start the timer
    start = time.time()
    input_data = []
    with open(sys.argv[1], 'r') as file:
        # Read each line in the file
        for line in file:
            x = int(line)
            input_data.append(x)
            #print(f"{x} \n")


    print(len(input_data))

    # stop the timer
    
    # calculate elapsed time
    

    #start the timer 
    #sortting arrays
    res = selection_sort(input_data.copy())
    end = time.time()
    
    #print(res)
    print(end - start)
    start = time.time()

    
    res = insertion_sort(input_data.copy())
    end = time.time()
    #print(res)
    print(end - start)
    start = time.time()

    
    res = bubble_sort(input_data.copy())
    end = time.time()
    #print(res)
    print(end - start)
    start = time.time()

    
    res = shaker_sort(input_data.copy())
    end = time.time()
    #print(res)
    print(end - start)

    # stop the timer
    # printing sorted arrays
    
    del input_data
    file.close()        
    
main()