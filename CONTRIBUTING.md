# Contributing

If you want to contribute, take a look at the [issues](https://github.com/Petlja/pygame4skulpt/issues).
Contribution workflow is a standard [fork and pull](https://help.github.com/articles/creating-a-pull-request-from-a-fork/).
General Skulpt contribution tutorial can be found [here](https://github.com/skulpt/skulpt/blob/master/HACKING.md), and the 
coding style guide [here](https://github.com/skulpt/skulpt/blob/master/CONTRIBUTING.md#coding-style-and-conventions).

In addition to your functionality, make sure to add a unit test into the [test](https://github.com/Petlja/pygame4skulpt/tree/master/test) directory. 
If adding a functionality that is to be tested by running an example, you can add a Pygame program that exposes it. 
A good example is [test/tick_clock.py](https://github.com/Petlja/pygame4skulpt/blob/master/test/tick_clock.py). 
Otherwise, you can make use of the ```unittest``` library as in [test/version_test.py](https://github.com/Petlja/pygame4skulpt/blob/master/test/version_test.py). 
You might find useful to run the test using the index page. All you have to do is to run it with a query string representing
the filename of your test. 
~~~
http://localhost:8888/index.html?tick_clock.py
~~~