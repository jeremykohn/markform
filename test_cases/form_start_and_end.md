# Markform start and end

## Markform start

A Markform start tag begins with an opening bracket and ends with a closing bracket. In between, it can include one or more plus signs with no other characters; or it can include a plus sign direclty after the opening bracket, another plus sign directly before the closing bracket, and optionally other text in between.

A Markdown start element consists of a line beginning with zero to three spaces, immediately followed by a Markform start tag, optionally followed by additional text.

### Test cases: Markform start

#### True:

```
[+]
```

```
 [+]
```

```
  [+]
```

```
   [+]
```

```
[+ +]
```

```
[+ Content +]
```

```
[+] [-]
```

```
[+] Content [-]
```

#### False:

```
 
```

```
[]
```

```
[-]
```

```
[_]
```

```
    [+]
```

```    
[ +]
```

```
[ + ]
```

```
[+ ]
```

```
[-] [+]
```

```
[-] Content [+]
```

```
Content [+]
```

## Markform end

A *Markform end tag* begins with an opening bracket and ends with a closing bracket. In between, it can include one or more minus signs with no other characters; or it can include a minus sign direclty after the opening bracket, another minus sign directly before the closing bracket, and optionally other text in between.

A *Markdown end element* consists of a line beginning with zero to three spaces, immediately followed by a Markform end tag, optionally followed by additional text.

### Test cases: Markform end

#### True

```
[-]
```

```
 [-]
```

```
  [-]
```

```
   [-]
```

```
[- -]
```

```
[- Content -]
```

```
[-] [+]
```

```
[-] Content [+]
```


#### False

```
 
```

```
[]
```

```
    [-]
```

```    
[ -]
```

```
[ - ]
```

```
[- ]
```

```
[+] [-]
```

```
[+] Content [-]
```
```
Content [-]
```


## Markform block

A *Markform block* begins with a Markform start element, and ends with either a Markform end element or the end of the document.

### Test cases: Markform block without input element

#### True

```
[+]
```

```
[+]
[-]
```

```
[+]

[-]
```

```
[-]
[_]
[+]
```

```
[+]

Content

[-]
```

```
[-]

Content

[+]
```


#### False:

```
[_]
```

```
[+]
[_]
```

```
[+]
[_]
[-]
```


### Test cases: Markform block with input element

#### True:

```
[+]
[_]
[-]
```


```
[+]

[_]
[-]
```

```
[+]
[_]

[-]
```

```
[+]

[_]

[-]
```

```
[+]
[_]
```

```
[+]

[_]
```


#### False:

```
[_]
```

```
[_]
[-]
```

```
[-]
[_]
```

```
[-]
[_]
[+]
```

```
[+] [_] [-]
```
