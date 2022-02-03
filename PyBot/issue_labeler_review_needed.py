from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp


router = routing.Router()

############################ Issue review_needed labeler #############################################


LABEL = 'review_needed' # label name

@router.register("issues", action="opened")
async def issue_opened_event(event, gh, *args, **kwargs):
    label = event.data['issue']['labels_url']

    await gh.post(label, data=[LABEL]) #event post for key label