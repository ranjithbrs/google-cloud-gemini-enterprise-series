"""
ADK Agent definition with BigQueryToolset for Cymbal Pools.
"""
import datetime
from google.adk.agent import Agent
from google.adk.tools.bigquery import (
    BigQueryToolset,
    BigQueryToolConfig,
    BigQueryCredentialsConfig,
)

def get_current_time() -> str:
    """Returns the current date and time in ISO format."""
    return datetime.datetime.now().isoformat()

# Configure BigQuery Toolset with write access
bq_toolset = BigQueryToolset(
    credentials_config=BigQueryCredentialsConfig(),
    tool_config=BigQueryToolConfig(write_access=True),
)

agent = Agent(
    name="bigquery_pool_agent",
    model="gemini-3.5-flash",
    instruction=(
        "You are an assistant for Cymbal Pools. Help users analyze pool installation "
        "requests stored in BigQuery and record new installation requests."
    ),
    tools=[bq_toolset, get_current_time],
)
