# 0.  From Problem Analysis to Data Definitions

- print an error if the user did not give a url and close the program
- otherwise, check if the url is an absolute url py parsing and checking for scheme and netloc
- catch error here, if it is not an abs path print message
- set maxDepth to 3 unless the user passed in sys.argv[2]
- catch invalid input here, must input a positive integer
- call crawl with parameters url, maxdepth, depth=0, and visited
- Base cases: No unvisited links are found or
- maximum recursion depth is reached (default 3, can specify on CLI)
- needs to know what depth is at (kept track of in a parameter)
- Based on the current depth of recursion, print appropriate indentation and the url
- encase all of crawl in a try catch 
- create a request for the url supplied called response
- if response is not a valid response, ignore the link and the recursion continues for the rest of its sibling and parent links
- print the reason the link did not work
- create a beautiful soup html object with the response.text and 'html.parser'
- use html.find_all('a') to create a list of links on the page
- for each link, make sure it is a hyperlink (has 'a' anchor tag and href attribute)
- craete absolute address and print as long as it begins with http
- trim the fragments off by slicing anything after '#'
- check if the address is in visited, if not, call crawl with absoluteURL, maxdepth, depth +1, and visited
- add the absoluteURL to the visited set

# 1.  System Analysis

**Analyze the flow of data throughout the program.  Does the program get input
from the user?  If so, does it come from interactive prompts or from
command-line arguments?  Is data incorporated from a file on the disk, from a
database or from the internet?**

**How is output given?  On the screen in the form of text or graphics?  Are
output files created, and what form do they take?**

**Identify the non-trivial formulas you need to create.  If there aren't any then
state "no formulas" in this section.**

**State what kind of data each desired function consumes and produces.  Formulate
a concise description of what the function computes.  Define a stub that lives
up to the signature.**


# 2.  Functional Examples

**Design a process for obtaining the output from the input.  Consider both *good*
and *bad* inputs.  Find or create examples of both kinds of input.**

**Work out problem examples on paper, on a whiteboard or some other medium that
is *not* your computer.  It is a mistake to begin writing executable code
before you thoroughly understand what form the algorithm(s) must take.**

**Instead, describe components of the system in *"pseudocode"*.  Expect to make
lots of mistakes at this point.  You will find that it is much easier to throw
away pseudocode than real code.**

**Manually work through several examples that illustrate the program's overall
purpose, as well as the purpose of each component of the finished system.  You
will converge on a correct solution much faster if you feel comfortable making
mistakes as you go.**

**This phase involves the use of many levels of abstraction to decompose the
problem into manageable components, and design strategies for implementing each
component.  Components may be functions, modules or classes.**


# 3.  Function Template

**Combine the function stubs written in step #2 with pseudocode from step #3.
Comment out the pseudocode, leaving a valid program that compiles/runs without
errors.  At this stage your program doesn't quite work, but it also doesn't
crash.**


# 4.  Implementation

**This is the only part of the process focused on writing code in your chosen
programming language.**

**One by one translate passages of pseudocode into valid code.  Fill in the gaps
in the function template.  Exploit the purpose statement and the examples.**

**If you were thorough in the previous steps and are familiar with your
programming system this part will go by very quickly and the code will write
itself.**

**When you are learning a new programming language or an unfamiliar library this
phase can be slow and difficult.  As you gain experience with the relevant
technologies you will spend less and less time in this phase of the process.**


# 5.  Testing

**Articulate the examples given in step #2 as tests and ensure that each
function passes all of its tests.  Doing so discovers mistakes.  Tests also
supplement examples in that they help others read and understand the definition
when the need arises—and it will arise for any serious program.**

**As bugs are discovered and fixed, devise new test cases that will detect these
problems should they return.**

**If you didn't come across any bugs (lucky you!) think of a possible flaw and a
test that can be employed to screen for it.**

**At a minimum you should create a document explaining step-by-step how a
non-technical user may manually test your program to satisfy themselves that it
operates correctly.  Explain the entire process starting how to launch the
program, what inputs they should give and what results they should see at every
step.  Provide test cases of good and bad inputs to catch both false positives
and false negatives.  Any deviation from the expected outputs are errors.**

**The ideal is to write an automated test to avoid all manual labor beyond
launching the test.**
