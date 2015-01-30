---

layout: post
title: testing golang with go test
date: 2015-01-31 09:52:11
category: blog

---

You can use `go test` command for testing go packages very easily.

<Br />


file names
------------

For every go source file that you have ( this example `main.go`) you will need a \<name\>_test.go file that contains the tests (`main_test.go` for example).

<Br />

function names
-----------------

The functions within the `<name>_test.go` file will need to start with the keyword `Test` and then have the suffix of a function that you wish to test.

To test a function called `AddNumbers` in main.go, we create a function called `TestAddNumbers` in main_test.go.

<Br />

Imports
---------

We can use the `testing` library to help us out with testing go files, its in the go standard library has a nice [Error()](http://golang.org/pkg/testing/#B.Error) function, that we use to format output.

An example of the output it can generate is below.

    --- FAIL: TestAddNumbers (0.00 seconds)
	main_test.go:13: For Adding 1 + 2 expected 3 got 4
    FAIL
    exit status 1
    FAIL	_/home/dannyla/code/github/go-examples	0.002s

<Br />

Example
--------

main.go

{% gist 49b3be0b08aa0571d27b main.go %}

main_test.go

{% gist 49b3be0b08aa0571d27b main_test.go %}
