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

### Website feedback form

Markform:

```
[+]

Your name: [_]
Your email address: [@]
Your message: [[ ]]

[(Submit my message)]

[-]
```

Converted to HTML:

```
<form>
  <div>
    <label for="markform-text-input-your-name">Your name:</label>
    <input id="markform-text-input-your-name" type="text">
  </div>
  <div>
    <label for="markform-text-input-your-email-address">Your email address:</label>
    <input id="markform-text-input-your-email-address" type="email">
  </div>
  <div>
    <label for="markform-textarea-your-message">Your message:</label>
    <textarea id= markform-textarea-your-message></textarea>
  </div>
  <div>
    <button id="markform-submit-button-submit-message" type="submit">Submit my message</button>
  </div>
</form>
```

### Image upload form

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
