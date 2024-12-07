import the_other_guy

def run():
    
    # we can get a list of permutations as tuples by providing a set of values
    perms = the_other_guy.list_permutations({1})
    
    assert (1,) in perms, "#1"
    assert len(perms) == 1, "#2"
    
    perms = the_other_guy.list_permutations({1, 2})
    
    assert (1, 2) in perms
    assert (2, 1) in perms
    assert len(perms) == 2
    
    perms = the_other_guy.list_permutations({1, 2, 3})
    
    assert (1, 2, 3) in perms
    assert (1, 3, 2) in perms
    assert (2, 1, 3) in perms
    assert (2, 3, 1) in perms
    assert (3, 1, 2) in perms
    assert (3, 2, 1) in perms
    
    assert(len(perms) == 6)
    
    # you can pass in any objects you want
    perms = the_other_guy.list_permutations({"A", "B"})
    
    assert ("A", "B") in perms
    assert ("B", "A") in perms
    assert len(perms) == 2
    