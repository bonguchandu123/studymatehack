from models.qna_model import QAModel
from models.embed_model import EmbeddingRetriever

class QAEngine:
    def __init__(self):
        self.qna = QAModel()
        self.retriever = EmbeddingRetriever()
        self.chunks = []

    def process_documents(self, all_chunks):
        self.chunks = all_chunks
        self.retriever.index_chunks(all_chunks)

    def ask(self, query):
        top_chunks = self.retriever.get_top_k_chunks(query)
        context = "\n".join(top_chunks)
        answer = self.qna.answer_question(context, query)
        return answer, top_chunks
