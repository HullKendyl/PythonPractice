bag = dict()
bag['dollars'] = 15
bag['skittles'] = 5
bag['chapstick'] = 1
print(bag)
print('There are', bag['skittles'],'skittles in the bag.')
bag['chapstick'] = bag['chapstick'] + 1
print('I just bought another chapstick. Now there are',
      bag['chapstick'], 'of them in the bag and only', (bag['dollars'] - 1), "dollars.")
bag['dollars'] = 14
print(bag,'\n')

print('Courses Offered:')
course_list = dict()
course_list['Biology'] = 2001
course_list['Psychology'] = 1001
course_list['Anatomy'] = 2008
print(course_list)