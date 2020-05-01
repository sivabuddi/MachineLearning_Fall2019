'''
Question1 :
Write a program to find a longest substring without repeating characters from a given string input from the console.
Sample Input: ‘ababcdxa’
Sample Output: abcdx
'''


class StringOperations:
    def longest_substring(self, input_string):
        temp_string = ""
        longest_substring = ""
        char_list = []
        for a in input_string:
            if a in char_list:
                longest_substring = self.clean_list(char_list, a, temp_string, longest_substring)
                char_list.append(a)
            if a not in char_list:
                char_list.append(a)

        for a in char_list:
            temp_string += a
        if len(longest_substring) < len(temp_string):
            longest_substring = temp_string
        print(longest_substring)

    def clean_list(self, input_list, char, temp_string, longest_substring):
        for a in input_list:
            temp_string += a
        for i in range(input_list.index(char) + 1):
            del input_list[0]
        if len(longest_substring) < len(temp_string):
            longest_substring = temp_string
        return longest_substring
