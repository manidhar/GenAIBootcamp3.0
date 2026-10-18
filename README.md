# GenAIBootcamp3.0

GenAI and agentic AI learnings using LangChain and Google ADK.

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Python 3.14 or newer (the project requirement configured in `pyproject.toml`)

## Set up the project

From the project root, sync the dependencies and create the virtual environment:

```bash
uv sync
```

Run the project with uv:

```bash
uv run python main.py
```

Run an example from the `01_LLMs` directory, for example:

```bash
uv run python 01_LLMs/1_llm.py
```

> **Warning:** Running `01_LLMs/4_chatmodel_hf_api.py` downloads the
> `HuggingFaceH4/zephyr-7b-beta` model (about 7 GB) to run locally. The initial
> download can take a considerable amount of time.
>
> **Note:** `01_LLMs/7_document_similarity.py` is currently not working as
> expected. Try `01_LLMs/8_gemini_document_similarity.py` to test similarity
> search instead.

## Configure API keys

Create a `.env` file in the project root. Add the credentials for the provider(s)
used by the example you want to run:

```dotenv
# Groq examples
GROQ_API_KEY=your_groq_api_key
GROQ_API_MODEL=openai/gpt-oss-120b
GROQ_API_BASE_URL=https://api.groq.com/openai/v1

# Google Gemini example
GOOGLE_API_KEY=your_google_api_key

# Hugging Face hosted inference example
HF_TOKEN=your_huggingface_token
```

The Groq examples use `GROQ_API_KEY`. `2_temperature.py` also reads
`GROQ_API_MODEL` and `GROQ_API_BASE_URL`; the values above match the example
configuration. `3_chatmodel_google.py` uses `GOOGLE_API_KEY`, and the hosted
Hugging Face example uses `HF_TOKEN`. You only need to fill in the keys for the
provider examples you intend to run. The local Hugging Face model and embedding
examples do not require API keys.

Keep `.env` private and never commit real API keys or tokens.
