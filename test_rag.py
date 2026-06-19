from src.rag_pipeline import RAGPipeline

rag = RAGPipeline()

rag.build_database()

result = rag.retrieve(
    "How do I reset my password?"
)

print("\nRetrieved Result:\n")

print(result)