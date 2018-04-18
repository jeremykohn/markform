def get_identifier_details(identifier):

    all_details = {
        "+": {
            "type": "form_start",
            "opening_identifier": "+",
            "closing_identifier": "+",
            "identifier_category": "simple_identifier"
        },
        "-": {
            "type": "form_end",
            "opening_identifier": "-",
            "closing_identifier": "-",
            "identifier_category": "simple_identifier"
        },
        "_": {
            "type": "text_input",
            "opening_identifier": "_",
            "closing_identifier": "_",
            "identifier_category": "simple_identifier"
        },
        "@": {
            "type": "email_input",
            "opening_identifier": "@",
            "closing_identifier": "@",
            "identifier_category": "simple_identifier"
        },
        "*": {
            "type": "password_input",
            "opening_identifier": "*",
            "closing_identifier": "*",
            "identifier_category": "simple_identifier"
        },
        "$": {
            "type": "number_input",
            "opening_identifier": "$",
            "closing_identifier": "$",
            "identifier_category": "simple_identifier"
        },
        "%": {
            "type": "range_input",
            "opening_identifier": "%",
            "closing_identifier": "%",
            "identifier_category": "simple_identifier"
        },
        "^": {
            "type": "file_input",
            "opening_identifier": "^",
            "closing_identifier": "^",
            "identifier_category": "simple_identifier"
        },
        "(": {
            "type": "submit_button",
            "opening_identifier": "(",
            "closing_identifier": ")",
            "identifier_category": "paired_identifier"
        },
        "[": {
            "type": "textarea",
            "opening_identifier": "[",
            "closing_identifier": "]",
            "identifier_category": "paired_identifier"
        },
        "{": {
            "type": "element_group",
            "opening_identifier": "{",
            "closing_identifier": "}",
            "identifier_category": "paired_identifier"
        },
        "[ ]": {
            "type": "checkbox",
            "checked": False,
            "identifier_category": "inner_identifier"
        },
        "[x]": {
            "type": "checkbox",
            "checked": True,
            "identifier_category": "inner_identifier"
        },
        "( )": {
            "type": "radio_button",
            "checked": False,
            "identifier_category": "inner_identifier"
        },
        "(o)": {
            "type": "radio_button",
            "checked": True,
            "identifier_category": "inner_identifier"
        },
        ">": {
            "type": "option",
            "selected": False,
            "identifier_category": "inner_identifier"
        },
        ">>": {
            "type": "option",
            "selected": True,
            "identifier_category": "inner_identifier"
        }
    }

    return all_details[identifier]
