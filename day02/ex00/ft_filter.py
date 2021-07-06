def ft_filter(function_to_apply, list_of_inputs):
	for item in list_of_inputs:
		if function_to_apply(item):
			yield item
