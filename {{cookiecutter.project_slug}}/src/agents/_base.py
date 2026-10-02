import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

load_dotenv()


def get_llm() -> BaseChatModel:
    model = os.getenv("LLM_MODEL")
    if not model:
        raise RuntimeError(
            "LLM_MODEL is not set. Copy .env.example to .env and fill it in."
        )
    provider = os.getenv("LLM_PROVIDER") or None
    base_url = os.getenv("LLM_BASE_URL")
    kwargs = {"base_url": base_url} if base_url else {}

    return init_chat_model(model, model_provider=provider, **kwargs)
