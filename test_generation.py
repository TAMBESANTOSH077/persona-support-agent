from src.rag_pipeline import RAGPipeline
from src.classifier import PersonaClassifier
from src.generation import ResponseGenerator

rag = RAGPipeline()
classifier = PersonaClassifier()
generator = ResponseGenerator()

query = "How do I reset my password?"

persona = classifier.classify(query)

retrieved = rag.retrieve(query)

response = generator.generate(
    persona["persona"],
    query,
    retrieved
)

print("\nDetected Persona:")
print(persona)

print("\nGenerated Response:\n")
print(response)