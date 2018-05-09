import string


def login_required(func):
    def wrapper(*args, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')
        if email != 'olena@gmail.com' or password != '12345678':
            return 'Please login'
        else:
            return func(*args, id=kwargs.get('id'))
    return wrapper


@login_required
def route(url: string, **data):
    if url == '/':
        return 'Hello, World'
    if url == '/about/':
        return 'I am a light web server'
    if url == '/catalog/':
        id = data.get('id')
        return f'It is a catalog. You are looking for the item {id}'
    else:
        return '404 - not found'


print(route('/catalog/', id=21))
print(route('/catalog/', email='olena@gmail.com', password='12345678', id=21))
print(route('/about/', email='olena@gmail.com', password='12345678', id=21))
print(route('/about/', email='ol@gmail.com', password='12'))
print(route('/', email='olena@gmail.com', password='12345678', id=21))
