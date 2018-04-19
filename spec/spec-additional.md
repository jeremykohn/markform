## 3. Types of Markform elements

Each type of input, textarea, submit, etc.
Also element group

###

###

### Rules for Priority in Resolving Conflicts in Element Groups

#### Checkbox groups

A checkbox group can contain any combination of pre-checked `[x]` and non-pre-checked `[ ]` checkbox elements. 

If multiple checkboxes in the same group are checked, there is no conflict.

#### Radio button groups

A radio button group can contain, at most, one pre-checked `(o)` and any number of non-pre-checked `( )` radio button elements. 

If multiple radio button elements are marked as "pre-checked", only the first of those elements will be interpreted as pre-checked. 

Therefore, these are equivalent:

`[{ (o) Yes | (o) No }]`

and

`[{ (o) Yes | ( ) No }]`

#### Dropdown/select menus

A dropdown/select menu can contain, at most, one pre-selected `>>` and any number of non-pre-selected `>` dropdown options.

If multiple dropdown options are marked with `>>`, only the first of those options will be interpreted as pre-selected.

Therefore, these are equivalent:

`[{ > Choose | >> Only | >> One }]`

and

`[{ > Choose | >> Only | > One }]`


#### Conflicting inner element types

If an element group contains inner elements of different types, the first element's type is determinative. 

Therefore, these are equivalent:

`[{ [ ] This is a checkbox group | with three inner elements | each of which is a checkbox input. }]`

and

`[{ [ ] This is a checkbox group | [ ] with three inner elements | [ ] each of which is a checkbox input. }]`


These are also equivalent:

`[{ [ ] This is a checkbox group | ( ) not a radio button group | > and not a dropdown menu. }]`

and

`[{ [ ] This is a checkbox group | [ ] ( ) Not a radio button group | [ ] > and not a dropdown menu. }]`

In such a case, the `( )` and `>` are each interpreted as ordinary text within a checkbox element.







## 4. Structure of Markform lines

Labels, pre-element content, post-element content, etc.
