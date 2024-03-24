"""Initialize scripts for OpenTelemetry"""
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter

from discord.ext.commands import Bot

from src.models.config import BotConfig
from src.instrumentation.instrumentator import DiscordPyInstrumentor

def init_opentelmetry(config: BotConfig, bot: Bot):
    resource = Resource(
        attributes={
            SERVICE_NAME: "capybara-discord-bot"
        }
    )
    init_trace(resource, config.otel_otlp_exporter_http_endpoint)
    init_metrics(resource, config.otel_otlp_exporter_http_endpoint)

    DiscordPyInstrumentor().instrument(bot=bot)
    

def init_trace(resource: Resource, otlp_endpoint: str):
    trace_provider = TracerProvider(resource=resource)
    trace_processor = BatchSpanProcessor(OTLPSpanExporter(endpoint=f"{otlp_endpoint}/v1/traces"))
    trace_provider.add_span_processor(trace_processor)
    trace.set_tracer_provider(trace_provider)

def init_metrics(resource: Resource, otlp_endpoint: str):
    metric_reader = PeriodicExportingMetricReader(OTLPMetricExporter(endpoint=f"{otlp_endpoint}/v1/metrics"))
    meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
    metrics.set_meter_provider(meter_provider)
