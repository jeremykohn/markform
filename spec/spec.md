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

Each simple-identifier element consists of:

1. An opening bracket `[`
2. A simple identifier character, one or more times
3. Optionally: inner content, followed by the simple identifier one or more times
4. A closing bracket `]`

The identifier determines the type of form element:

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

A simple-identifier element is called **"minimal"** if it is only three characters long: an opening bracket, a simple identifier that is not repeated, and a closing bracket.

### 2.2 Elements with paired (inverse) identifiers: 

Each inverse-identifier element consists of:

1. An opening bracket `[`
2. An opening identifier character
3. Inner content, which is required for only certain types of inverse-identifier elements
4. A closing identifier character, which is the inverse of the opening identifier character
5. A closing bracket `]`

The identifier determines the type of form element:

| Element type | Opening identifier | Closing identifier | Element | Element with inner content |
| -- | -- | -- | -- | -- |
| Textarea      | `[` | `]` | `[[ ]]` | `[[ Inner content ]]` |
| Submit        | `(` | `)` | `[( )]` | `[( Inner content )]` |
| Element group | `{` | `}` | `[{ }]` | `[{ Inner content }]` |

### 2.3 Element groups and inner elements

| Element group type | Element group |
| -- | -- |
| Checkbox group       | `[{ [x] Pre-checked checkbox \| [x] Also pre-checked \| [ ] Not pre-checked }]`       |
| Radio button group   | `[{ (o) Pre-checked radio button \| ( ) Not pre-checked \| ( ) Also not pre-checked }]` |
| Dropdown/Select menu | `[{ > Dropdown option \| >> Pre-selected default option \| > Another option }]` |

An element group consists of:

1. An opening bracket `[`
2. An opening curly brace `{`, which is the element group's opening identifier
3. Inner content, consisting of one or more inner elements that are separated from each other by pipe `|` characters
4. A closing curly brace `}`, which is the element group's closing identifier
5. A closing bracket `]`

Each inner element consists of:

1. Optionally: Pre-identifier content
2. An inner identifier
3. Optionally: Post-identifier content

The pre-identifier content or post-identifier content can include pipe characters, but only if they are "escaped" by prepending a backslash: the two-character sequence `\|` is interpreted as a pipe character within an inner element.

Each inner element has an **"inner element identifier"** which indicates the type of form element, and also indicates whether or not that element is pre-checked or pre-selected.

The type of inner element determines the type of element group:

| Element group type | Inner element type | Identifier | Element |
| -- | -- | -- | -- |
| Checkbox group       | Checkbox input (pre-checked)   | `[x]` | `[x] Option 1` |
| Checkbox group       | Checkbox input                 | `[ ]` | `[ ] Option 2` |
| Radio button group   | Radio input (pre-checked)      | `(o)` | `(o) Option 1` |
| Radio button group   | Radio input                    | `( )` | `( ) Option 2` | 
| Dropdown/Select menu | Dropdown option (pre-selected) | `>>`  | `>> Option 1`  |
| Dropdown/Select menu | Dropdown option                | `>`   | `> Option 2`   |
