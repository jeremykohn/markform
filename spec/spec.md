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


## 2. Structure of Markform elements

In general, a Markform element starts with an opening bracket `[`, followed immediately by a character called the "opening identifier" which indicates the element's type; and the element ends with a closing bracket `]`, preceded immediately by a character called the "closing identifier" which corresponds to the opening identifier. 

Different identifiers indicate different types of Markform elements.

For some types of elements, the opening identifier and closing identifier are of the same character. For other types of elements, the opening identifier and closing identifier are of different characters, and the characters are inverses of each other.

### 2.1 Elements with simple identifiers

| Element type | Simple identifier | Element | Element (minimal) | Element with inner content |
| -- | -- | -- | -- | -- |
| Form start     | `+` | `[+++++]` | `[+]` | `[+ Inner content +]` |
| Text input     | `_` | `[_____]` | `[_]` | `[_ Inner content _]` | 
| Email input    | `@` | `[@@@@@]` | `[@]` | `[@ Inner content @]` |
| Password input | `*` | `[*****]` | `[*]` | `[* Inner content *]` |
| Number input   | `$` | `[$$$$$]` | `[$]` | `[$ Inner content $]` |
| Range input    | `%` | `[%%%%%]` | `[%]` | `[% Inner content %]` |
| File upload    | `^` | `[^^^^^]` | `[^]` | `[^ Inner content ^]` |
| Form end       | `-` | `[-----]` | `[-]` | `[- Inner content -]` |

Each simple-identifier element consists of:

1. An opening bracket `[`
2. A simple identifier character, one or more times
3. Optionally: inner content, followed by the simple identifier one or more times
4. A closing bracket `]`

An simple-identifier element is called **"minimal"** if it is only three characters long: an opening bracket, a simple identifier that is not repeated, and a closing bracket.

### 2.2 Elements with paired (inverse) identifiers: 

| Element type | Opening identifier | Closing identifier | Element | Element with inner content |
| -- | -- | -- | -- | -- |
| Textarea      | `[` | `]` | `[[ ]]` | `[[ Inner content ]]` |
| Submit        | `(` | `)` | `[( )]` | `[( Inner content )]` |
| Element group | `{` | `}` | `[{ }]` | `[{ Inner content }]` |

Each inverse-identifier element consists of:

1. An opening bracket `[`
2. An opening identifier character
3. Inner content, which is required for only certain types of inverse-identifier elements
4. A closing identifier character, which is the inverse of the opening identifier character
5. A closing bracket `]`
