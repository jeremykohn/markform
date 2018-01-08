## Markform Tags

### Definition

A Markform tag is a sequence of characters, within a single line of text, that represents a specified type of input field or other form element.

### Overall tag structure

A Markform tag consists of these characters, in this order:

1. A tag opening, consisting of:
    1. An opening bracket: `[`
    2. An opening token: `+`, `_`, `@`, `*`, `$`, `%`, `^`, `(`, `[`, `{`, or `-`
2. Inner content, if any, consisting of text that does not close the tag
3. A tag closing, consisting of:
    1. A closing token: `+`, `_`, `@`, `*`, `$`, `%`, `^`, `)`, `]`, `}`, or `-`
    2. A closing bracket: `]`

### Categories of tags

#### Simple-token tags

In a simple-token tag, the opening token characer is the same as the closing token character:
- `+` Start of form
- `_` Text input
- `@` Email input
- `*` Password input
- `$` Number input
- `%` Range input
- `^` File input
- `-` End of form

#### Inverse-token tags

In an inverse-token tag, the closing token characer is the inverse of the opening token character:
- `(` `)` Submit button
- `[` `]` Textarea
- `{` `}` Checkbox group, radio button group, or select group

### Detailed tag structure

#### Simple-token tags with no inner content

1. Opening bracket: The character `[`
2. Simple token character, optionally repeated one or more times
3. Closing bracket: The character `]`

#### Simple-token tags with inner content

1. Opening bracket: The character `[`
2. Opening token: A simple-token character, optionally repeated
3. Inner content: A sequence of characters that does not close the tag
6. Closing token: The same character as the opening token character, optionally repeated
3. Closing bracket: The character `]`

#### Inverse-token tags with no inner content

1. Opening bracket: The character `[`
2. Opening token: An inverse-token character
6. Closing token: A character that is the inverse of the opening-token character
3. Closing bracket: The character `]`

#### Inverse-token tags with inner content

1. Opening bracket: The character `[`
2. Opening token: An inverse-token character
3. Inner content: A sequence of characters that does not close the tag
6. Closing token: A character that is the inverse of the opening-token character
3. Closing bracket: The character `]`
