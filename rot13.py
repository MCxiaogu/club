class Rot13():
    '''Usage:
    rot=Rot13()
    rot.encode(str)
    rot.decode(str)
    returns a list with each element in str'''

    def __init__(self):
        self.dic_en = {}
        for c in (65, 97):
            for i in range(26):
                self.dic_en[chr(i + c)] = chr((i + 13) % 26 + c)
        self.dic_dn = {}
        for key, value in self.dic_en.items():
            self.dic_dn[value] = key

    def __str__(self):
        return 'ROT13 Passcode Class'

    def __repr__(self):
        return 'ROT13 Passcode Class'

    def encode(self, strr):
        self.l = []
        for each in strr:
            if each.isdigit() == False:
                try:
                    self.l.append(self.dic_en.get(each))
                except Exception as e:
                    print(e)
            else:
                self.l.append(each)
        return self.l

    def decode(self, strr):
        self.l = []
        for each in strr:
            if each.isdigit() == False:
                try:
                    self.l.append(self.dic_dn[each])
                except Exception as e:
                    print(e)
            else:
                self.l.append(each)


rot = Rot13()
help(rot)
