Last login: Sat Oct 22 21:22:21 on ttys000
Hannas-MBP:~ Hanna$ pwd
/Users/Hanna
Hannas-MBP:~ Hanna$ ls
Desktop		Dropbox		Music		ex1-14.py
Documents	Library		Pictures	exercise
Downloads	Movies		Public		miniconda2
Hannas-MBP:~ Hanna$ cd documents
Hannas-MBP:documents Hanna$ ls
Arduino					Holz.mp4
Atom					Juni 2016 Ausgaben.xlsx
Ausgaben Juli.xlsx			Outtakes.mp4
BaföG					Set Fire to the Rain - Adele Cover.mov
Die Mädels - Kinder Filmchen.mp4	ex1-14.py
Hannas-MBP:documents Hanna$ python ex1-14.py
Hello World!
Hello Again
I like typing this.
This is fun.
Yay! Printing.
I'd much rather you 'not'.
I "said" do not touch this.
Hannas-MBP:documents Hanna$ python ex1-14.py
Hello World!
Hello Again
I like typing this.
This is fun.
Yay! Printing.
I'd much rather you 'not'.
I "said" do not touch this.
Do you even listen to me?
Hannas-MBP:documents Hanna$ python ex1-14.py
Hello World!
Hannas-MBP:documents Hanna$ python ex1-14.py
Hello World!
Hannas-MBP:documents Hanna$ python ex1-14.py
Hello World!
I like typing this.
This is fun.
Hannas-MBP:documents Hanna$ cd ~
Hannas-MBP:~ Hanna$ pwd
/Users/Hanna
Hannas-MBP:~ Hanna$ ls
Desktop		Dropbox		Music		ex1-14.py
Documents	Library		Pictures	exercise
Downloads	Movies		Public		miniconda2
Hannas-MBP:~ Hanna$ documents
-bash: documents: command not found
Hannas-MBP:~ Hanna$ cd documents
Hannas-MBP:documents Hanna$ ls
Arduino					Juni 2016 Ausgaben.xlsx
Atom					Outtakes.mp4
Ausgaben Juli.xlsx			Set Fire to the Rain - Adele Cover.mov
BaföG					ex1-14.py
Die Mädels - Kinder Filmchen.mp4	ex2.py
Holz.mp4
Hannas-MBP:documents Hanna$ python ex2.py
I could have code like this.
This will run.
Hannas-MBP:documents Hanna$ pyhton ex3.py
-bash: pyhton: command not found
Hannas-MBP:documents Hanna$ cd documents
-bash: cd: documents: No such file or directory
Hannas-MBP:documents Hanna$ cd ~
Hannas-MBP:~ Hanna$ pwd
/Users/Hanna
Hannas-MBP:~ Hanna$ ls
Desktop		Dropbox		Music		ex1-14.py
Documents	Library		Pictures	exercise
Downloads	Movies		Public		miniconda2
Hannas-MBP:~ Hanna$ cd documents
Hannas-MBP:documents Hanna$ ls
Arduino					Juni 2016 Ausgaben.xlsx
Atom					Outtakes.mp4
Ausgaben Juli.xlsx			Set Fire to the Rain - Adele Cover.mov
BaföG					ex1-14.py
Die Mädels - Kinder Filmchen.mp4	ex2.py
Holz.mp4				ex3.py
Hannas-MBP:documents Hanna$ python ex3.py
I will count my chickens:
Hens 30
Roosters 97
Now I will count the eggs:
8
Is it true that 3 + 2 < 5 - 7?
False
What is 3 + 2? 5
What is 5 - 7? -2
Oh that's why it's False.
How about some more.
Is it greater? True
Is it greater or equal? True
Is it less or equal? False
Hannas-MBP:documents Hanna$ 
Last login: Sun Oct 23 10:04:56 on ttys000
Hannas-MacBook-Pro:~ Hanna$ ls
Desktop		Dropbox		Music		ex1-14.py
Documents	Library		Pictures	exercise
Downloads	Movies		Public		miniconda2
Hannas-MacBook-Pro:~ Hanna$ cd documents
Hannas-MacBook-Pro:documents Hanna$ ls
Arduino					Holz.mp4
Atom					Juni 2016 Ausgaben.xlsx
Ausgaben Juli.xlsx			Outtakes.mp4
BaföG					Python Exercises
Die Mädels - Kinder Filmchen.mp4	Set Fire to the Rain - Adele Cover.mov
Hannas-MacBook-Pro:documents Hanna$ cd python exercises
-bash: cd: python: No such file or directory
Hannas-MacBook-Pro:documents Hanna$ cd Python Exercises
-bash: cd: Python: No such file or directory
Hannas-MacBook-Pro:documents Hanna$ python ex3-mycalculation.py
python: can't open file 'ex3-mycalculation.py': [Errno 2] No such file or directory
Hannas-MacBook-Pro:documents Hanna$ cd bafög
Hannas-MacBook-Pro:bafög Hanna$ cd ..
Hannas-MacBook-Pro:documents Hanna$ cd python exercises
-bash: cd: python: No such file or directory
Hannas-MacBook-Pro:documents Hanna$ cd atom
Hannas-MacBook-Pro:atom Hanna$ ls
Miniconda2-latest-MacOSX-x86_64.sh
Hannas-MacBook-Pro:atom Hanna$ cd ..
Hannas-MacBook-Pro:documents Hanna$ ls
Arduino					Holz.mp4
Atom					Juni 2016 Ausgaben.xlsx
Ausgaben Juli.xlsx			LPTHW Exercises
BaföG					Outtakes.mp4
Die Mädels - Kinder Filmchen.mp4	Set Fire to the Rain - Adele Cover.mov
Hannas-MacBook-Pro:documents Hanna$ cd lpthw exercises
-bash: cd: lpthw: No such file or directory
Hannas-MacBook-Pro:documents Hanna$ python juni 2014 ausgaben.xlsx
python: can't open file 'juni': [Errno 2] No such file or directory
Hannas-MacBook-Pro:documents Hanna$ ls
Arduino					Holz.mp4
Atom					Juni 2016 Ausgaben.xlsx
Ausgaben Juli.xlsx			LPTHW-Exercises
BaföG					Outtakes.mp4
Die Mädels - Kinder Filmchen.mp4	Set Fire to the Rain - Adele Cover.mov
Hannas-MacBook-Pro:documents Hanna$ cd lpthw-exercises
Hannas-MacBook-Pro:lpthw-exercises Hanna$ ls
ex1-14.py		ex2.py			ex3.py
ex1.py			ex3-mycalculation.py
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex3-mycalculation.py
  File "ex3-mycalculation.py", line 11
    print, (1,5 * 2 + 1,5) + (1,5 * 2) + ((6,75 + 3,5) / 2) + (3,5 / 2)
         ^
SyntaxError: invalid syntax
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex3-mycalculation.py
  File "ex3-mycalculation.py", line 11
    print, 4,5 + 3 + 5,125 + 1,75
         ^
SyntaxError: invalid syntax
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex3-mycalculation.py
For how many hours a week do I have classes at university (apprx)?
Monday 0
Tuesday 1 11 5
Wednesday 1 10
Thursday
Traceback (most recent call last):
  File "ex3-mycalculation.py", line 6, in <module>
    print "Thursday", (6,75 + 3,5) / 2
TypeError: unsupported operand type(s) for /: 'tuple' and 'int'
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex3-mycalculation.py
For how many hours a week do I have classes at university (apprx)?
Monday 0
Tuesday 4.5
Wednesday 3.0
Thursday 5.125
Friday 1.75
Weekends occasionally
All days added up: 14.375
Hannas-MacBook-Pro:lpthw-exercises Hanna$ ls
ex1-14.py		ex2.py			ex3.py
ex1.py			ex3-mycalculation.py	ex4.py
Hannas-MacBook-Pro:lpthw-exercises Hanna$ pyhton ex4.py
-bash: pyhton: command not found
Hannas-MacBook-Pro:lpthw-exercises Hanna$ cd ~
Hannas-MacBook-Pro:~ Hanna$ ls
Desktop		Dropbox		Music		ex1-14.py
Documents	Library		Pictures	exercise
Downloads	Movies		Public		miniconda2
Hannas-MacBook-Pro:~ Hanna$ cd documents
Hannas-MacBook-Pro:documents Hanna$ ls
Arduino					Holz.mp4
Atom					Juni 2016 Ausgaben.xlsx
Ausgaben Juli.xlsx			LPTHW-Exercises
BaföG					Outtakes.mp4
Die Mädels - Kinder Filmchen.mp4	Set Fire to the Rain - Adele Cover.mov
Hannas-MacBook-Pro:documents Hanna$ cd lpthw-exercises
Hannas-MacBook-Pro:lpthw-exercises Hanna$ ls
ex1-14.py		ex2.py			ex3.py
ex1.py			ex3-mycalculation.py	ex4.py
Hannas-MacBook-Pro:lpthw-exercises Hanna$ pyhton ex4.py
-bash: pyhton: command not found
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex4.py
  File "ex4.py", line 7
    carpool_capacity = cars driven * space_in_a_car
                                 ^
SyntaxError: invalid syntax
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex4.py
There are 100 cars available.
There are only 30 drivers available.
There will be 70 empty cars today.
We have 90 to carpool today.
We need to put about 3 in each car.
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex4.py
There are 100 cars available.
There are only 30 drivers available.
There will be 70 empty cars today.
We have 90 to carpool today.
We need to put about 3 in each car.
Hannas-MacBook-Pro:lpthw-exercises Hanna$ 
Hannas-MacBook-Pro:lpthw-exercises Hanna$ ls
ex1-14.py		ex2.py			ex4.py
ex1-14_2.py		ex3-mycalculation.py	ex5.py
ex1.py			ex3.py
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex5.py
  File "ex5.py", line 11
    print "He's %s pounds heavy." % my weight
                                            ^
SyntaxError: invalid syntax
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex5.py
Let's talk about Zed A. Shaw.
He's 74 inches tall.
He's 180 pounds heavy.
Actually that's not too heavy.
He's got Blue eyes and Brown hair.
His teeth are usually White depending on the coffee.
Traceback (most recent call last):
  File "ex5.py", line 17, in <module>
    print "If I add %d, %d and %d I get %d." % (my_age, my_heigth, my_weight, my_age + my_height + my_weight)
NameError: name 'my_heigth' is not defined
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex5.py
Let's talk about Zed A. Shaw.
He's 74 inches tall.
He's 180 pounds heavy.
Actually that's not too heavy.
He's got Blue eyes and Brown hair.
His teeth are usually White depending on the coffee.
If I add 35, 74 and 180 I get 289.
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex4.py
There are 100 cars available.
There are only 30 drivers available.
There will be 70 empty cars today.
We have 90 to carpool today.
We need to put about 3 in each car.
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex5.py
Let's talk about Zed A. Shaw.
He's 74 inches tall.
He's 180 pounds heavy.
Actually that's not too heavy.
He's got Blue eyes and Brown hair.
His teeth are usually White depending on the coffee.
If I add 35, 74 and 180 I get 289.
Hannas-MacBook-Pro:lpthw-exercises Hanna$ ls
ex1-14.py		ex2.py			ex4.py
ex1-14_2.py		ex3-mycalculation.py	ex5.py
ex1.py			ex3.py			ex6.py
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex6.py
There are 10 types of people.
Those who know binary and those who don't.
I said: 'There are 10 types of people.'.
I also said: 'Those who know binary and those who don't.'.
Isn't that joke so funny?! False
This is the left side of...a string with a right side.
Hannas-MacBook-Pro:lpthw-exercises Hanna$ ls
ex1-14.py		ex3-mycalculation.py	ex6.py
ex1-14_2.py		ex3.py			ex7.py
ex1.py			ex4.py
ex2.py			ex5.py
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex7.py
Mary had a little lamb.
Traceback (most recent call last):
  File "ex7.py", line 2, in <module>
    print "Its fleece was white as &s." % 'snow'
TypeError: not all arguments converted during string formatting
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex7.py
Mary had a little lamb.
Its fleece was white as snow.
And everywhere that Mary went.
..........
Cheese Burger
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex7.py
Mary had a little lamb.
Its fleece was white as snow.
And everywhere that Mary went.
..........
Cheese
Burger
Hannas-MacBook-Pro:lpthw-exercises Hanna$ ls
ex1-14.py		ex3-mycalculation.py	ex6.py
ex1-14_2.py		ex3.py			ex7.py
ex1.py			ex4.py			ex8.py
ex2.py			ex5.py
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex8.py
1 2 3 4
'one' 'two' 'three' 'four'
True False False True
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
Traceback (most recent call last):
  File "ex8.py", line 10, in <module>
    "But it didn't sing."
TypeError: not enough arguments for format string
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex8.py
1 2 3 4
'one' 'two' 'three' 'four'
True False False True
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
Hannas-MacBook-Pro:lpthw-exercises Hanna$ ls
ex1-14.py		ex3-mycalculation.py	ex6.py
ex1-14_2.py		ex3.py			ex7.py
ex1.py			ex4.py			ex8.py
ex2.py			ex5.py			ex9.py
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex9.py
Here are the days:  Mon Tue Wed Thu Fri Sat Sun
Here are the months:  Jan/nFeb/nMar/nApr/nMay/nJun/nJul/nAug

There is something going on here.
With three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.

Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex9.py
Here are the days:  Mon Tue Wed Thu Fri Sat Sun
Here are the months:  Jan
Feb
Mar
Apr
May
Jun
Jul
Aug

There is something going on here.
With three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.

Hannas-MacBook-Pro:lpthw-exercises Hanna$ ls
ex1-14.py		ex3-mycalculation.py	ex7.py
ex1-14_2.py		ex3.py			ex8.py
ex1.py			ex4.py			ex9.py
ex10.py			ex5.py
ex2.py			ex6.py
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex9.py
Here are the days:  Mon Tue Wed Thu Fri Sat Sun
Here are the months:  Jan
Feb
Mar
Apr
May
Jun
Jul
Aug

There is something going on here.
With three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.

Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex10.py
	I'm tabbed in.
I'm split
on a line.
I'm \ a \ cat.

I'll do a list:
	* Cat food
	* Fishies
# 	* Catnip
	* Grass

Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex10.py
	I'm tabbed in.
I'm split
on a line.
I'm \ a \ cat.

I'll do a list:
	* Cat food
	* Fishies
	* Catnip
	* Grass

Hannas-MacBook-Pro:lpthw-exercises Hanna$ ls
ex1-14.py		ex3-mycalculation.py	ex7.py
ex1-14_2.py		ex3.py			ex8.py
ex1.py			ex4.py			ex9.py
ex10.py			ex5.py
ex2.py			ex6.py
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex10.py
	I'm tabbed in.
I'm split
on a line.
I'm \ a \ cat.

I'll do a list:
	* Cat food
	* Fishies
	* Catnip
	* Grass

|
-
|
\
|
|
|
-
/
\
/
|
\
-
/
-
-|
|
\|
//
-/
|


Last login: Sun Oct 23 10:20:36 on ttys000
Hannas-MacBook-Pro:~ Hanna$ pwd
/Users/Hanna
Hannas-MacBook-Pro:~ Hanna$ ls
Desktop		Dropbox		Music		ex1-14.py
Documents	Library		Pictures	exercise
Downloads	Movies		Public		miniconda2
Hannas-MacBook-Pro:~ Hanna$ cd documents
Hannas-MacBook-Pro:documents Hanna$ ls
Arduino					Holz.mp4
Atom					Juni 2016 Ausgaben.xlsx
Ausgaben Juli.xlsx			LPTHW-Exercises
BaföG					Outtakes.mp4
Die Mädels - Kinder Filmchen.mp4	Set Fire to the Rain - Adele Cover.mov
Hannas-MacBook-Pro:documents Hanna$ cd lpthw-exercises
Hannas-MacBook-Pro:lpthw-exercises Hanna$ ls
ex1-14.py		ex11.py			ex5.py
ex1-14_2.py		ex2.py			ex6.py
ex1-14_3.py		ex3-mycalculation.py	ex7.py
ex1.py			ex3.py			ex8.py
ex10.py			ex4.py			ex9.py
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex11.py
How old are you? 21
How tall are you? 1.77cm
How much do you weight? 63kg
So, you're '21' old, '1.77cm' tall and '63kg' heavy.
Hannas-MacBook-Pro:lpthw-exercises Hanna$ ls
ex1-14.py		ex11.py			ex6.py
ex1-14_2.py		ex2.py			ex7.py
ex1-14_3.py		ex3-mycalculation.py	ex8.py
ex1.py			ex3.py			ex9.py
ex10.py			ex4.py
ex11-myquestions.py	ex5.py
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex11-myquestions.py 
What is your name? Hanna
What is your favourite colour? purple
Would you like to have some apple crumble? Yes
What are you studying? DigitalMedia
Traceback (most recent call last):
  File "ex11-myquestions.py", line 14, in <module>
    """ % (name, colour, subject)
ValueError: unsupported format character 't' (0x74) at index 135
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex11-myquestions.py 
What is your name? Hanna
What is your favourite colour? purple
Would you like to have some apple crumble? Yes
What are you studying? Digi
Hello 'Hanna' I like the colour 'purple', too.
Good decision, the apple crumble is indeed very good!
Traceback (most recent call last):
  File "ex11-myquestions.py", line 13, in <module>
    print "I wish you all the best for studying r% this semester." % subject
ValueError: unsupported format character 't' (0x74) at index 40
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex11-myquestions.py 
What is your name? Hanna
What is your favourite colour? p
Would you like to have some apple crumble? y
What are you studying? digi
Hello 'Hanna' I like the colour 'p', too.
Good decision, the apple crumble is indeed very good!
I wish you all the best for studying 'digi' this semester.
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex11-myquestions.py 
What is your name? Hanna
What is your favourite colour? red
Would you like to have some apple crumble? yes
What are you studying? music 
Hello 'Hanna' I like the colour 'red', too.
Good decision, the apple crumble is indeed very good!
I wish you all the best for studying 'music' this semester.
Hannas-MacBook-Pro:lpthw-exercises Hanna$ ls
ex1-14.py		ex11.py			ex5.py
ex1-14_2.py		ex12.py			ex6.py
ex1-14_3.py		ex2.py			ex7.py
ex1.py			ex3-mycalculation.py	ex8.py
ex10.py			ex3.py			ex9.py
ex11-myquestions.py	ex4.py
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex12.py 
How old are you? 21
How tall are you? 1.77cm
How much do you weigh? 63kg
So, you're '21' old, '1.77cm' tall and '63kg' heavy.
Hannas-MacBook-Pro:lpthw-exercises Hanna$ pydoc raw_input

Hannas-MacBook-Pro:lpthw-exercises Hanna$ pydoc open

Hannas-MacBook-Pro:lpthw-exercises Hanna$ pxdoc file
-bash: pxdoc: command not found
Hannas-MacBook-Pro:lpthw-exercises Hanna$ pydoc file

Hannas-MacBook-Pro:lpthw-exercises Hanna$ pydoc os

Hannas-MacBook-Pro:lpthw-exercises Hanna$ pydoc sys

Hannas-MacBook-Pro:lpthw-exercises Hanna$ ls
ex1-14.py		ex11.py			ex5.py
ex1-14_2.py		ex12.py			ex6.py
ex1-14_3.py		ex13.py			ex7.py
ex1-14_4.py		ex2.py			ex8.py
ex1.py			ex3-mycalculation.py	ex9.py
ex10.py			ex3.py
ex11-myquestions.py	ex4.py
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex13.py first 2nd 3rd
The script is called: ex13.py
Your first varibale is: first
Your second variable is: 2nd
Your third variable is: 3rd
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex13.py stuff things that
The script is called: ex13.py
Your first varibale is: stuff
Your second variable is: things
Your third variable is: that
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex13.py apple orange grapefruit
The script is called: ex13.py
Your first varibale is: apple
Your second variable is: orange
Your third variable is: grapefruit
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex13.py hanna marie luise marlene
Traceback (most recent call last):
  File "ex13.py", line 3, in <module>
    script, first, second, third = argv
ValueError: too many values to unpack
Hannas-MacBook-Pro:lpthw-exercises Hanna$ ls
ex1-14.py		ex11.py			ex4.py
ex1-14_2.py		ex12.py			ex5.py
ex1-14_3.py		ex13-mygo.py		ex6.py
ex1-14_4.py		ex13.py			ex7.py
ex1.py			ex2.py			ex8.py
ex10.py			ex3-mycalculation.py	ex9.py
ex11-myquestions.py	ex3.py
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex13-mygo.py 
  File "ex13-mygo.py", line 14
    print "The person using this is %r years old.", % age
                                                    ^
SyntaxError: invalid syntax
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex13-mygo.py 
  File "ex13-mygo.py", line 15
    print "The person using this is %s years old.", % age
                                                    ^
SyntaxError: invalid syntax
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex13-mygo.py 
What is your name? Hanna
How old are you? 21
Are you a man or a female? female
Traceback (most recent call last):
  File "ex13-mygo.py", line 11, in <module>
    script, name, age, gender = argv
ValueError: need more than 1 value to unpack
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex13-mygo.py name age gender
What is your name? Hanna
How old are you? 21
Are you a man or a female? f 
The script you are working with is called: ex13-mygo.py
The person using Python is called: name
The person using this is age
The person using this is a gender
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex13-mygo.py 
What is your name? H
How old are you? 21
Are you a man or a female? f

Traceback (most recent call last):
  File "ex13-mygo.py", line 12, in <module>
    script, name, age, gender = argv
ValueError: need more than 0 values to unpack
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex13-mygo.py hanna 21 female
What is your name? Hanna
How old are you? 21
Are you a man or a female? female

Traceback (most recent call last):
  File "ex13-mygo.py", line 12, in <module>
    script, name, age, gender = argv
ValueError: need more than 0 values to unpack
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex13-mygo.py 
What is your name? q
How old are you? q
Are you a man or a female? q
Traceback (most recent call last):
  File "ex13-mygo.py", line 11, in <module>
    script, name, age, gender = argv
ValueError: need more than 1 value to unpack
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex13-mygo.py hanna 21 female
What is your name? H
How old are you? 21
Are you a man or a female? f
The script you are working with is called: ex13-mygo.py
The person using Python is called: hanna
The person using this is 21
The person using this is a female
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex14.py hanna
  File "ex14.py", line 11
    print "Where do you live %s?" $ user_name
                                  ^
SyntaxError: invalid syntax
Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex14.py hanna
Hi hanna, I'm the ex14.py script.
I'd like to ask you a few questions.
Do you like me hanna?
> Yes
Where do you live hanna?
> nordstetten
What kind of computer do you have?
> macbook

Alright, so you said 'Yes' about liking me.
You live in 'nordstetten'. Not sure where that is.
And you have a 'macbook' computer. Nice.

Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex14.py hanna
Hi hanna, I'm the ex14.py script.
I'd like to ask you a few questions.
Do you like me hanna?
> Yes
Where do you live hanna?
> nordstetten
What kind of computer do you have?
> mac

Alright, so you said 'Yes' about liking me.
You live in 'nordstetten'. Not sure where that is.
And you have a 'mac' computer. Nice.

Hannas-MacBook-Pro:lpthw-exercises Hanna$ python ex14.py hanna
Hi hanna, I'm the ex14.py script.
I'd like to ask you a few questions.
Do you like me hanna?
> Yes
Where do you live hanna?
> nordstetten
What kind of computer do you have?
> mac
Are you a computer freak?
> no

Alright, so you said 'Yes' about liking me.
You live in 'nordstetten'. Not sure where that is.
And you have a 'mac' computer. Nice.
Oh that's funny. So you are a freak? - 'no'. Just like me.

Hannas-MacBook-Pro:lpthw-exercises Hanna$ cd ~
Hannas-MacBook-Pro:~ Hanna$ pwd
/Users/Hanna
Hannas-MacBook-Pro:~ Hanna$ exit
logout
Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.

[Prozess beendet]

