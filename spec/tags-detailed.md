### Overall rules of forming tags

A Markform tag is comprised of, in sequence: 
  1. A tag opening 
  2. Inner content (Optional)
  3. A tag closing

A Markform tag begins at the earliest tag opening for which there is a later tag closing of the same type, and ends at the earliest tag closing of that type.

Each Markform tag must be within a single line of text; that is, it cannot include newline characters.

### Components of a Markform tag

1. Tag opening
    1. Opening bracket: The character `[`
    2. Opening token: A character that determines the type of Markform tag
        - An opening token is called "simple" if it is comprised of a character on this list: `+ - _ @ * $ % ^`
        - An opening token is called "inverse" if it is comprised of a character on this list: `( { [`
        - Simple opening token characters may optionally be repeated one or more times. The additional characters will be considered part of the opening token.
        - If an inverse opening token character is repeated, only the first of these characters will be considered part of the tag's opening token.
    3. (Optional) Opening whitespace: One or more spaces

2. (Optional) Inner content: Any text between the tag opening and tag closing.
    - In a simple-token tag, inner content can begin with the same character as the tag's opening-token character, or end with the same character as the tag's closing token character, but only if the inner content is separated from the respective token by one or more spaces. Otherwise, all the consecutive opening-token characters or closing-token characters will be considered part of the respective token, not part of the inner content.
    - In an inverse-token tag, inner content can begin with the same character as the tag's opening-token character, and inner content can end with the same character as the tag's closing token character.
    - Inner content cannot contain any newline characters; this would break up the text onto multiple lines, and a Markform tag would not be formed.
    - Inner content cannot begin or end with any spaces, since the spaces will be considered part of the opening whitespace or closing whitespace respectively.

3. Tag closing
    1. (Optional) Closing whitespace: One or more spaces
    2. Closing token: A single character that corresponds to the opening token:
        - For simple opening tokens, the closing token character is the same as the opening token character.
        - For inverse opening tokens, the closing token character is the inverse of the opening token character:
            - The inverse of `(` is `)`
            - The inverse of `{` is `}`
            - The inverse of `[` is `]`
    3. Closing bracket: The character `]`

### Permissible overlap of tag opening and tag closing

In a simple-token tag, the opening and closing tokens may overlap if there are no other characters in between. Examples:
- `[+]`
- `[++]`
- `[+++++]`

In any Markform tag, the opening and closing whitespaces may overlap if there are no other characters in between. Examples:
- `[+ +]`
- `[+   +]`
- `[+  ++++]`
- `[+++   +++]`