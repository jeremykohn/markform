# Test Cases

## Markform start and end

### Markform start

Start of form, can be converted to `<form>` tag

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


### Not a Markform start

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



## Markform end

Can be converted to `</form>` tag if it is preceded by a Markform start

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


### Not a Markform end

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







