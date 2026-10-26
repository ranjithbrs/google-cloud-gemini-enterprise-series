"""
Telemetry and callback logging handler for ADK agent.
"""
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("adk_agent")

def log_event(event_name: str, payload: dict):
    logger.info("Event: %s | Payload: %s", event_name, payload)
