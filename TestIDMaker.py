import unittest
# import the code you want to test here
from idmaker import name_to_dict, make_userid

class TestIDMaker(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def test_name_to_dict_PHB(self) -> None:
        self.assertEqual(name_to_dict('Brown, Peter H.'), {'lastname': 'Brown', 'othernames': "Peter H."})

    def test_name_to_dict_RedBaron(self) -> None:
        self.assertEqual(name_to_dict('von Richthofen, Manfred Albrecht'), 
                         {'lastname': 'von Richthofen', 'othernames': "Manfred Albrecht"})
    
    def test_name_to_dict_ABB3(self) -> None:
        self.assertEqual(name_to_dict('Brown, Jr., A. Bruce'), {'lastname': 'Brown', 'othernames': "A. Bruce"})

    def test_name_to_dict_Wm(self) -> None:
        self.assertEqual(name_to_dict('Windsor, William Arthur Philip Louis'), 
                                        {'lastname': 'Windsor', 'othernames': "William Arthur Philip Louis"})
        
    def test_userid_PHB(self) -> None:
        self.assertEqual(make_userid({'lastname': 'Brown', 'othernames': "Peter H."}), 'phbrown001')

    def test_userid_LFB(self) -> None:
        self.assertEqual(make_userid({'lastname': 'Feitzinger', 'othernames': "Laura"}), 'lfeitzinger001')

    def test_userid_RedBaron(self) -> None:
        self.assertEqual(make_userid({'lastname': 'von Richthofen', 'othernames': "Manfred Albrecht"}), 
                         'mavonrichthofen001')

    def test_userid_ABB3(self) -> None:
        self.assertEqual(make_userid({'lastname': 'Brown', 'othernames': "A. Bruce"}), 'abbrown001')

    def test_userid_Wm(self) -> None:
        self.assertEqual(make_userid({'lastname': 'Windsor', 'othernames': "William Arthur Philip Louis"}), 
                        'wawindsor001')
    
    def test_userid_OReilly(self) -> None:
        self.assertEqual(make_userid({'lastname': "O'Reilly", 'othernames': 'Richard R.'}), 'rroreilly001')

    def test_userid_Jamie(self) -> None:
        self.assertEqual(make_userid({'lastname': "Grant-Ponce", 'othernames': 'Jamie'}), 'jgrant-ponce001')


if __name__ == '__main__':
    unittest.main()

