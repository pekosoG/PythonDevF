
my_set= {1,3}

def add_element_to_set():
    my_set.add(2)
    print 'Element added: ',my_set

    my_set.update([2,3,4])
    print 'Several elements added:',my_set

    my_set.update([4,5],{1,6,8})
    print 'set updatet uding list',my_set

    my_set.discard(4)
    print 'set element discard', my_set

    my_set.remove(6)
    print 'set element removed',my_set

    try :
        my_set.remove(11) #Exception!
        print 'set unexisting element remove',my_set
    except :
        print 'remove unexisting set element throws exception'

    print 'poping an element:',my_set.pop()

    print 'clear on set: ',my_set.clear()

add_element_to_set()