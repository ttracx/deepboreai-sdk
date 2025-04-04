# DeepBoreAI SDK

This Python SDK provides programmatic access to the DeepBoreAI real-time drilling analytics platform.

## Features
- Post telemetry data
- Stream real-time alerts
- Export historical data to CSV
- Command-line interface (CLI)

## Installation

```bash
pip install deepboreai-sdk
```

## Usage

```python
from deepboreai_sdk.sdk import DeepBoreAI

client = DeepBoreAI()
client.post_telemetry({...})
alerts = client.get_recent_alerts()
client.export_csv()
```

Or use the CLI:

```bash
deepboreai ingest --file sample.json
deepboreai stream
deepboreai export
```