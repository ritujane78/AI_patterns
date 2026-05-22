from typing import Annotated, Dict, List, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass
from autogen import ConversableAgent


config_list = {
    "model": "llama3.1:8b",
    "base_url": "http://localhost:11434/v1",
    "api_key": "ollama"
}

llm_config = {"config_list": config_list, "temperature": 0.0}
