
#llm = ChatOpenAI(model='gpt-3', temperature=0)

class Notes:
    def criar_tags(texto):
        pass

    def criar_resumo_curto(article):
        resumo  = Notes.text_sumarize(article, min_length=30, max_length=130)
        return resumo


    def criar_resumo_detalhado(article):
        resumo  = Notes.text_sumarize(article, min_length=130, max_length=330)
        return resumo


    def text_sumarize(article, min_length=30, max_length=130):

        from transformers import pipeline
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(article, max_length=max_length, min_length=min_length)

        return summary

    def cria_bullet_point(text):
        pass

    def formatar_notas(tags, resumo_curto, resumo_detalhado, bullet_point):
        pass

    def salvar_notas(trastricao_path):
        pass


if __name__ == '__main__':
    trastricao_path = "/workspaces/Video_to_text/media/transc/transc.md"

    resume = Notes.criar_resumo_curto(trastricao_path)
    print(f'Small Resume: {resume}')

    resume = Notes.criar_resumo_detalhado(trastricao_path)
    print(f'Large Resume: {resume}')

    #Notes.salvar_notas(trastricao_path)