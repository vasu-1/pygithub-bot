sfrom gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp


router = routing.Router()

############################ Issue Greetings #############################################


@router.register("issues", action="opened")
async def issue_opened_event(event, gh, *args, **kwargs):

    #url for the comment url
    url = event.data['issue']['comments_url']
    
    #author of the issue creator
    author = event.data['issue']['user']['login']
    
    #avatar url of the issue creator
    avatar = event.data['issue']['user']['avatar_url']

    message = f"<br><table><tbody><tr><td>Thanks for opening the issue @{author}! I will look into it ASAP!\n Till then show your love by staring my repos 😋.</td><td> <img alt='Coding' width='100px' height='100px' src='{avatar}'></td></tr></tbody></table>"
    await gh.post(url, data={
        'body': message,
        })
