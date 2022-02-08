from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp


router = routing.Router()

link = "https://api.github.com/repos/vasu-1/testpython/issues/3/comments";

@router.register("workflow_run", action="completed")
async def workflow_job(event, gh, *arg, **kwargs):

	status = event.data['workflow_run']['conclusion']
	# ur = event.data['pull_request']['comments_url']

	if(status == "success"):
		messag = f"succeed"
		await gh.post(link, data={
			'body': messag,
			})

	elif(status == "failure"):
		messag = f"Failure"
		await gh.post(link, data={
			'body': messag,
			})
	else:
		return