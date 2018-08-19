def ddg(entry0,entry1,entry2,entry3):
    base_total = 0
    function_total = base_total
    entries = [entry0,entry1,entry2,entry3]
    print('Your starting total number of points is',base_total)

    for entry in entries:
        if entry == 'egg':
            function_total = base_total - base_total
        elif entry == 'duck':
            function_total = base_total + 5
        elif entry == 'goose':
            function_total = base_total + 10
        base_total = function_total
            
    print('Duck, Duck, Goose!')
    print('You entered:',entry0,',',entry1,',',entry2,',',entry3) 
    print('Your have a total of',function_total,'points!')
ddg('duck','duck','egg','goose')