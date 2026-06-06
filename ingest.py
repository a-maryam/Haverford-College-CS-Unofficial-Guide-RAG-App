"""
Milestone 3 — Document ingestion and chunking.

Implements the Chunking Strategy from planning.md:
  - Reddit threads      -> fixed-length chunking (people write in weird/inconsistent
                           formats, so paragraph boundaries are unreliable there).
  - Everything else     -> paragraph chunking (reviews, requirements, the article, and
                           the lottery page carry most of their meaning per-paragraph).

Parameters (from planning.md):
  - Fixed chunk size: 400-600 chars  -> using 500 (midpoint of the range)
  - Overlap:          100 chars
"""

from pathlib import Path
import re

# --- Configuration (from planning.md "Chunking Strategy") ---------------------
DOCS_DIR = Path(__file__).parent / "documents"

FIXED_CHUNK_SIZE = 500   # midpoint of the planned 400-600 char range (Reddit)
FIXED_OVERLAP = 100      # planned 100 char overlap


# --- Loading ------------------------------------------------------------------
def load_documents(docs_dir=DOCS_DIR):
    """Load every .txt file in `docs_dir`.

    Returns a list of dicts: {"source": <filename>, "text": <file contents>}.
    """
    docs = []
    for path in sorted(Path(docs_dir).glob("*.txt")):
        text = path.read_text(encoding="utf-8")
        if text.strip():  # skip empty files
            docs.append({"source": path.name, "text": text})
    return docs


# --- Chunking methods ---------------------------------------------------------
# Paragraphs longer than this are split further with the fixed-length chunker so
# no single chunk swallows several reviews. 600 = top of the planned 400-600 range.
PARAGRAPH_MAX_CHARS = 600


def fixed_length_chunk(text, chunk_size=FIXED_CHUNK_SIZE, overlap=FIXED_OVERLAP):
    """Split `text` into fixed-length character chunks with overlap.

    Slides a window of `chunk_size` characters across the text, stepping forward
    by (chunk_size - overlap) each time so consecutive chunks share `overlap`
    characters of context.
    """
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    text = text.strip()
    chunks = []
    step = chunk_size - overlap
    for start in range(0, len(text), step):
        chunk = text[start:start + chunk_size].strip()
        if chunk:
            chunks.append(chunk)
        if start + chunk_size >= len(text):
            break  # last window already reached the end
    return chunks


def paragraph_chunk(text, max_chars=PARAGRAPH_MAX_CHARS):
    """Split `text` into chunks on paragraph (blank-line) boundaries.

    A "paragraph" is a run of text separated by one or more blank lines.
    Surrounding whitespace is stripped and empty paragraphs are dropped.

    Some sources (e.g. RateMyProfessor exports) pack many reviews into one
    blank-line-free block, which would otherwise become a single huge chunk.
    Any paragraph longer than `max_chars` is split further with the
    fixed-length chunker so no chunk swallows several reviews.
    """
    # Split on one or more blank lines (handles \n\n and lines of only whitespace).
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]

    chunks = []
    for para in paragraphs:
        if len(para) > max_chars:
            chunks.extend(fixed_length_chunk(para))
        else:
            chunks.append(para)
    return chunks


# --- Routing ------------------------------------------------------------------
def is_reddit(source):
    """Reddit documents use fixed-length chunking; identified by filename."""
    return "reddit" in source.lower()


def chunk_document(doc):
    """Apply the appropriate chunker to a single document based on its source.

    Returns a list of dicts: {"source", "method", "chunk_index", "text"}.
    """
    if is_reddit(doc["source"]):
        method = "fixed"
        chunks = fixed_length_chunk(doc["text"])
    else:
        method = "paragraph"
        chunks = paragraph_chunk(doc["text"])

    return [
        {"source": doc["source"], "method": method, "chunk_index": i, "text": chunk}
        for i, chunk in enumerate(chunks)
    ]


# --- Main: load, chunk, and report --------------------------------------------
def main():
    documents = load_documents()
    print(f"Loaded {len(documents)} documents from {DOCS_DIR}\n")

    all_chunks = []
    for doc in documents:
        chunks = chunk_document(doc)
        all_chunks.extend(chunks)
        method = chunks[0]["method"] if chunks else "?"
        print(f"  {doc['source']:<32} -> {method:<9} ({len(chunks)} chunks)")

    print(f"\nTotal chunks: {len(all_chunks)}")
    for i in range(45, 51):
        print(all_chunks[i])
        print("\n")
    return all_chunks


if __name__ == "__main__":
    main()
