from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp


router = routing.Router()

############################ issue comment reactor #############################################
# https://stackoverflow.com/questions/64112300/how-can-i-get-the-list-of-github-webhook-events



@router.register("issue_comment", action="created")
async def issue__comment_create_event(event, gh, *args, **kwargs):
    url = event.data['comment']['reactions']['url']


    url1 = event.data['issue']['comments_url']
    message = "heart"

    await gh.post(url, data={
        'content': message,
    })

    # await gh.post(url, data={
    #     'heart': 1,
    # })