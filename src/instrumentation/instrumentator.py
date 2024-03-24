"""Auto instrumentation for the application and discordpy

    For application, we aim to decouple the instrument code from business logic
    For discordpy, just a temporary solution before a formal auto instrument
        package is released.
"""
import wrapt
from opentelemetry.instrumentation.instrumentor import BaseInstrumentor
from opentelemetry.instrumentation.utils import unwrap
from opentelemetry import trace

from discord.client import Client
from discord.app_commands import CommandTree

def sync_trace_wrapper(wrapped, instance, args, kwargs):
    """Sync trace wrapper"""
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span(wrapped.__name__):
        result = wrapped(*args, **kwargs)
        return result

async def async_trace_wrapper(wrapped, instance, args, kwargs):
    """Async trace wrapper"""
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span(wrapped.__name__):
        result = await wrapped(*args, **kwargs)
        return result

class DiscordPyInstrumentor(BaseInstrumentor):
    def instrumentation_dependencies(self):
        return tuple()
    
    def _instrument(self, **kwargs):
        # Get the bot instance for instrumentation
        bot = kwargs.get("bot")
        self._instrument_trace(bot=bot)
        

    def _uninstrument(self):
        """Clean up trace instrumentation"""
        self._uninstrument_trace()
    
    def _instrument_trace(self, bot: Client):
        """Initalize trace instrumentation"""
        wrapt.wrap_function_wrapper(bot, "on_ready", async_trace_wrapper)
        wrapt.wrap_function_wrapper(bot, "on_message", async_trace_wrapper)
        wrapt.wrap_function_wrapper(bot.tree, "sync", async_trace_wrapper)
    
    def _uninstrument_trace(self):
        """Initialize metric instrumentation"""
        unwrap(Client, "on_ready")
        unwrap(Client, "on_message")
        unwrap(CommandTree, "sync")