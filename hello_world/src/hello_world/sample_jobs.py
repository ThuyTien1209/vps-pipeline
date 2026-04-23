import dagster as dg

tsale_data_update = dg.define_asset_job(
    name="tsale_update_job", selection=[
        "tsale_data_daily",
        "tsales_it_null_checking"
    ]
)

ob_territory_data_update = dg.define_asset_job(
    name="ob_territory_update_job", selection = ["territory_mapping_data_daily","ob_data_daily", "send_ob_data_daily"]
)

ha_territory_data_update = dg.define_asset_job(
    name="ha_territory_update_job", selection = ["territory_mapping_data_daily","ha_data_daily", "send_ha_data_daily"]
)

daily_schedule_tsale = dg.ScheduleDefinition(
    job=tsale_data_update,
    cron_schedule="30 8 * * *",
    execution_timezone="Asia/Ho_Chi_Minh",
)

daily_schedule_ob_territory = dg.ScheduleDefinition(
    job=ob_territory_data_update,
    cron_schedule="30 8 * * *",
    execution_timezone="Asia/Ho_Chi_Minh",
)

daily_schedule_ha_territory = dg.ScheduleDefinition(
    job=ha_territory_data_update,
    cron_schedule="30 8 * * *",
    execution_timezone="Asia/Ho_Chi_Minh",
)