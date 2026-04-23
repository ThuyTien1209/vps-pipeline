import dagster as dg

print_hello_job = dg.define_asset_job(name ='print_hello_job', selection='hello')

print_world_job = dg.define_asset_job(name ='print_world_job', selection='world')

hello_schedule = dg.ScheduleDefinition(job=print_hello_job, cron_schedule='0 6 * * *', execution_timezone='Asia/Ho_Chi_Minh')
world_schedule = dg.ScheduleDefinition(job=print_world_job, cron_schedule='0 7 * * *', execution_timezone='Asia/Ho_Chi_Minh')


