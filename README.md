# Markform

A quick shorthand for creating HTML forms, inspired by [Markdown](https://daringfireball.net/projects/markdown/).

## Form elements

| Markform code | Element name | HTML code |
| --- | -- | -- |
| `[+]` | Form start | `<form>` |
| `[_]` | Text input | `<input type="text">` |
| `[[ ]]` | Textarea | `<textarea></textarea>` |
| `[@]` | Email input | `<input type="email">` |
| `[*]` | Password input | `<input type="password">` |
| `[$]` | Number input | `<input type="number">` |
| `[%]` | Range input | `<input type="range">` |
| `[^]` | File upload | `<input type="file">` |
| `[( )]` | Submit button | `<button type="submit">` |
| `[-]` | Form end | `</form>` |

## Example usage

Markform code:

```
[+](post)(action.php)

Your name: [_]
Your email address: [@]
Your message: [[ ]]

[(Submit message)]

[-]
```

Converted to HTML:

```
<form method="post" action="action.php">
  <div>
    <label for="markform-input-your-name">Your name:</label>
    <input id="markform-input-your-name" type="text">
  </div>
  <div>
    <label for="markform-input-your-email-address">Your email address:</label>
    <input id="markform-input-your-email-address" type="email">
  </div>
  <div>
    <label for="markform-textarea-your-message">Your message:</label>
    <textarea id= markform-textarea-your-message></textarea>
  </div>
  <div>
    <button id="markform-button-submit-message" type="submit">Submit message</button>
  </div>
</form>

```
