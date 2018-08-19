def ddg(entry0,entry1,entry2,entry3):
    base_total = 0
    function_total = base_total
    print('Your starting total number of points is',base_total,'.')

    if entry0 == 'egg':
        function_total = base_total - base_total
    elif entry0 == 'duck':
        function_total = base_total + 5
    elif entry0 == 'goose':
        function_total = base_total + 10
    
    if entry1 == 'egg':
        function_total = function_total - function_total
    elif entry1 == 'duck':
        function_total = function_total + 5
    elif entry1 == 'goose':
        function_total = function_total + 10

    if entry2 == 'egg':
        function_total = function_total - function_total
    elif entry2 == 'duck':
        function_total = function_total + 5
    elif entry2 == 'goose':
        function_total = function_total + 10

    if entry3 == 'egg':
        function_total = function_total - function_total
    elif entry3 == 'duck':
        function_total = function_total + 5
    elif entry3 == 'goose':
        function_total = function_total + 10
            
    print('Duck, Duck, Goose! Your have a total of',function_total,'points!')
ddg('goose','goose','duck','duck')