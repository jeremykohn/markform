A Markform tag begins with an opening bracket `[`, immediately followed by a character or "token" that identifies the type of tag.

A Markform tag ends with an opening bracket `]`, immediately preceded by a character or "token" that identifies the type of tag, and that is either the same as the opening token, or the mirror image (inverse) of the opening token, depending on the type of tag.

Types of Markform tags whose opening and closing tokens are inverses of each other may not include multiple opening tokens or multiple closing tokens: `[((( ))]` is invalid. However, other types of Markform tags may have mulitple opening tokens and/or closing tokens: `[___  __]` is valid.

A Markform tag may optionally include whitespace or other text between the opening token(s) and closing token(s). Any text becomes the tag's "inner content."
