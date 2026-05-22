# La funcionalidad de embeddings ha sido desactivada temporalmente para
# ahorrar memoria en el plan gratuito de Render.
# Para habilitarla, restaura este archivo con la versión original y considera
# usar un plan de pago o una API externa de embeddings.

import logging

logger = logging.getLogger(__name__)

def embed_text(text: str):
    """Stub de embed_text – no hace nada y advierte."""
    logger.warning("La función embed_text no está disponible en este momento.")
    raise NotImplementedError(
        "La funcionalidad de embeddings está desactivada. "
        "Consulta con el administrador para habilitarla."
    )
