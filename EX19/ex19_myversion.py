def students_total(old_students, new_students):
	print "There are %d old students at Leuphana." % old_students
	print "This semester %d new people started at Leuphana." % new_students
	print "In total there are approximately 10.000 people.\n"
	
	
print "There are different ways of calculating these numbers."
print "We can just add the numbers to the function directly."
students_total(8000, 2000)


print "We can give the function direct variables."
amount_of_old_students = 9000
amount_of_new_students = 2500

students_total(amount_of_old_students, amount_of_new_students)

print "Another way to deal with these numbers is math."
students_total(200 + 3000, 400 + 600)