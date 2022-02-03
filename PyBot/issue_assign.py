from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp


router = routing.Router()


############################ issue comment reactor #############################################
# https://stackoverflow.com/questions/64112300/how-can-i-get-the-list-of-github-webhook-events


# issue comment will pass body and we will fetch the body of the comment and see that if it is used /assigned of nor


@router.register("issue_comment", action="created")
async def issue__comment_create_event(event, gh, *args, **kwargs):

    #url for the comment reaction api
    url = event.data['issue']['url']
    main_url = url + "/assignees"

    #comment url
    url_comment = event.data['comment']['url']

    #assignee check
    assinee = event.data['issue']['assignee']

    #issue body from the issue comment
    comment_body = event.data['comment']['body']

    #finding owner to not react on that comment
    #repo_owner = event.data['repository']['owner']['login']

    #finding author of the comment
    author = event.data['comment']['user']['login']

    #message for not assigning
    message = "We cannot assign this issue to you as it already assigned to someone ! Thanks !";

    if(comment_body == '/assign') :
        if(assinee == null) :
            await gh.post(main_url, data={
                'assignees' : [author],
            })

        else :
            await gh.post(url_comment, data={
                'body': message,
            })