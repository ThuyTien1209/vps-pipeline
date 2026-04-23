import dagster as dg

from .defs.assets import print_asset
from .defs.jobs import jobs
from .defs.resources.notifier import NftyResource


all_assets = dg.load_assets_from_modules([print_asset])

defs = dg.Definitions(
    assets=all_assets,
    jobs=[jobs.print_hello_job, jobs.print_world_job],
    schedules=[jobs.hello_schedule, jobs.world_schedule], 
    resources={"nfty": NftyResource()}   
)


