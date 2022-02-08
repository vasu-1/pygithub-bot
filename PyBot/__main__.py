import asyncio
import importlib
import os
import sys
import traceback

import aiohttp
from aiohttp import web
import cachetools
from gidgethub import aiohttp as gh_aiohttp
from gidgethub import routing
from gidgethub import sansio

from . import issue_greeter, pr_greeter, issue_labeler_review_needed, pr_review_needed_labeler, comment_reacter, issue_close_greet, pr_close_greet, issue_assign, deployment_status

import sentry_sdk

router = routing.Router(issue_greeter.router, pr_greeter.router, issue_labeler_review_needed.router, pr_review_needed_labeler.router, comment_reacter.router, issue_close_greet.router, pr_close_greet.router, issue_assign.router, deployment_status.router)
cache = cachetools.LRUCache(maxsize=500)

sentry_sdk.init(os.environ.get("SENTRY_DSN"))

async def main(request):
    try:
        body = await request.read()
        secret = os.environ.get("GH_SECRET")

        event = sansio.Event.from_http(request.headers, body, secret=secret)
        print('GH delivery ID', event.delivery_id, file=sys.stderr)
        if event.event == "ping":
           return web.Response(status=200)
        
        oauth_token = os.environ.get("GH_AUTH")
        async with aiohttp.ClientSession() as session:
            gh = gh_aiohttp.GitHubAPI(session, "vasu-1",
                                      oauth_token=oauth_token)
          
            await asyncio.sleep(1)
            await router.dispatch(event, gh)
        try:
            print('GH requests remaining:', gh.rate_limit.remaining)
        except AttributeError:
            pass
        return web.Response(status=200)
    except Exception as exc:
        traceback.print_exc(file=sys.stderr)
        return web.Response(status=500)


if __name__ == "__main__": 
    app = web.Application()
    app.router.add_post("/", main)
    port = os.environ.get("PORT")
    if port is not None:
        port = int(port)
    web.run_app(app, port=port)
