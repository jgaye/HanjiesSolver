# Test init

box = Box()
box.is_unknown() must be True

# Test setters & getters

box.is_unknown must be True
box.fill_white()
box.is_white() must be True
box.fill_white() must return error
box.fill_black() must return error

box2 = Box()
box2.is_unknown must be True
box2.fill_black()
box2.is_black() must be True
box2.fill_white() must return error
box2.fill_black() must return error

# Test repr

box3 = Box()
print box3 must be "?"
print box must be white square
print box2 must be black square
