from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp


router = routing.Router()


############################ issue comment reactor #############################################
# https://stackoverflow.com/questions/64112300/how-can-i-get-the-list-of-github-webhook-events


# issue comment reacter will also work for pull request so we don't need to do other stuff for that


@router.register("issue_comment", action="created")
async def issue__comment_create_event(event, gh, *args, **kwargs):

    #url for the comment reaction api
    url = event.data['comment']['reactions']['url']

    #finding owner to not react on that comment
    repo_owner = event.data['repository']['owner']['login']

    #finding author of the comment
    author = event.data['issue']['user']['login']


    if(author != repo_owner) :

        #reaction for the create issue comment
        message = 'heart'

        await gh.post(url, data={
            'content': message,
        })

        # await gh.post(url, data={
        #     'heart': 1,
        # })


@router.register("issue_comment", action="edited")
async def issue__comment_edit_event(event, gh, *args, **kwargs):

    #url for the comment reaction api
    url = event.data['comment']['reactions']['url']

    #finding owner to not react on that comment
    repo_owner = event.data['repository']['owner']['login']

    #finding author of the comment
    author = event.data['issue']['user']['login']


    if(author != repo_owner) :

        #reaction for the edit issue comment
        message = 'eyes'

        await gh.post(url, data={
            'content': message,
        })