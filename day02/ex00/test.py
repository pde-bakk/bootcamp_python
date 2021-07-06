#!/usr/bin/env python3
from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce
from functools import reduce


def square(x):
	return x * x


def filter_even(x):
	return x % 2 == 0


def test_equality(testname, og_func, ft_func, apply_func) -> None:
	iterable = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
	if testname == 'Reduce':
		og, ft = og_func(apply_func, iterable), ft_func(apply_func, iterable)
		if og != ft:
			print(f'{testname} failed because {og} != {ft}')
	else:
		for og, ft in zip(og_func(apply_func, iterable), ft_func(apply_func, iterable)):
			if og != ft:
				print(f'{testname} failed because {og} != {ft}')
				return
	print(f'{testname} succeeded!')


def main():
	test_equality('Map', map, ft_map, square)
	test_equality('Filter', filter, ft_filter, filter_even)
	test_equality('Reduce', reduce, ft_reduce, lambda x, y: x+y)


if __name__ == '__main__':
	main()
