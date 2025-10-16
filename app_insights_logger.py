import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Attach Azure handler
logger.addHandler(
    AzureLogHandler(
        connection_string="InstrumentationKey=19c9c53e-448a-4953-9374-a782b6392735"
    )
)

def log_custom_event():
    logger.info("Custom log: User click")
    logger.warning("Trace: Payment in progress")

