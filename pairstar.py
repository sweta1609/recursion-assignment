def starpair(input , output, i = 0):
    output = output + input[i]
    if (i == len(input)-1):
        print(output)
        return
    if (input[i] == input[i+1]):
        output = output + '*'
    starpair(input , output, i+1)
Input = input().strip()
Output = ""
starpair(Input, Output)
