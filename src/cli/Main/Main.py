import typer

app = typer.Typer(help="Main CLI tool")

@app.command()
def run(
    input:   str  = typer.Option(..., help="Input value"),
    verbose: bool = typer.Option(False, help="Show detailed output"),
):
    """Main command — customize this."""
    if verbose:
        typer.echo(f"Running Main with input: {input}")

    # TODO: add your logic here
    typer.echo("Done!")

@app.command()
def version():
    """Show current version."""
    typer.echo("Main v1.0.0")


if __name__ == "__main__":
    app()