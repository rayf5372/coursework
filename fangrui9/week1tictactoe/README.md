# tictactoe-text

This a tic-tac-toe game with a text UI that you run in a terminal. 

The main program is in `src/TextTTTGame.java`, but there are a number of other Java source files which it depends on to work.
In the Project pane to the left, expand the folder tree until you find `TextTTTGame`.
Double-click on it to open it. Notice the tab name includes `.java`.
In the Project pane, the `.java` file extensions are hidden.

## Your task

**Fix all of the TODOs in the Java files.**

If you haven't used it before, the TODO Tool Window is a great way to navigate to each of the TODOs in this assignment.
In the `View` menu, select `Tool Windows`, then `TODO` should be the last one listed. Click it and the TODO Tool Window will open.

The code is broken: we've removed a few necessary parts.
You'll be fixing it, figuring out what's missing and writing a few lines of Java code.
The point here is to give you practice with Java and git.

There are a few places where we have removed code.
Anywhere we've done this, we've left comments that look like this:
```
// TODO:
```
Often we'll tell you some information about the missing code.

IntelliJ will also give you clues: what are the error messages?
Is a variable declaration missing, and if so what should its initial value be?
Is there a syntax error?

Once you've fixed it all, you will play the game in the frame at the bottom of IntelliJ. You'll see something like this:
```
/Users/pgries/Library/Java/JavaVirtualMachines/corretto-11.0.19/Contents/Home/bin/java -Dvisualgc.id=112413596497458 -javaagent:/Applications/IntelliJ IDEA.app/Contents/lib/idea_rt.jar=61526:/Applications/IntelliJ IDEA.app/Contents/bin -Dfile.encoding=UTF-8 -classpath /Users/pgries/IdeaProjects/tictactoe-text/out/production/tictactoe-text TextTTTGame
```
That beastly thing is the command that IntelliJ uses to run the program. It may look a bit different on your computer.

Then the game will start:
```
To exit the game at any time, type '9'. To start, type any other number.
```

A full game might look something like below:

```
To exit the game at any time, type '9'. To start, type any other number.
1
- - - 
- - - 
- - - 
Player X, enter your move by typing the row then a space then column number. Your options are 0, 1, or 2.
1 1
- - - 
- X - 
- - - 
Player O, enter your move by typing the row then a space then column number. Your options are 0, 1, or 2.
0 0
O - - 
- X - 
- - - 
Player X, enter your move by typing the row then a space then column number. Your options are 0, 1, or 2.
1 0
O - - 
X X - 
- - - 
Player O, enter your move by typing the row then a space then column number. Your options are 0, 1, or 2.
1 2
O - - 
X X O 
- - - 
Player X, enter your move by typing the row then a space then column number. Your options are 0, 1, or 2.
2 1
O - - 
X X O 
- X - 
Player O, enter your move by typing the row then a space then column number. Your options are 0, 1, or 2.
0 2
O - O 
X X O 
- X - 
Player X, enter your move by typing the row then a space then column number. Your options are 0, 1, or 2.
0 1
Player X wins!
O X O 
X X O 
- X - 
Player X wins!

Process finished with exit code 0
```

The last line indicates that the program terminated without error (exit code 0 indicates this).

## Submission
Once you have fixed all of the TODOs in the code, you are ready to hand in your work!

Submit your code to MarkUs where you can run the self tests to confirm your code works.
There are no hidden tests for this assignment.

For this assignment, we encourage you to practice using git to submit, but we have left the file upload option available.
For future assignments, like `week1git` this week, you **must** submit using git.

### After you finish [not for credit]
We encourage you to go back and look at how the code is organized. Think about how the various
classes interact. Where are instances of each class created? What relationships exist between each class?

One way to do this is to generate a UML class diagram.
Conveniently, IntelliJ Ultimate can do this for us if we right-click the `src` directory
and choose `Diagrams -> Show Diagrams` near the bottom of the context menu. You might
need to zoom in a bit and toggle some options to make it easier to focus in on the classes
and their features which are of interest to you.

As the term goes, we'll talk a lot more about design, but hopefully this little exercise
gives you a bit of a preview of what kind of code we'll be working with, as well as ways we can visualize it!
