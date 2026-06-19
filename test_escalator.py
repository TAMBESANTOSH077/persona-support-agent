from src.rag_pipeline import RAGPipeline
from src.classifier import PersonaClassifier
from src.escalator import EscalationEngine

rag = RAGPipeline()
classifier = PersonaClassifier()
escalator = EscalationEngine()

query = "Nothing works! I am really frustrated."

persona = classifier.classify(query)

retrieved = rag.retrieve(query)

print("Persona:")
print(persona)

print()

if escalator.should_escalate(persona["persona"], retrieved):

    print("Escalation Required\n")

    print(escalator.escalation_message())

else:

    print("No Escalation Required")