# Markform Spec

[Markform][1] is a plain-text format, inspired by [Markdown][2], with a simple and readable syntax that can be easily converted into forms and form elements for websites.

[1]: https://github.com/jeremykohn/markform
[2]: https://daringfireball.net/projects/markdown/


## 1. Definitions

A Markform **element** is a sequence of text characters that corresponds to an HTML form element.

A Markform **element group** is an element that contains multiple elements; this can be used to create a group of checkboxes, a set of radio buttons, or a dropdown menu.

An **inner element** is an element within a Markform element group.

An **identifier** is a sequence of one or more characters, within a Markform element, that identifies the element's type.

For elements other than inner elements:
- The **opening identifier** is the identifier immediately following an element's first character.
- The **closing identifier** is the identifier immediately preceding an element's last character.
- An element's **inner content** is the text, if any, between the element's opening identifier and closing identifier.
- **Pre-element content** is any text preceding an element on the same line of text.
- **Post-element content** is any text following an element on the same line of text.

For inner elements:
- An **inner identifier** is an identifier, within an element group, that indicates the presence and type of an inner element.
- **Pre-identifier content** is any text, within an inner element, that precedes the inner identifier.
- **Post-identifier content** is any text, within an inner element, that follows the inner identifier.

A Markform **line** is a line of text that includes a Markform element.

A Markform **block** is a sequence of lines of text whose first line includes a "form start" Markform element and whose last line includes a "form end" Markform element.

A Markform **document** is a text document that includes a Markform block; the document may include text outside of the Markform block as well.
