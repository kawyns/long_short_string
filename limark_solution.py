import collections

def minSubstring(s, t):

    # creates a dict that counts all the unique characters in t
    list_count = collections.Counter(t)


    # the total length of the string t
    length = len(t)

    # the starting (left) pointer
    i = 0

    # the placeholder variable for the final position of the starting pointer
    I = 0

    # placeholder value for the final position of the ending (right) pointer
    J = 0


    # counts all the characters in s starting from  index 1 instead of 0
    for j, c in enumerate(s, 1):


        # if the character in s is greater than 0 in the unique characters dictionary, the length of t is decreased by that number
        length -= list_count[c] > 0

        # list_count will update with the counts of all characters of s that needs to be decreased
        list_count[c] -= 1

        if not length:
            # i goes along the entire length of list_count
            # if length is not less than 0 while the first character of the index of s is less than 0
            while i < j and list_count[s[i]] < 0:

                # 1 is added to list count and the left pointer moves 1 to the right. this continues and all character counts are updated
                list_count[s[i]] += 1
                i += 1

                # when the value of the left pointer has reached a point where i = 0 and cannot go on anyfurther decreasing the list_counts
                # I is assigned the position of i and J is assigned the final position of j
                # the remaining values contain atleast 1 of the original characters in t
            if not J or j - i <= J - I:
                I = i
                J = j
    return s[I:J]


s = input("Input the long string: ")
t = input("Input the short string: ")
print(minSubstring(s,t))
