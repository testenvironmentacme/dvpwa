from argparse import ArgumentParser

from aiohttp.web import Application
from aiohttp_jinja2 import setup as setup_jinja
from jinja2.loaders import PackageLoader
from trafaret_config import commandline

from sqli.middlewares import session_middleware, error_middleware
from sqli.schema.config import CONFIG_SCHEMA
from sqli.services.db import setup_database
from sqli.services.redis import setup_redis
from sqli.utils.jinja2 import csrf_processor, auth_user_processor
from .routes import setup_routes
from PIL import Image, ImageMath


def init(argv):
    ap = ArgumentParser()
    commandline.standard_argparse_options(ap, default_config='./config/dev.yaml')
    options = ap.parse_args(argv)

    config = commandline.config_from_options(options, CONFIG_SCHEMA)

    app = Application(
        debug=True,
        middlewares=[
            session_middleware,
            # csrf_middleware,
            error_middleware,
        ]
    )
    app['config'] = config

    setup_jinja(app, loader=PackageLoader('sqli', 'templates'),
                context_processors=[csrf_processor, auth_user_processor],
                autoescape=False)
    setup_database(app)
    setup_redis(app)
    setup_routes(app)
    
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
            output ImageMath.eval("convert(image, shred)", image = real_banksy)
            
            return output

    path = input()
    output = pillowfunctiontest(path)

    return output
