
positive_test_cases = [
    "[+]",
    " [+] ",
    "  [+++] ",
    "Form [+] start",
    "Yes [+   +] an element",
    "Yes [+  +]+] an element",
    "Yes [[+   +]] element",
    "Yes [+++ + all sorts of text in here++++] an element",
    "Element and pre-element text [+   +]",
    "[+    +] element and post-element text"
    "Textarea [[]] element",
    "Yes valid element [[{[ with all sorts of text in here  }]}]] and text afterwards"
]

negative_test_cases = [
    # None, 0, 1, 2.3, True, False, 
    "",
    "No element here",
    "No element",
    "Not a [+ element",
    "No element [[ on this line",
    "No element [[] on this line",

]

unsure_test_cases = [
    "Might be a form start element [[+   +] ] certainly not a textarea",
    "Might be a textarea [[[ the validation might be taken care of later]]]"
]

for line in positive_test_cases:
    parsed_line = parse_line(line)
    if parsed_line["opening_identifier"] != None:
        print("Line with Markform element: {}".format(line))
        print(parse_line(line))
    else:
        print("Uh oh, this line is supposed to have a Markform element in it: {}".format(line))
        print("Instead, the parsed line is: {}".format(parse_line(line)))
    
for line in negative_test_cases:
    parsed_line = parse_line(line)
    if parsed_line["element_text"] == None:
        print("Line without Markform element: {}".format(line))
        print(parse_line(line))
    else:
        print("Uh oh, this line isn't supposed to have a Markform element in it: {}".format(line))
        print("Instead, the parsed line is: {}".format(parse_line(line)))
