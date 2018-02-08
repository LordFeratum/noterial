from aiohttp import web

from aiopg.sa import create_engine

from settings import settings


async def startup(app):
    dsn = app['settings']['DB_DSN']
    app['pg_engine'] = await create_engine(dsn, loop=app.loop)


async def cleanup(app):
    app['pg_engine'].close()
    await app['pg_engine'].wait_closed()


app = web.Application(middlewares=[])
for method, path, view, kwargs in []:
    app.router.add_route(method, path, view, **kwargs)


app['settings'] = settings
app.on_startup.append(startup)
app.on_cleanup.append(cleanup)


if __name__ == '__main__':
    web.run_app(app, port=settings['PORT'])
