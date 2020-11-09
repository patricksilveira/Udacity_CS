    Jump to content
    Email for accessibility support

Lesson 6: Problem Set

1. Quiz: Udacify
2. Quiz: Proc
3. Quiz: Median
4. Quiz: Blastoff
5. Quiz: Finish

    6. Quiz: Find Last

Toggle Sidebar
Udacify
# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter

# print udacify('dacians')

# the output should be the string 'Udacians'



def udacify (text):
    text = "U" + text[:]
    return text



# Remove the hash, #, from infront of print to test your code.

print udacify('dacians')
#>>> Udacians

print udacify('turn')
#>>> Uturn

print udacify('boat')
#>>> Uboat

View Intro

At this point, the programming problems are getting tough enough that I encourage you to install your own Python interpreter so you'll have a better environment to work in than using the web interface. If you don't want to install Python on your own machine, you can still do everything using the Udacity web site, but you'll be able to run code faster and get more immediate results if you run a Python interpreter on your own machine.

What you need to do to get Python set up on your own machine depends on if you are running Windows, Mac OS, Linux, or something else. You can download Python from python.org. Note that the class is using version 2.7 of Python, so make sure to download that version. Some things are not compatible with Version 3.X of Python.

For more help setting up Python on your platform, Chad Black wrote a great guide to setting up Python on different platforms.
