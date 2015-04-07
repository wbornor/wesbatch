Various tools that I've written mainly for use in unix/linux environments. Created to solve a specific problem I encountered at one time or another.

FixedFieldSet - shows stats on a set of fixed field records
```
>>> from FixedFieldSet import *
>>> records = ['050070200707019999', '050070200708020050', '050072200710070375']
>>> fields = [FixedField('insurer_id', 0, 6, str), 
...           FixedField('date', 6, 14, str),
...           FixedField('contract_amt', 14, 18, int), 
...           ]  
...    
>>> rp = RecordParser(fields)
>>> rp.parse(records)
>>> rp.show_stats() 
<insurer_id> count:3 sum:0 avg:0 min:0 max:0
<date> count:3 sum:0 avg:0 min:0 max:0
<contract_amt> count:3 sum:10424 avg:3474 min:50 max:9999
```


distinct - returns the distinct entries in a list
```
>>> import distinct
>>> distinct.get_distincts([1,3,5,'a',3,3,5,'b'])
[1, 3, 5, 'a', 'b']
```


unique - from a sorted file, print only unique lines. _distinct_ is not very efficient for large datasets so instead sort your file and run it through the much simpler yet efficient unique.py
```
$cat test
123
123
123
456
789
789
hi
hi
hi
no
no
$unique test
123
456
789
hi
no
```


wwbcat - for each file in a list of files, append the given string
```
$wwbcat meow wes1 wes2 wes3 wes4
$cat wes*
hi
meow
how
meow
are
meow
you?
meow
```

wwbprepend - for each file in a list of files, prepend the given string to it
```
$wwbprepend meow wes1 wes2 wes3 wes4
$cat wes*
meow
hi
meow
how
meow
are
meow
you?
```

apsuf - appends a suffix to each filename in the list of arguments
```
$apsuf sew wes1 wes2 wes3 wes4
$ls wes*
wes1sew   wes2sew   wes3sew   wes4sew
```

wwbstats - computes statistics for a list of numbers
```
$cat nums
1
5
10
15
20
$cat nums | wwbstats
sum: 51.0
avg: 10.2
max: 20.0
min: 1.0
rng: 19.0
```


sls - list directories on remote servers

lsd - list only the directory names in a directory

statusbar - print a growing status bar

[check out the code here](http://code.google.com/p/wesbatch/)