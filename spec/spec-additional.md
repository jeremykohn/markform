## 3. Types of Markform elements

Each type of input, textarea, submit, etc.
Also element group

### Text input

A text input element's first two characters are an opening bracket `[` followed by an underscore `_`.

A text input element's first two characters are an underscore `_` followed by a closing bracket `]`.

If there is text content that comes before the input element, then that pre-element content is converted to a pre-element label.

If there is text content that comes after the input element, then that post-element content is converted to a post-element label.

Text inside the input element, other than the opening and closing tokens, is converted into placeholder text. (After you strip the outer spaces from pre-element and post-element content.)

Markform:

`[_ Type some things here _]`

HTML attribute and value:

`placeholder="Type some things here"`

The id of the input element is created by combining the pre-element content and post-element content. (Rules: strip outer spaces, lowercase all letters and replace each section of one or more continuous non-alphanumeric characters with a single underscore.)

(Except for spaces. Each set of one or more continous spaces is replaced with a hyphen.)

This same id is also used as the value of the `for` HTML attribute for the pre-element label and post-element label:

Markform:

`This is [___] a very nice & special input element!`

HTML:

<label for="this-is-a-very-nice-_-special-input-element">This is</label>
<input id="this-is-a-very-nice-_-special-input-element">
<label for="this-is-a-very-nice-_-special-input-element">a very nice & special input element!</label>

(Also use placeholder as part of HTML id?)
(? If there is placeholder text, it is also included as part of the input ID and label `for` values. ?)








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

`[{ (o) Yes | ( ) No }]`

#### Dropdown/select menus

A dropdown/select menu can contain, at most, one pre-selected `>>` and any number of non-pre-selected `>` dropdown options.

If multiple dropdown options are marked with `>>`, only the first of those options will be interpreted as pre-selected.

Therefore, these are equivalent:

`[{ > Choose | >> Only | >> One }]`

`[{ > Choose | >> Only | > One }]`


#### Conflicting inner element types

If an element group contains inner elements of different types, the first element's type is determinative. 

Therefore, these are equivalent:

`[{ [ ] This is a checkbox group | with three inner elements | each of which is a checkbox input. }]`

`[{ [ ] This is a checkbox group | [ ] with three inner elements | [ ] each of which is a checkbox input. }]`

These are also equivalent:

`[{ [ ] This is a checkbox group | ( ) not a radio button group | > and not a dropdown menu. }]`

`[{ [ ] This is a checkbox group | [ ] ( ) Not a radio button group | [ ] > and not a dropdown menu. }]`

In such a case, the `( )` and `>` are each interpreted as ordinary text within a checkbox element.







## 4. Structure of Markform lines

Labels, pre-element content, post-element content, etc.
