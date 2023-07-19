
from typing import Match
print("Please Enter The Number of DNA Sequences ")
Number = input()
print("Enter Their Names Arranged")
Name = input()
SeqNames = [str(a) for a in Name]
Matrix = []

for i in range(int(Number)):
    print("Enter the row number ", i + 1)
    Row = input()
    Row = Row.replace(" ", "")
    Rows = [int(a) for a in Row]
    Matrix.append(Rows)

##Printing Matrix
print("The Distance Matrix You Entered Is")
print(" ", *SeqNames)
for counter in range(int(Number)):
    mat = []
    for z in range(int(Number)):
        mat.append(Matrix[counter][z])
    print(SeqNames[counter], *mat)
while len(Matrix) != 2:
    ##Getting the Minimum
    Minimum = 500000
    Merging = []
    for n in range(int(Number)):
        for z in range(int(Number)):
            if n != z:
                if (Matrix[n][z] <= Minimum):
                    Minimum = Matrix[n][z]
    ##Getting sequences that will be merged               
    for n in range(int(Number)):
        for z in range(n + 1, int(Number)):
            if Minimum == Matrix[n][z]:
                Merging.append(n)
                Merging.append(z)

    ##Printing sequences that will be merged
    print("The Sequences That will be merged")
    Mer = 0
    for i in Merging:
        Merged = SeqNames[i]
        print(Merged)
        Mer = Mer + 1
        if Mer % 2 == 0:
            print("Will be merged")

    for x in range(0, len(Merging) - 1, 2):
        SeqNames[Merging[x]] = SeqNames[Merging[x]] + "/" + SeqNames[Merging[x + 1]]
        SeqNames.remove(SeqNames[Merging[x + 1]])

    M = []
    Mt = []
    UpdatedMatrix = []
    var1 = 0
    var2 = 0

    Mt1 = []
    Mt1.append(0)
    for col in range(int(Number)):
        if col != Merging[0] and col != Merging[1]:
            Mt1.append(int((Matrix[Merging[0]][col] + Matrix[Merging[1]][col]) / 2))

    for rows in range(0, int(Number)):
        if rows == Merging[0]:
            M.append(Mt1)
            continue
        elif rows == Merging[1]:
            continue
        Mt = []
        for col in range(0, int(Number)):

            if col == Merging[0]:
                Mt.append(Mt1[rows - 1])
            elif col == Merging[1]:
                continue
            elif col == rows:
                Mt.append(0)
            else:
                Mt.append(Matrix[rows][col])
        M.append(Mt)

    print("The Distance Matrix ")
    print("  ", *SeqNames)

    for counter in range(int(Number) - 1):
        mat = []
        for z in range(int(Number) - 1):
            mat.append(M[counter][z])
        print(SeqNames[counter], *mat)
    Matrix = M
    Number = str(int(Number) - 1)
