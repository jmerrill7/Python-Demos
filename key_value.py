dictionary_name = {'item_1':1,'item_2':2,'item_3':3 }
print dictionary_name['item_1']

epic_programmer_dict = {'Tim Lee' :'tbl@gmail.com',
                        'Guido van Rossum' :'gvr@gmail.com',
                        'Linus Torvalds' :'lt@gmail.com'}

print epic_programmer_dict

#get tim's email

print epic_programmer_dict['Tim Lee']

#change Tim's email

epic_programmer_dict['Tim Lee'] = 'Tim@gmail.com'
print 'new email for tim: ' + epic_programmer_dict['Tim Lee']

#add more programmers

epic_programmer_dict['Larry Page'] = 'lp@gmail.com'

print epic_programmer_dict
epic_programmer_dict['Me'] = 'jamesmerrill7@gmail.com'
epic_programmer_dict['Sergy Brin'] = 'sb@gmail.com'

print epic_programmer_dict

#delete entry

del epic_programmer_dict['Larry Page']

print epic_programmer_dict
