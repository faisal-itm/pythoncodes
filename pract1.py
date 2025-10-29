def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    raceres= list(racers)
    racerss =  raceres.reverse()

    return racerss

racebrs = ['khalil', 'ahmad', 'khan', 'adil', 'ali']\
rrr= racebrs.reverse()()
print(rrr)
a = purple_shell(racebrs)
print(a)