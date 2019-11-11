# interpol8

Have you ever thought to yourself, "Gee whiz, I sure would like to be a smartass in my math or science classes!" ?
Or maybe even, "I have some actual reason to fit data exactly to a polynomial." ?

Well this might be what you are looking for! You'll need to be able to run Python programs, but the syntax for this is
something like the following, where you replace `f(n)` with numbers:

```
zeda@zeda:~$ python3 interpol8.py f(0) f(1) f(2) f(3)
```

For example, suppose you have a set `[1,4,7,10]` and you want to find the function so that `f(0)=1`, `f(1)=4`,...:

```
zeda@zeda:~$ python3 interpol8.py 1 4 7 10
f(x) = 1+3x
```

And that is cool and all, but what if you have a function that is `1` at `f(0)` and `0` for the next 6 points:

```
zeda@zeda:~$ python3 interpol8.py 1 0 0 0 0 0 0
f(x) = 1-49x/20+203x^2/90-49x^3/48+35x^4/144-7x^5/240+x^6/720
```

Not gonna lie, I just think this is fun, but I understand that for many people there are times like one time when I was in physics class that we were collecting data and we had like 60 data points and, like a jackass, I found a 59-th degree polynomial to fit each of the points. I mean, I'm not saying you *should* do that, but I totally dare you to.
