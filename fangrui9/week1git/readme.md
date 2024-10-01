# Coding Homework for Week 1

This homework will have you demonstrate that:

- you are able to add, commit, and push code using git
- you are able to use Java to solve small coding problems

In lab this week, you worked on writing `Multiples.java` and `Reduce.java`.

To submit:
- `Multiples.java`
- `Reduce.java`

## Your Tasks

You will now be tasked with ensuring the two methods you wrote are
fully correct, and you will get some extra practice working with git.

Tip: If you had trouble implementing these methods in Java, you might start
by first implementing them in Python, then translating your code into Java line-by-line.
As you become more comfortable with the syntax of Java, it will get easier to directly write
your code.

## Task 1: `Multiples.java`

1. Copy over your `Multiples.java` from lab. When prompted by IntelliJ,
tell it that you want to add the file to your git repo (or manually add the file later).

2. You will now modify the main method so that we will be able to test it more conveniently.
While we could check that the string it prints is the right value, it would be nice to convert
the method into a method which returns the value instead of printing it.
You can do this by changing the return type of the method, which is currently `void`.
Change the method to return an `int`.

3. Modify the body of the `main` method so that it correctly returns the result instead of printing it.

**Note: since this method now returns an `int`, you will notice that you can no longer run this file, since only a `public static void main` (psvm) method can be directly run as a "main" method in Java. If you wish to still be able to run your file, you can create a new psvm method. This is optional, but might help you double check that your code is correct.**

4. Modify `main` so that it takes three parameters — first an integer `n`, then an integer `a`,
and then an integer `b`. These will all be positive integers. It currently takes `String [] args` as its
one parameter.

5. Generalize the code so that it uses `n` in place of where 1000 was previously used, `a` where 3 was used,
and `b` where 5 was used. Note: depending on your implementation, you may need to add code
to make it work when `a == b`. 

6. Add, commit, and then push your code to MarkUs. Log into MarkUs and ensure you see your pushed files,
then run the self test to confirm this code is correct.

### Task 2: Overloading `main`

Unlike Python, Java allows us to define multiple methods with the same name,
but with different numbers and types of parameters. This is called **overloading** and is discussed in the readings.
Think about how overloading might be useful when writing code in certain situations.

For example, in step 5 when we generalized our code, we could have also included an alternative main method
which takes no arguments and simply calls our current main method with the default values from the original
problem (1000, 3, and 5). (This might remind you of some recursive code you have written in the past where your public method's body just calls a private helper to do the work for it.)

1. Add this overloaded version of your main method which was described above. (i.e., write a method called `main` which takes no arguments and just calls your `main` from Task 1 to solve the original multiples problem for a=3 and b=5.

Thinking back to Python, this would allow us to accomplish the same thing that Python's syntax for default
parameters does for us:

```python
def main(n: int = 1000, a: int = 3, b: int = 5) -> int:
    # logic of the Multiples problem
```

As you learn more languages, it can be interesting to observe how they often provide similar functionality with different syntax.

## Task 3: `Reduce.java`

Repeat the above steps from Task 1 (not Task 2!), but for `Reduce.java`. In step 5, the method should only take one integer, `n`,
as a parameter, with the generalization being to use `n` where 100 was previously used.
Once you complete these steps, your code should pass all the tests on MarkUs.

**Reminder: There are no hidden tests, so if you pass the tests on MarkUs, then you will earn full
marks.**

And that's all for `week1git`! Next week you'll further explore writing more interesting classes in Java
rather than these static methods, which hopefully felt quite similar to the kind of standalone functions
you used to write when first learning to write Python code.

## Extra to think about [not for credit]

What is the runtime of your solution for the Multiples problem, in terms of `n`?
We aren't testing your code for efficiency in this assignment, but if your solution is linear in `n`, then
we encourage you to think about how it could be made more efficient. This is good practice for
these kinds of technical interview questions!
