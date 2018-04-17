# Markform start and end, and Markform block

test_cases = {
    'not_a_markform_block': [' ', '[_]', '[_]\n[-]', '[-]\n[_]'], 
    'markform_block_without_input_element': ['[+]', '[+]\n[-]', '[+]\n\n[-]', '[-]\n[_]\n[+]', '[-]\n[_]\n[+]', '[+] [_] [-]'], 
    'markform_end_true': ['[-]', ' [-]', '  [-]', '   [-]', '    [-]', '[--]', '[- -]', '[---]', '[- Content -]', '[-] [+]', '[-] Content [+]'], 
    'markform_end_false': [' ', '[]', '   \n[ -]', '[ - ]', '[- ]', '[+] [-]', '[+] Content [-]', 'Content [-]'], 
    'markform_block_with_input_element': ['[+]\n[_]\n[-]', '[+]\n\n[_]\n[-]', '[+]\n[_]\n\n[-]', '[+]\n\n[_]\n\n[-]', '[+]\n[_]', '[+]\n\n[_]'], 
    'markform_start_true': ['[+]', ' [+]', '  [+]', '   [+]', '    [+]', '[++]', '[+ +]', '[+++]', '[+ Content +]', '[+] [-]', '[+] Content [-]'], 
    'markform_start_false': [' ', '[]', '[-]', '[_]', '   \n[ +]', '[ + ]', '[+ ]', '[-] [+]', '[-] Content [+]', 'Content [+]']
}

print(test_cases)




# Prev

consolidated_test_cases = {'not_a_markform_block': ['\n \n', '\n[_]\n', '\n[_]\n[-]\n', '\n[-]\n[_]\n'], 'markform_block_without_input_element': ['\n[+]\n', '\n[+]\n[-]\n', '\n[+]\n\n[-]\n', '\n[-]\n[_]\n[+]\n', '\n[-]\n[_]\n[+]\n', '\n[+] [_] [-]\n'], 'markform_end_true': ['\n[-]\n', '\n [-]\n', '\n  [-]\n', '\n   [-]\n', '\n[--]\n', '\n[- -]\n', '\n[---]\n', '\n[- Content -]\n', '\n[-] [+]\n', '\n[-] Content [+]\n'], 'markform_end_false': ['\n \n', '\n[]\n', '\n    [-]\n', '    \n[ -]\n', '\n[ - ]\n', '\n[- ]\n', '\n[+] [-]\n', '\n[+] Content [-]\n', '\nContent [-]\n'], 'markform_block_with_input_element': ['\n[+]\n[_]\n[-]\n', '\n[+]\n\n[_]\n[-]\n', '\n[+]\n[_]\n\n[-]\n', '\n[+]\n\n[_]\n\n[-]\n', '\n[+]\n[_]\n', '\n[+]\n\n[_]\n'], 'markform_start_true': ['\n[+]\n', '\n [+]\n', '\n  [+]\n', '\n   [+]\n', '\n    [+]\n', '\n[++]\n', '\n[+ +]\n', '\n[+++]\n', '\n[+ Content +]\n', '\n[+] [-]\n', '\n[+] Content [-]\n'], 'markform_start_false': ['\n \n', '\n[]\n', '\n[-]\n', '\n[_]\n', '    \n[ +]\n', '\n[ + ]\n', '\n[+ ]\n', '\n[-] [+]\n', '\n[-] Content [+]\n', '\nContent [+]\n']}
# print(consolidated_test_cases)

for test_category in consolidated_test_cases:
    test_list = consolidated_test_cases[test_category]
    consolidated_test_cases[test_category] = [test_case[1:-1] for test_case in test_list]

# print(consolidated_test_cases)




# Prev

test_cases_from_github = {

"markform_start_true": [

"""
[+]
"""
,
"""
 [+]
"""
,
"""
  [+]
"""
,
"""
   [+]
"""
,
"""
    [+]
"""
,
"""
[++]
"""
,
"""
[+ +]
"""
,
"""
[+++]
"""
,
"""
[+ Content +]
"""
,
"""
[+] [-]
"""
,
"""
[+] Content [-]
"""
],
"markform_start_false": [

"""
 
"""
,
"""
[]
"""
,
"""
[-]
"""
,
"""
[_]
"""
,
"""    
[ +]
"""
,
"""
[ + ]
"""
,
"""
[+ ]
"""
,
"""
[-] [+]
"""
,
"""
[-] Content [+]
"""
,
"""
Content [+]
"""
],
"markform_end_true": [

"""
[-]
"""
,
"""
 [-]
"""
,
"""
  [-]
"""
,
"""
   [-]
"""
,
"""
[--]
"""
,
"""
[- -]
"""
,
"""
[---]
"""
,
"""
[- Content -]
"""
,
"""
[-] [+]
"""
,
"""
[-] Content [+]
"""
],

"markform_end_false": [

"""
 
"""
,
"""
[]
"""
,
"""
    [-]
"""
,
"""    
[ -]
"""
,
"""
[ - ]
"""
,
"""
[- ]
"""
,
"""
[+] [-]
"""
,
"""
[+] Content [-]
"""
,
"""
Content [-]
"""
],

"markform_block_with_input_element": [


"""
[+]
[_]
[-]
"""

,
"""
[+]

[_]
[-]
"""
,
"""
[+]
[_]

[-]
"""
,
"""
[+]

[_]

[-]
"""
,
"""
[+]
[_]
"""
,
"""
[+]

[_]
"""
],


"markform_block_without_input_element": [

"""
[+]
"""
,
"""
[+]
[-]
"""
,
"""
[+]

[-]
"""
,
"""
[-]
[_]
[+]
"""
,
"""
[-]
[_]
[+]
"""
,
"""
[+] [_] [-]
"""
],


"not_a_markform_block": [

"""
 
"""
,
"""
[_]
"""
,
"""
[_]
[-]
"""
,
"""
[-]
[_]
"""
]
}



# Display all test cases.
# print(test_cases_from_github)
