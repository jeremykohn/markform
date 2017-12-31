### Opening, closing, and inner content

A Markform tag begins with an opening bracket `[` and ends with a closing bracket `]`.

The character immediately after the opening bracket in a Markform tag is called an "opening token." It identifies the Markform tag type. 

The character immediately before the closing bracket in a Markform tag is called a "closing token."
- In some types of tags, the closing token is the same as the opening token.
- In other types of tags, the closing token is the inverse of the opening token.

A Markform tag may optionally include whitespace or other text between the opening token(s) and closing token(s). Any text becomes the tag's "inner content."

### Same-token tags and inverse-token tags

If the opening token does not have an inverse, the closing token is the same as the opening token. 
- Tags whose opening token and closing token are inverses are called "same-token tags."
- Examples:
  - `[+ +]`
  - `[_ _]`
  - `[@ @]`
- "Same-token" tags can be three characters long, with the middle character serving as both the opening token and the closing token:
  - `[+]`
  - `[_]`
  - `[@]`
- Same-token tags may include multiple opening tokens and/or closing tokens. For example: `[__  __]` is valid.

If the opening token has an inverse, the closing token is the inverse of the opening token. 
- Tags whose opening token and closing token are inverses are called "inverse-token tags."
- Examples:
  - `[(` `)]`
  - `[[` `]]`
- Inverse-token tags may not include multiple opening tokens or multiple closing tokens. For example: `[(( ))]` is invalid.
  
