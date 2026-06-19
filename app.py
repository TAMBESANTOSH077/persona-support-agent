import streamlit as st

from src.rag_pipeline import RAGPipeline
from src.classifier import PersonaClassifier
from src.generation import ResponseGenerator
from src.escalator import EscalationEngine

st.set_page_config(
    page_title="AI Customer Support Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Customer Support Agent")
st.write("Persona-Aware Support using RAG")

@st.cache_resource
def load_components():
    rag = RAGPipeline()
    classifier = PersonaClassifier()
    generator = ResponseGenerator()
    escalator = EscalationEngine()
    return rag, classifier, generator, escalator

rag, classifier, generator, escalator = load_components()

query = st.text_area(
    "Enter your support question",
    height=150,
    placeholder="Example: How do I reset my password?"
)

if st.button("Generate Response"):

    if query.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Processing..."):

        persona = classifier.classify(query)

        retrieved = rag.retrieve(query)

        response = generator.generate(
            persona["persona"],
            query,
            retrieved
        )

        escalate = escalator.should_escalate(
            persona["persona"],
            retrieved
        )

    st.success("Completed")

    st.subheader("Detected Persona")

    st.json(persona)

    st.subheader("Generated Response")

    st.write(response)

    if escalate:

        st.error("Escalation Required")

        st.write(
            escalator.escalation_message()
        )

    else:

        st.success("No Escalation Required")