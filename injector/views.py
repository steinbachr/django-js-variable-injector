from django.shortcuts import render

def injector_test(request):
	return render(request, 'injector_test.html', {
		'test_arr': [1, 2, 3, 4],
		'test_dict': {
			'a': 1,
			'b': 2,
			'c': 3
		}
	})