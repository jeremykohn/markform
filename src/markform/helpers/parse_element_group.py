        # Element group.
        elif identifier == "{":
            # Parse the inner content first, to get components and determine valid type of element group. If any.
            parsed_element_group = parse_element_group(inner)
            group_type = parsed_element_group["group_type"]
            inner_element_list = parsed_element_group["inner_element_list"]  # Each inner element includes a [ ], [x], ( ), (o), or >, but not | characters
            # Checkbox group.
            if group_type == "checkbox":
                output = create_html.checkbox_group(pre_element_content=pre, post_element_content=post, inner_element_list=inner_element_list)
            # Radio button group.
            elif group_type == "radio":
                output = create_html.radio_group(pre_element_content=pre, post_element_content=post, inner_element_list=inner_element_list)
            # Select / dropdown menu.
            elif group_type == "dropdown":
                output = create_html.dropdown_menu(pre_element_content=pre, post_element_content=post, inner_element_list=inner_element_list)
            else:
                # Don't convert element group, just append to output.
                output = line




# Return 
# "group_type": checkboxes, radio, or dropdown
# "inner_element_list": list of inner elements, split acc to pipe characters
    # [{"pre_identifier_content":     "identifier_type",     "checked": True, "selected": True,     "post_identifier_content":     ]


def parse_element_group(inner_content):
    # Split on unescaped pipes.
    parsed_inner_elements = []
    pos = 0



# Then pass inner_element_list to checkbox_group(), radio_group(), or dropdown_menu()



# Refactor:
# Change to 

elif identifier == "{":
    output = create_html.element_group( ... )
    # and then within element_group() there's parse_element_group, create checkbox_group, etc.


    # Here, the first type determines the type of element group.
    # In others, treat inner identifier as ordinary text? Or remove it? And how to determine whether it's 'checked', 'selected', etc?

    # I think just convert it to a label (or dropdown option), including inner identifier.




    # Pre > Post
    # Is that <option>Pre Post</option> ?
    # Or something else?
    # Or require only post- `>` content?
