from loader import dp
from .chanel import CustomMiddleware


if __name__ == 'middleware':
    dp.middleware.setup(CustomMiddleware())