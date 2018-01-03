# Markform

A quick shorthand for creating HTML forms, inspired by [Markdown](https://daringfireball.net/projects/markdown/).

## Form elements

| Element name | Markform code | HTML code |
| --- | -- | -- |
| Form start | `[+]` | `<form>` |
| Text input | `[_]` | `<input type="text">` |
| Textarea | `[[ ]]` | `<textarea></textarea>` |
| Email input | `[@]` | `<input type="email">` |
| Password input |`[*]` | `<input type="password">` |
| Number input | `[$]` | `<input type="number">` |
| Range input | `[%]` | `<input type="range">` |
| File upload | `[^]` | `<input type="file">` |
| Submit button | `[( )]` | `<button type="submit">` |
| Form end | `[-]` | `</form>` |

## Example usage

### Sign-up form example

Markform:

```
[+]

First name: [_]
Last name: [_]
Email address: [@]
Choose a password: [*]

[(Create my account)]

[-]
```

Converted to HTML:

```
<form>
  <div>
    <label for="markform-text-input-first-name">First name:</label>
    <input id="markform-text-input-first-name" type="text">
  </div>
  <div>
    <label for="markform-text-input-last-name">Last name:</label>
    <input id="markform-text-input-last-name" type="text">
  </div>
  <div>
    <label for="markform-text-input-email-address">Email address:</label>
    <input id="markform-text-input-email-address" type="email">
  </div>
  <div>
    <label for="markform-text-input-choose-a-password">Choose a password:</label>
    <input id="markform-text-input-choose-a-password" type="password">
  </div>
  <div>
    <button id="markform-submit-button-create-my-account" type="submit">Create my account</button>
  </div>
</form>
```

### Upload image

Markform:

```
[+]

Image to rescale: [^]

Horizontal resolution: [$]
Vertical resolution: [$]

[(Upload image)]

[-]
```

Converted to HTML:

```
<form>
  <div>
    <label for="markform-file-input-image-to-rescale">Image to rescale:</label>
    <input id="markform-file-input-image-to-rescale" type="file">
  </div>
  <div>
    <label for="markform-number-input-horizontal-resolution">Horizontal resolution:</label>
    <input id="markform-number-input-horizontal-resolution" type="number">
  </div>
  <div>
    <label for="markform-number-input-vertical-resolution">Vertical resolution:</label>
    <input id="markform-number-input-vertical-resolution" type="number">
  </div>
  <div>
    <button id="markform-submit-button-upload-image" type="submit">Upload image</button>
  </div>
</form>
