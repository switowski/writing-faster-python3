# Writing Faster Python 3

## Code examples

All the Python files contains code examples I used in the presentation (and some examples that I didn't include). At the top of each file you will find a short description of what this example compares and the command I used to run the benchmarks.

In the _just-for-fun_ folder you can find code examples that should be treated as curiosities (seriously, don't replace `bool(variable)` with `not not variable` just because it's faster).

## Benchmarking methodology

I use a pretty simple way of benchmarking:

```shell
$ python -m timeit -s "from mymodule import test_function" "test_function()"
```

It uses the timeit module to:

1. Execute some setup code **that won't be part of the benchmark** (i.e. the setup code is executed before the timing starts). That setup code is what we pass to the `-s` option, e.g. `from mymodule import test_function`.
2. Measure the execution time of some code (that code is located in the second pair of double quotes, so `test_function()` in the above example)

I use the default settings of the timeit module because I think they are good enough and I want to keep my setup simple, even if it will be slightly different from the "real world" usage (e.g. timeit [disables the garbage collection](https://docs.python.org/3/library/timeit.html#timeit.Timer.timeit))

I have also disabled creation of the compiled bytecode in the `__pycache__` directory with by setting PYTHONDONTWRITEBYTECODE=1 environment variable.

### Each run of test_function should be independent

It's very important to design the test functions in such a way that each loop in the `timeit` run is independent from previous loops.

A good example here is the `list.sort()` function. If we create a list in the setup code (which sounds like a reasonable thing to do, because we want to benchmark the sorting, not the list creation time) and run `list.sort()` more than once, the 2nd and each next run will be much faster (since `sort()` sorts list in place and sorting a sorted list is faster than sorting an unsorted list). So we have to make sure that we always randomize the list before we call `sort()`.

## Stricter benchmarks

At some point I thought: _"Hmm, I'm using the default settings of timeit and someone might say that they are too loose."_ So I tried to tighten them up. The initial idea was to try the following setup:

* Use only 1 run, not "best of 5 runs" (although one might argue if this is really "more strict" or "more random").
* Use the same number of loops for each function (by setting the `number` parameter).

See the `stricter_benchmarks.py` file for how to achieve that.

I've used that benchmarking method on a couple of examples in this repository, and the difference was negligible compared to the simple way of benchmarking. But I still had a bigger problem. No matter if I ran the simple or strict benchmarks, each rerun gave me slightly different results. You can try it yourself - run the `python -m timeit ...` command from any of the examples a couple of times, and you will get slightly different results each time. The difference is small (just a few percent), but it's there. Our programs don't run in a vacuum, and whatever other processes I have running on my computer, they will affect the benchmarks.

Then another idea came to my mind - Docker! If I want to run a script in isolation, docker seems to be a good choice. And indeed, it was a good choice! I tried to reproduce my local setup in a docker container by:

* Using a lightweight image with Python 3.10.4
* Mounting the folder to have access to my example scripts
* Running the `python -m timeit ...` command

I ended up with command like this:

```shell
$ docker run -w /home -it -v $(pwd):/home python:3.10.4-alpine python -m timeit -s "from filter_list import test_comprehension" "test_comprehension()"
```

Now when I tried to rerun the benchmark command multiple times, I was either getting the same number or a much smaller difference (around 1%).

So if you want to run the benchmarks in a stricter setup, I can recommend Docker. But for this presentation, the actual numbers don't matter as much as showing which code examples are slower and which are faster. So for the sake of simplicity (and to squeeze in one more example instead of trying to explain some complex benchmarking setup), I stick with "simple benchmarks".

If you know other ways of running objective benchmarks, please let me know!
