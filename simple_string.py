name = "Guido"
print name [0]
print name.upper ()
print name.lower ()
print name.capitalize ()

date = "11/12/2013"

# go through string and split
# where there is a '/'

date_manip = date.split('/')

#show the outcome

print date_manip [0]
print date_manip [1]
print date_manip [2]

print 'Month: ' + date_manip[0]
print 'Day: ' + date_manip[1]
print 'Year: ' + date_manip[2]

print ('Month: ' + date_manip[0] +
       '. Day: ' + date_manip[1] +
       '. Year: ' + date_manip[2])
