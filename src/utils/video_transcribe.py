import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
load_dotenv(override=True)
OLLAMA_SERVER_URL = os.environ['OLLAMA_SERVER_URL']

def run_transcribe(transcribe_path):

    print(OLLAMA_SERVER_URL)
#    llm = Ollama(model="mistral:7b", base_url=OLLAMA_SERVER_URL)
    llm = Ollama(model="llama3:8b" , base_url=OLLAMA_SERVER_URL)
    
    with open(transcribe_path, "r", encoding="utf-8") as file:
        transcribe = file.read()

    texto = transcribe

    prompt = f"Crie até 10 tags referente a este texto \n'{texto}'\n"

    prompt = prompt + """
                Você deve responder apenas as tags, sem nenhum comentário, 
                sem numeração, as tags devem estar alinhadas em uma única linha,
                separadas por um espaço, em potuguês.
                por exemplo, um texto sobre filosofia pode ter a tag #filosofia
                outro exemplo, um texto que fale sobre treino de academia
                pode ter as tags #fitness #health
                todas as tags devem ter # na frente, por exemplo #exemplo
                """
        
    tags = llm.invoke(prompt)
    print(tags)


import socket

def check_server(host='localhost', port=11434):
    try:
        sock = socket.create_connection((host, port), timeout=5)
        return True
    except Exception as e:
        print(f"Could not connect to server. Reason: {str(e)}")
        return False


# curl http://localhost:11434/api/generate -d '{
#     "model": "mistral:7b",
#     "prompt": "Why is the sky blue?",
#     "stream": false
# }'

# media/transcribe/transc.md

# Test the connection


if __name__ == '__main__':

    if check_server():
        print("Server is reachable.")
        transcribe_path = "./media/transcribe/transc.md"
        run_transcribe(transcribe_path)
    else:
        print("Server is unreachable or not running on the specified port.")
        


