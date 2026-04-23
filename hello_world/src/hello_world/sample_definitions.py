import dagster as dg

from .defs.jobs import jobs
from .defs import assets
from .defs.resources.db_resource import MyDatabaseResource
from .defs.resources.notifier_resource import NotifierResource
from .defs.resources.excel_resource import ExcelAutomationResource
from .defs.resources.email_resource import OutlookEmailResource
from .defs.resources.bline_daily_resource import DailyReportExcelResource
from .defs.configs.configs import PipelineConfigs

# Load all assets from module
all_assets = dg.load_assets_from_modules([assets])

# Create Definitions
defs = dg.Definitions(
    assets=all_assets,
    

    jobs=[
        jobs.tsale_data_update, 
        jobs.ob_territory_data_update,
        jobs.ha_territory_data_update
    ],

    schedules=[
        jobs.daily_schedule_tsale, 
        jobs.daily_schedule_ob_territory,
        jobs.daily_schedule_ha_territory
    ],
    

    resources={
        # Resource Database
        "db": MyDatabaseResource(
            engine=PipelineConfigs.DB_ENGINE,
            query_folder=PipelineConfigs.QUERY_FOLDER,
            chunksize=PipelineConfigs.CHUNKSIZE,
            log_every=PipelineConfigs.LOG_EVERY
        ),
        
        # Resource Notify
        "notifier": NotifierResource(
            success_bot=PipelineConfigs.SUCCESS_BOT,
            fail_bot=PipelineConfigs.FAIL_BOT
        ),
        
        # Resource auto excel format for OB
        "excel_tool": ExcelAutomationResource(),
        "email_tool": OutlookEmailResource(),
        # "bline_tool" : DailyReportExcelResource()
    }
)