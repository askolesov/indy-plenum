from plenum.common.constants import CONFIG_LEDGER_ID
from plenum.server.batch_handlers.batch_request_handler import BatchRequestHandler
from plenum.server.database_manager import DatabaseManager


class ConfigBatchHandler(BatchRequestHandler):

    def __init__(self, database_manager: DatabaseManager):
        super().__init__(database_manager, CONFIG_LEDGER_ID)

    def commit_batch(self, txn_count, state_root, txn_root, pp_time, prev_result= None):
        return super().commit_batch(txn_count, state_root, txn_root, pp_time, prev_result)

    def post_batch_applied(self, ledger_id, state_root, pp_time, prev_result= None):
        pass

    def post_batch_rejected(self):
        pass
