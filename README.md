# Haverford CS Unofficial Guide — RAG App

A retrieval-augmented generation (RAG) chatbot that answers questions about Haverford College's CS department using informal, student-sourced knowledge that official channels don't surface: course difficulty, professor teaching styles, grading policies, and the course lottery system.

---

## Architecture

![Architecture Diagram](arch_diagram.png)

---

## Motivation

I didn't know the CS course lottery existed until I got to campus — even though it's on the registrar's website. Most of the actually useful information, like which courses are difficult, what professors are like, and how grading works, comes from word of mouth or only becomes available once you're already enrolled. I built this to make that knowledge searchable.

---

## Tech Stack

| Layer | Tool |
|---|---|
| Embedding model | `all-MiniLM-L6-v2` (sentence-transformers) |
| Vector store | ChromaDB |
| LLM | `llama-3.3-70b-versatile` via Groq API |
| UI | Gradio |
| Language | Python |

---

## Pipeline

**1. Ingestion** — 12 sources collected and cleaned into `.txt` files, including Rate My Professor reviews, Reddit threads, the Haverford course catalog, registrar lottery guidelines, and a student-published open letter about faculty shortages.

**2. Chunking** — Two strategies applied based on document structure:
- *Paragraph splitting* for structured sources (RMP reviews, course requirements, the registrar page) where meaning lives within paragraphs
- *Fixed-length chunking* (400–600 chars, 100-char overlap) for Reddit, where formatting is inconsistent
- Overflow guard: paragraphs exceeding the size limit fall back to fixed-length splitting

**3. Embedding + Storage** — Chunks embedded with `all-MiniLM-L6-v2` and stored in ChromaDB with source metadata for attribution.

**4. Retrieval** — Top-k=10 similarity search. Started at k=5; raised to 10 after end-to-end testing showed CS105/106 placement guidance only entered the retrieval window at k=10.

**5. Generation** — Groq-hosted Llama 3.3 70B generates answers grounded strictly in retrieved chunks. System prompt: *"Answer the question using only the information in the provided documents. If the documents don't contain enough information to answer, say 'I don't have enough information on that.'"* Sources (URLs) are surfaced alongside every answer.

**6. Interface** — Gradio web UI: type a question, get an answer with source links.

---

## Evaluation

5 test questions run end-to-end:

| Question | Result |
|---|---|
| What is CS245 about? | Accurate — Principles of Programming Languages |
| What is Professor Wonacott like? | Accurate — mixed reviews: friendly but long-winded |
| What is the course lottery like? | Accurate — detailed procedural + student experience |
| What is the CS department like? | Partially accurate — theoretical, supportive, hit-or-miss |
| What courses should a first-year take? | Accurate — CS105/106 placement guidance recovered at k=10 |

**Known failure mode:** The system correctly refuses questions where the corpus has no data (e.g., CS240 course description) — grounding is working as intended. The main gap is sparse coverage of individual course descriptions.

---

## Key Design Decisions

- **Mixed chunking strategy** rather than one-size-fits-all, because review corpora and structured pages have fundamentally different semantic density
- **k=10 retrieval** chosen empirically — k=5 caused refusals on valid questions; k=10 recovered them without introducing irrelevant noise
- **Strict grounding prompt** to prevent hallucination; the model declines rather than fabricates when context is insufficient
- **Source attribution in ChromaDB metadata** so every answer links back to its origin

---

## Sources

| # | Source |
|---|---|
| 1–2 | Haverford registrar (lotteries, CS major/minor requirements) |
| 3 | Haverford course catalog |
| 4 | Student publication — open letter on CS faculty shortage |
| 5–9 | Rate My Professor (Wonacott, Lindell, Nguyen, Dougherty, Friedler) |
| 10–11 | Reddit (r/Pennsylvania, r/Haverford) |
| 12 | College Confidential |

---

## Running Locally

```bash
pip install -r requirements.txt

# Ingest and chunk documents
python ingest.py

# Embed chunks and build ChromaDB index
python embed.py

# Launch Gradio UI
python app.py
```

Set your Groq API key in the environment before running:

```bash
export GROQ_API_KEY=your_key_here
```
