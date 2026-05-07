import typer

app = typer.Typer()


def main(extension: str = typer.Argument("txt", help="type de l'extension du fichier"), delete: bool = typer.Option(..., help="Supprime le fichier trouvé")):
    """
    Affiche les fichiers trouvés avec l'extension donnée
    """
    extension = typer.style(
        extension, fg=typer.colors.BLACK, bg=typer.colors.BLACK)
    typer.echo(f"Recherche des fichiers {extension}")

    #typer.echo(f"Recherche des fichiers avec l'extension {extension}.")
    if delete:
        suppression = typer.confirm(
            "Voulez vous vraiment supprimer ce fichier ?")
        if not suppression:
            print("On annule l'operation !")
            raise typer.Abort()

        print("fichier supprimé")


@app.command("search")
def serch_py():
    main(delete=False, extension="py")


@app.command("delete")
def delete_py():
    main(delete=True, extension="py")


if __name__ == "__main__":
    app()
