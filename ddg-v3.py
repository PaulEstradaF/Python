def ddg(entry0,entry1,entry2,entry3):
    base_total = 0
    function_total = base_total
    entries = [entry0,entry1,entry2,entry3]
    allowed_entries = ['egg','duck','goose']
    print('Your starting total number of points is',base_total)
    valid_entry = True

    while valid_entry == True:
        try:
            for entry in entries:
                if str.lower(entry) not in allowed_entries:
                    print('Sorry!',str.capitalize(entry),'is not a valid entry. Please enter Egg, Duck, or Goose only.')
                    valid_entry = False
                    break
                elif str.lower(entry) == 'egg':
                    function_total = base_total - base_total
                elif str.lower(entry) == 'duck':
                    function_total = base_total + 5
                elif str.lower(entry) == 'goose':
                    function_total = base_total + 10
                base_total = function_total
                valid_entry = True
        finally:
            if valid_entry == True:
                print('Duck, Duck, Goose!')
                print('You entered:',str.capitalize(entry0),',',str.capitalize(entry1),',', \
                      str.capitalize(entry2),',',str.capitalize(entry3)) 
                print('You have a total of',function_total,'points!')
                break
	
ddg('Egg','Duck','eGG','goOse')
