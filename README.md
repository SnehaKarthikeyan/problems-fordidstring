# problems-fordidstring

Question:

Given two strings s and n, your task is to find whether string n is forbidden in string s.

Input Description:

A string of length up-to 100 characters.

Output Description:

Print "YES", if the string n is forbidden in string s, else print "NO".

Hint:

Check whether string n is present in string s

Sample Input:

GUVITECHGUVITECH\n
TECHGUVI

Sample Output:

YES

Explanation:

The string TECHGUVI is forbidden in GUVITECHGUVITECH, so the output is YES.

Testcase 1:

Input:

GUVITECHGUVITECH\n
ECHGUUVITE

Output:

NO

Testcase 2:

Input:

GUVITECHGUVITECHGUVI\n
GUVITECHGUV

Output:

YES

Testcase 3:

Input:

GUVIGUVITECHTECHGUVITECH\n
VITECHTEC

Output:

YES

Testcase 4:

Input:

GUVIGUVITECHGUVIGUVITECHTECHGUVITECH\n
VITECHGUVITECHGUVI

Output:

NO

Testcase 5:

Input:

GUVIGUVITECHGUVIGUVITECHTECHGUVITECH\n
VITECHGUVIGUVI

Output:

YES
