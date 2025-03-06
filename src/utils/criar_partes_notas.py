import os
from lang
#llm = ChatOpenAI(model='gpt-3', temperature=0)

class Notes:
    def criar_tags(texto):
        'Create text tags'
        print('Create Tags')
        prompt = """
                Crie até 10 tags referente a este texto \n{texto}\n
                Você deve responder apenas as tags, sem nenhum comentário, 
                sem numeração,
                as tags devem estar alinhadas em uma única linha,
                separadas por um espaço,
                Elas devem ser relacionadas apenas ao texto
                por exemplo, um texto sobre filosofia pode ter a tag #filosofia
                outro exemplo, um texto que fale sobre treino de academia
                pode ter as tags #fitness #health
                todas as tags devem ter # na frente, por exemplo #exemplo
                """
        
        tags = llm.ivoke(prompt)

        return tags.content

    def resume_small(article):
        resumo  = Notes.text_sumarize(article, min_length=30, max_length=130)
        return resumo


    def resume_detail(article):
        resumo  = Notes.text_sumarize(article, min_length=130, max_length=330)
        return resumo


    def text_sumarize(article, min_length=30, max_length=130):

        from transformers import pipeline
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(article, max_length=max_length, min_length=min_length)

        return summary

    def cria_bullet_point(text):
        pass

    def formatar_notas(tags, resume_small, resume_detail, bullet_point):
        pass

    def salvar_notas(transcribe_path):
        """Save a file on text note file"""
        print('Create a file on text note file')

        transcribe_path = transcribe_path.replace("'", "")
        print(f'new transcribe_path {transcribe_path}')

        with open(transcribe_path,"rb") as file:
            transcribe = file.read()
            #tag = Notes.criar_tags(transcribe)
            resume_small = Notes.resume_small(transcribe)
            resume_detail = Notes.resume_detail(transcribe)
            #bullet_point = Notes.cria_bullet_point(transcribe)
            #note = Notes.formatar_notas(tag, 
            #                            resume_small, 
            #                            resume_detail,
            #                            bullet_point)

            print('Notes created')

        output_path = os.path.dirname(transcribe_path)
        output_path = output_path.replace('transcribe', 'notes')

        base_name = os.path.splitext(os.path.basename(output_path))[0]
        resume_path = f'{output_path}/{base_name}.md'
        print(f'basename path {base_name}')

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f'Folder create: "{output_path}"')
        
        with open(resume_path, 'w', encoding='utf-8') as f:
            #f.write(note.strip())
            f.write(resume_small.strip())
            f.write(resume_detail.strip())

        print(f'Save transcribe_path on: "{transcribe_path}"')


if __name__ == '__main__':
    transcribe_path = "/workspaces/Video_to_text/media/transc/transc.md"

    resume = Notes.salvar_notas(transcribe_path)
    print(f'Small Resume: {resume}')


    #Notes.salvar_notas(trastricao_path)