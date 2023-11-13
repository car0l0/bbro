#Imports
import openai
import typer
from rich import print
from rich.table import Table

# Reemplaza esto con tu clave de API real
openai.api_key = ""

def chatgpt(prompt):
    model='gpt-3.5-turbo'
    messages = [
        {"role": "system", "content": "You are a model that classifies offensive content into one of the following labels: fatphobia, sexism, racism, xenophobia, homophobia. Your answer MUST only be the label."},
        {"role": "user", "content": "Text to analyze: " + prompt }
    ]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    label = response['choices'][0]['message']['content']
    return label

def main(user_content):

    openai.api_key = ""

    print("💬 [bold green]ChatGPT API en Python[/bold green]")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    print(table)

    # Contexto del asistente
    context = {"role": "system",
               "content": "You are a model that classifies offensive content into one of the following labels: fatphobia, sexism, racism, xenophobia, homophobia."}
    messages = [context]

    while True:
        content = __prompt(user_content)
        if content == "new":
            print("🆕 New conversation created")
            messages = [context]
            content = __prompt(user_content)

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")
    return response_content



def __prompt(user_content) -> str:
    prompt = typer.prompt("\n Classify the following content:"+user_content)

    if prompt == "exit":
        exit = typer.confirm("✋ ¿Estás seguro?")
        if exit:
            print("👋 ¡Hasta luego!")
            raise typer.Abort()

        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(main)