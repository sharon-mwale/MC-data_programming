from cross_peer import squares, unitlist, units, peers

def test():
    "A set of units tests."
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all (len(units[s])== 3 for s in squares)
    assert all (len(peers[s])== 20 for s in squares)
    assert units['C2'] ==[['A2', 'B2','D2','E2','F2', 'G2','H2','I2'],
                         ['C1', 'C2','C3','C4','C5', 'C6','C7','C8','C9']
                         ['A1', 'A2','A3','B1','B2', 'B3','C1','C2','C3']]
    assert peers['C2'] == set(['A2', 'B2','D2','E2','F2', 'G2','H2','I2'
                             'C1', 'C2','C3','C4','C5', 'C6','C7','C8','C9'
                             'A1', 'A3','B1','B3'])
    print ('ALL tests pass.')