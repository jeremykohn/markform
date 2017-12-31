Opening and closing brackets/tokens

A Markform tag begins with an opening bracket `[`, immediately followed by a character or "opening token" that identifies the type of tag. A Markform tag ends with a character or "closing token" that corresponds to the opening token, immediatly followed by a closing bracket `]`.

For some types of Markform tags, the opening and closing tokens are the same character. Examples:
- `[+ +]`
- `[_ _]`
- `[@ @]`, etc. 

These tag types can be three characters long, with the middle character serving as both the opening token and the closing token. Examples:
  - `[+]`
  - `[_]`
  - `[@]`

Also, non-inverse tag types may include multiple opening tokens and/or closing tokens. For example: `[__  __]` is valid.

For other types of Markform tags, the closing token is the inverse of the opening token. Examples:
- `[(` `)]`
- `[[` `]]`

"Inverse" tag types may not include multiple opening tokens or multiple closing tokens. For example: `[(( ))]` is invalid.

A Markform tag may optionally include whitespace or other text between the opening token(s) and closing token(s). Any text becomes the tag's "inner content."
