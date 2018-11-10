alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original position: " + str(alien_0['x_position']))

# 检查字典元素
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# 改变字典键值
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New position: " + str(alien_0['x_position']))
