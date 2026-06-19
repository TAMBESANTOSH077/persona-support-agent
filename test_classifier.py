from src.classifier import PersonaClassifier

classifier = PersonaClassifier()

queries = [
    "Our API keeps returning HTTP 401 Unauthorized.",
    "Nothing works! I'm really frustrated.",
    "How will this issue affect business operations?"
]

for query in queries:

    print("\nUser:", query)

    result = classifier.classify(query)

    print(result)