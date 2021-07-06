# I decided not to implement it with an Initializer argument since that is not in the prototype for this assignment.
def ft_reduce(function_to_apply, list_of_inputs):
	it = iter(list_of_inputs)
	value = next(it)
	for element in it:
		value = function_to_apply(value, element)
	return value
