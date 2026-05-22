from sentence_transformers import SentenceTransformer

_modelo = None

def get_model():
    """Devuelve el modelo, cargándolo solo la primera vez que se necesita."""
    global _modelo
    if _modelo is None:
        _modelo = SentenceTransformer('all-MiniLM-L6-v2')
    return _modelo

def embed_text(text: str):
    """Genera el embedding de un texto usando el modelo."""
    model = get_model()
    return model.encode(text)
