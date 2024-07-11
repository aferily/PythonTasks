# 9_1
def good():
    return ['Harry', 'Ron', 'Hermione']
print(f'good: {good()}')

# 9_2
def get_odds():
    return range(1, 10, 2)
counter = 1
for num in get_odds():
    if counter == 3:
        print(f'3-е нечетное натуральное числе черезе for: {num}')
        break
    counter += 1
else:
    print(f'список нечетных натуральных чисел слишком мал для поиска 3-его')

# 9_3
def test(fun):
    def upd_fun(*args, **kwargs):
        print('start')
        fun()
        print('end')
    return upd_fun

@test
def fun():
    print('smth done')

fun()

# 9_4
class OopsException(Exception):
    pass

def fun():
    raise OopsException("что ты наделал, все сломалось..")

try:
    fun()
except OopsException as err:
    print(f'Ooops. Комментарий: {err}')