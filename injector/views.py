from django.shortcuts import render


class TestClass(object):
    def __init__(self):
        self.arr = ['a', 1, 2]
        self.dict = {'a': 1, 'b': 2}
        self.num = 1

    def test_method(self):
        return True


def injector_test(request):
    return render(request, 'injector_test.html', {
        'test_arr': [1, 2, 3, 4],
        'test_dict': {
            'a': 1,
            'b': 2,
            'c': 3
        },
        'test_str': 'hey',
        'test_int': 2,
        'test_bool': True,
        'test_none': None,
        'test_unicode': unicode('test'),
        'test_complex1': [1, unicode('test')],
        'test_complex2': {
            'a': 1,
            'b': unicode('test'),
            1: 'c',
            'c': '\'test\''
        },
        'test_class': TestClass()
    })