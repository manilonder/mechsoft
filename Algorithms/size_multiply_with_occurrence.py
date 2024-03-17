'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''

def find_max(t, z):
    # Initialize the maximum value to 0
    # it will keep the maximum value for each possible substring result
    max_value = 0
    #print(len(t))
    # Iterate through all possible subsequences of t
    for i in range(len(t)):
        for j in range(i + 1, len(t) + 1):
            # Get the subsequence of t
            substring = t[i:j]
            #print(substring)
            # 'count()' function is used to count the number of occurrences of a substring within a string.
            count_in_z = z.count(substring)
            
            # Calculate the value of the subsequence by multiplying its length with its count in z
            value = len(substring) * count_in_z
            #print(value)
            # Update the maximum value if the current value is greater
            max_value = max(max_value, value)
    # Return the maximum value found
    return max_value

if __name__ == '__main__':
    # Call the function with sample inputs and print the result
    result = find_max("acldm1labcdhsnd", "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")
    print(result)
