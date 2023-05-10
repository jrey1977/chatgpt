import openai
import config
import typer
from rich import print
from rich.table import Table

def main():

    openai.api_key = config.api_key

    print("[bold green]ChatGPT API en Python[/bold green]")

    table = Table("Comando", "Descripción")
    table.add_row("exit","Salir de la aplicación")
    table.add_row("new","Empezar nueva conversación")
    print(table)

    context = {
        "role": "system",
        "content": "Eres un asistente muy útil."
    }
    messages = [context]

    while True:

        content = __prompt()

        if content == 'new':
            print("Nueva conversación")
            messages = [context]
            content = __prompt()

        messages.append({
            "role": "assistant",
            "content": content
        })

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                    messages=messages)
        
        reponse_content = response.choices[0].message.content

    
        messages.append({
            "role": "assistant",
            "content": reponse_content
        }) 

        print(f'[bold green]>[/bold green][green]{reponse_content}[/green]')

def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre qué quieres hablar?")

    if prompt == 'exit':
        exit = typer.confirm("¿Estás seguro?")
        if exit:
            print("¡hasta luego!")
            raise typer.Abort()
        return __prompt()
    
    return prompt

if __name__== "__main__":
    typer.run(main)