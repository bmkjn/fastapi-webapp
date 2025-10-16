import logging
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter

# Setting up tracing
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Configure Azure Monitor exporter
exporter = AzureMonitorTraceExporter.from_connection_string(
    "InstrumentationKey=19c9c53e-448a-4953-9374-a782b6392735;IngestionEndpoint=https://uaenorth-0.in.applicationinsights.azure.com/;LiveEndpoint=https://uaenorth.livediagnostics.monitor.azure.com/;ApplicationId=a70e5645-1ce5-49bc-b5c1-6e25d57d8a23"
)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(exporter)
)

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a custom log message
def log_custom_event():
    logger.info("Custom log: User click")
    with tracer.start_as_current_span("custom-trace-span"):
        logger.info("Trace: Payment in progress")

if __name__ == "__main__":
    log_custom_event()
