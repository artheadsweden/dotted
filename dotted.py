class DotList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, key):
        return self.items[key]

    def __getattr__(self, attr):
        new_items = []
        for item in self.items:
            try:
                attr_value = getattr(item, attr)
                if isinstance(attr_value, list):
                    new_items.extend(attr_value)
                else:
                    new_items.append(attr_value)
            except AttributeError:
                pass
        if not new_items:
            raise AttributeError(f"'DotList' object has no attribute '{attr}'")
        return DotList(new_items)

    def index(self, value, start=0, stop=None):
        index = self.items.index(value)
        return [index]
    
    def filter(self, value):
        return [x for i, x in enumerate(self.items) if x == value]
    
    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f"DotList({repr(self.items)})"


class A:
    def __init__(self, name):
        self.name = name

class B:
    def __init__(self, a_list):
        self.a_list = a_list

class C:
    def __init__(self, b_list):
        self.b_list = b_list

a1 = A('foo')
a2 = A('bar')
b = B([a1, a2])
dotlist = DotList([b])
c = C(DotList(dotlist))

print(dotlist[0].a_list[0].name)  # prints 'foo'
print(dotlist.a_list.name)  # prints ['foo', 'bar']
if 'foo' in c.b_list.a_list.name:
    print('Yes')
else:
    print('No')
    
print(c.b_list.a_list.name.filter('bar'))  # ['bar']
