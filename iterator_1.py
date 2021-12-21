def get_nested_list():
	nested_list = [
		['a', 'b', 'c'],
		['d', 'e', 'f', 'h', False],
		[1, 2, None],
	]
	return nested_list


def flat_list_generator(some_list):
	return (it for sublist in some_list for it in sublist)


class FlatIterator:

	def __init__(self, some_list, cursor=0):
		self.some_list = some_list
		self.cursor = cursor
		self.flat_list = [item for sublist in self.some_list for item in sublist]

	def __iter__(self):
		self.cursor = -1
		return self

	def __next__(self):
		if self.cursor + 1 >= len(self.flat_list):
			raise StopIteration
		self.cursor += 1
		return self.flat_list[self.cursor]


if __name__ == '__main__':
	nested_list = get_nested_list()
	iterator_obj = FlatIterator(nested_list)

	for item in iterator_obj:
		print(item)

	print('-------------------------------')

	for i in flat_list_generator(nested_list):
		print(i)
