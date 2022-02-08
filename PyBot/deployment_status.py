from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp


router = routing.Router()

link = "https://api.github.com/repos/vasu-1/testpython/issues/3/comments";

@router.register("deployment_status", action="")
async def opened_pr(event, gh, *arg, **kwargs):

	status = event.data['deployment_status']['state']
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