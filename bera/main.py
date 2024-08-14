import os, sys
os.chdir(sys.path[0])  # 将当前文件路径设为工作路径

from bera_tools import *

from eth_account import Account
from loguru import logger

from bera_tools import BeraChainTools
from config.address_config import *

private_key = "0x03018da7cd..."
account = Account.from_key(private_key)
bera = BeraChainTools(private_key=account.key, rpc_url='https://rpc.ankr.com/berachain_testnet')

# # bex 使用bera交换honey
# bera_balance = bera.w3.eth.get_balance(account.address)
# logger.info(f'bera balance: {bera_balance}')
# result = bera.bex_swap(int(bera_balance * 0.1), wbear_address, honey_address)
# logger.info(result)

# 注册域名
result = bera.create_bera_name()
logger.info(result)