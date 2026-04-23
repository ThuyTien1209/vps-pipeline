import dagster as dg
from pathlib import Path
# from hello_world.resources.send_ntfy import NftyResource
import requests
from datetime import datetime
from ..resources.notifier import NftyResource

TODAY = datetime.today().date().strftime(format='%Y-%M-%d')

@dg.asset
def hello(context : dg.AssetExecutionContext,
          nfty: NftyResource) -> None: 
    
    try: 
        context.log.info(f"Đang run asset Hello cho ngày {TODAY}")
        priint("Hello")

        SUCCESS = f'asset hello run thành công cho ngày {TODAY}'
        context.log.info(SUCCESS)


        # requests.post(SUCCESS_CHANNEL, data = SUCCESS.encode(encoding='utf-8'), verify=False)

        # nfty.success(SUCCESS)
        
    except Exception as e:
         
         ERROR = f"asset hello run cho ngày {TODAY} lỗi: {str(e)}"
         context.log.info(ERROR) # log in Dagster UI
         context.log.info("Đang gửi lỗi")
        #  requests.post(FAILURE_CHANNEL, data = ERROR.encode(encoding='utf-8'), verify=False) # noti send to phone
         context.log.info("Gửi lỗi thành công")

        #  nfty.failure(ERROR)
         


@dg.asset(deps=['hello'])
def world(context: dg.AssetExecutionContext,
          nfty: NftyResource) -> None:
    try: 
        context.log.info(f"Đang run asset world cho ngày {TODAY}")
        print('world')

        SUCCESS = f'asset world run thành công cho ngày {TODAY}'
        context.log.info(SUCCESS) # asset world run thành công cho ngày xx-xx-xxxx
        # requests.post(SUCCESS_CHANNEL, data = SUCCESS.encode(encoding='utf-8'), verify=False) 
        # nfty.success(SUCCESS)

    except Exception as e:
        ERROR = f"asset world run cho ngày {TODAY} lỗi: {str(e)}"
        context.log.info(ERROR)
        context.log.info("Đang gửi lỗi")
        # requests.post(FAILURE_CHANNEL, data = ERROR.encode(encoding='utf-8'), verify=False)
        context.log.info("Gửi lỗi thành công")
        # nfty.failure(ERROR)






