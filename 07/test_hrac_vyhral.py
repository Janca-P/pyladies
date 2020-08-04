from piskvorky import vyhodnot
"""Vyhodnotí xxx v poli jako návratovou hodnotu x a provede print "Výhra"""
def test_hrac_vyhral():
    assert vyhodnot("-o-o-------------xxx") == "x"
    assert vyhodnot("xxooxxoox-ooxxooxxxo") == "x"
    assert vyhodnot("oxxxoxoxxooxxooxxoo-") == "x"