import typer
import json
from deepboreai_sdk.sdk import DeepBoreAI

app = typer.Typer()
client = DeepBoreAI()

@app.command()
def ingest(file: str):
    with open(file, 'r') as f:
        data = json.load(f)
    result = client.post_telemetry(data)
    typer.echo(result)

@app.command()
def export(out: str = 'drilling_data.csv'):
    path = client.export_csv(out)
    typer.echo(f"Exported to {path}")

@app.command()
def stream():
    def callback(data):
        typer.echo(f"Live Alert: {data}")
    typer.echo("Listening to live data stream...")
    client.watch_live(callback)
    input("Press Enter to stop...
")

if __name__ == "__main__":
    app()