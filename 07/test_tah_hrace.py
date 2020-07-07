import util #nezapomínat na přítomnost v příslušném adresáři
def test_tah_hrace():
    """Po provedení tahu hráče se na příslušném políčku objeví symbol x"""
    assert util.tah("--------------------", 0 , "x") == "x-------------------"