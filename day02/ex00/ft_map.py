def ft_map(function_to_apply, list_of_inputs):
	for item in list_of_inputs:
		yield function_to_apply(item)
