# Markform start and end

## Markform start

A *Markform start tag* begins with an opening bracket and ends with a closing bracket. In between, it can include one or more plus signs with no other characters; or it can include a plus sign direclty after the opening bracket, another plus sign directly before the closing bracket, and optionally other text in between.

A *Markform start element* consists of a line beginning with zero to three spaces, immediately followed by a Markform start tag, optionally followed by additional text.

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
[++]
```

```
[+ +]
```

```
[+++]
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

A *Markform end element* consists of a line beginning with zero to three spaces, immediately followed by a Markform end tag, optionally followed by additional text.

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
[--]
```

```
[- -]
```

```
[---]
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

Any Markform elements inside a Markform block are converted to HTML. The start and end of the Markform block are respectively converted to an opening `<form>` tag and a closing `</form>` tag.

### Test cases: Markform blocks

#### Markform block with input element


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



#### Markform block without input element

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
[-]
[_]
[+]
```

```
[+] [_] [-]
```



#### Not a Markform block

```
 
```

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

