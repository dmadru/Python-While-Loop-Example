'''
prog5.py     Author:Dylan Madru

This program reads values from an external file, baseball.txt,
calculates the averege of the baseball averages for the team
by adding all of the values and dividing by the count,
and determines the number of people on the team by using the same count.
The program uses a while loop to process the values that will run until it hits
the "sentinel" value, -1. It also calculates the highest and lowest averages
for the team by using 'if' statements. These results are printed
in the program and are also sent to an external file, results.txt.

'''
def DescribeProgram():
    print("""This program reads values from an external file, baseball.txt, determines the
number of players on the team, and calculates the averege of the baseball
averages for the team. It also calculates the highest and lowest averages
for the team. These results are printed in the program and are also sent to
an external file, results.txt.
""")
def main():

    DescribeProgram()

    
    baseball_obj = open("baseball.txt",'r')
    results_obj = open("prog5_results.txt", 'w')
    #Initialize variables
    sum = 0
    count = 0
    average = 0
    high = 0
    low = 1
    
    SENTINEL = -1

    baseball = float(baseball_obj.readline())
    while baseball != SENTINEL:
        print(format(baseball,'.3f'))
        results_obj.write(str(format(baseball,'.3f'))+'\n')
        count+=1
        if baseball > high:
            high = baseball
        if baseball < low:
            low = baseball
        sum+= baseball
        baseball = float(baseball_obj.readline())
    
    average = sum/count
    average = round(average, 3)
    #Displays results and writes to the file "results.txt"
    print("The average of the batting averages is",format(average,'.3f'))
    results_obj.write("The average of the batting averages is "+str(format(average,'.3f')))
    print("The number of players on the team is ",count)
    results_obj.write("\nThe number of players on the team is "+str(count))
    print("The highest average was ",format(high,'.3f'))
    results_obj.write("\nThe highest average was "+str(format(high,'.3f')))
    print("The lowest average was ",format(low, '.3f'))
    results_obj.write("\nThe lowest average was "+str(format(low,'.3f')))
    baseball_obj.close()
    results_obj.close()


main()
