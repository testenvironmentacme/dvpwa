from functools import wraps
from typing import Optional

from aiohttp.web import Application
from aiohttp.web_exceptions import HTTPForbidden, HTTPUnauthorized
from aiohttp.web_request import Request
from aiohttp_session import get_session
from PIL import Image, ImageMath

from sqli.dao.user import User


def authorize(ensure_admin=False):
    def __decorator__(handler):
        @wraps(handler)
        async def __wrapper__(request: Request):
            user = await get_auth_user(request)
            if user is None:
                raise HTTPUnauthorized()
            if ensure_admin and not user.is_admin:
                raise HTTPForbidden()
            return await handler(request)
        return __wrapper__
    return __decorator__


async def get_auth_user(request: Request) -> Optional[User]:
    app: Application = request.app
    session = await get_session(request)
    user_id = session.get('user_id')
    async with app['db'].acquire() as conn:
        return await User.get(conn, user_id)

def pillowfunctiontest(sql):
    im1 = Image.open(r"C:\Users\System-Pc\Desktop\ybear.jpg").convert('L') 
    im2 = Image.open(r"C:\Users\System-Pc\Desktop\leave.jpg").convert('L')

    out = ImageMath.eval("convert(min(a, b), 'L')", a = im1, b = im2)
    test = ImageMath.eval("exec(exit())")
    out.save("result.jpg")
    out.show()
    
    with Image.open(path) as im:
        im.thumbnail(size)
        im.save(file + ".thumbnail", "JPEG")
        ImageMath.eval("convert(image, shred)", image = real_banksy)

path = input()
pillowfunctiontest(path)
