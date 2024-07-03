def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()

# inner_function()
# Если вызвать ее после test_function: NameError: name 'inner_function' is not defined.
# Это происходит по тому, что inner_function находится в объемлющей области видимости test_function
# И в глобальном пространстве inner_function() не существует