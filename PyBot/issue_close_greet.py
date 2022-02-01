from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp


router = routing.Router()

############################ Issue Greetings when closed #############################################


@router.register("issues", action="closed")
async def issue_opened_event(event, gh, *args, **kwargs):

    url = event.data['issue']['comments_url']
    author = event.data['issue']['user']['login']
    # avatar = event.data['issue']['user']['avatar_url']

    message = f"<br><table><tbody><tr><td>Thanks for closing this issue @{author}! We hope you loved to work with our repository 😋.</td></tr></tbody></table>"
    await gh.post(url, data={
        'body': message,
        })
