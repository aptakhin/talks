from time import perf_counter
from contextlib import contextmanager

from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import InMemoryMetricReader, ConsoleMetricExporter, PeriodicExportingMetricReader


def init_otel():
    resource = Resource(attributes={
        SERVICE_NAME: "my-service"
    })

    reader = InMemoryMetricReader()
    meter_provider = MeterProvider(resource=resource, metric_readers=[reader])
    metrics.set_meter_provider(meter_provider)

    tracer_provider = TracerProvider(resource=resource)
    processor = SimpleSpanProcessor(ConsoleSpanExporter())
    tracer_provider.add_span_processor(processor)
    trace.set_tracer_provider(tracer_provider)

    exporter = ConsoleMetricExporter()
    # reader = PeriodicExportingMetricReader(
    #     exporter,
    #     # preferred_temporality=temporality_cumulative,
    #     export_interval_millis=5_000,
    # )


@contextmanager
def catchtime() -> float:
    start = perf_counter()
    yield lambda: perf_counter() - start
