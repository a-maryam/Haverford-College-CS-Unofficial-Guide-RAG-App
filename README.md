# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
I'm choosing a CS Course selection and survival guide for Haverford College. I want to span the 
CS course lottery, difficulty of courses, professor course structure and grading policies. This sort of 
knowledge is mostly informal. You find out which courses are tough by word of mouth and you only get 
grading info and course insights if you enroll and get a syllabus. I don't think I was aware of the 
CS course lottery until I got to campus; even though it is on the registrar's website.
---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

Note about document ingestion: I copied in the documents into txt files and cleaned them manually (it wasn't much)

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | Haverford College Website | Information about course lotteries | https://www.haverford.edu/registrar/lotteries | 
| 2 | College Confidential | Information about CS course difficulty and 4+1 | https://talk.collegeconfidential.com/t/math-computer-science-4-1-w-upenn/1869266 |
| 3 | Rate My Professor | Prof Wonacott's RMP | https://www.ratemyprofessors.com/professor/752469 |
| 4 | RMP | Steven Lindell RMP | https://www.ratemyprofessors.com/professor/2238783 |
| 5 | Reddit | Is Haverford good for CS? | https://www.reddit.com/r/Pennsylvania/comments/10630z4/is_haverford_college_decent_for_comp_sci_looking/ |
| 6 | Student-run Campus Publication | Letter about Shortage | https://haverfordclerk.com/open-letter-on-the-shortage-of-computer-science-faculty/ |
| 7 | RMP | RMP Prof. Dung Nguyen | https://www.ratemyprofessors.com/professor/3122048 |
| 8 | RMP | RMP John Dougherty | https://www.ratemyprofessors.com/professor/2349369 |
| 9 | RMP | Sorelle Friedler RMP | https://www.ratemyprofessors.com/professor/2041582 |
| 10 | Reddit | How are CS/math depts? | https://www.reddit.com/r/Haverford/comments/1kkygm5/how_is_the_computer_science_and_math_departments/ |
| 11 | Haverford website | Requirements | https://www.haverford.edu/academics/computer-science-major-minor-and-concentration | 
| 12 | Haverford Course Catalog | Course Catalog | https://www.haverford.edu/computer-science/courses/course-catalog |


---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

     chunking reddit, college confidential, and professor reviews may be similar. I think that chunking the requirements page, an article, and the course lottery page might be different. 

     Paragraph splitting seems good for college confidential, professor reviews, requirements, the article and lottery page. I think most of the meaning bites will be in a pragraph. I think for reddit I would use fixed chunking because people can write in weird formats at times. 

     Prompted Claude some: big chunks hurt opinion reviews because a large chunk size will swallow several reviews (loss of meaning). So, it is 
     good that I had decided to use paragraph splitting. Chunk size for reddit
     could hurt us potentially, but I feel like the overlap gives some safety.
     I'm expecting some repercussions though.

**Chunk size:**
     400-600. (Reddit, will use paragraph splitting otherwise)

**Overlap:**

     100 chars

**Reasoning:**
     400-600 chars looks like a reasonable size chunk for reddit; I looked at visuals of char counts online. 100 chars overlap seems like it would capture meaningful idea boundaries.

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Embedding model:**
all-MiniLM-L6-v2 from sentence-transformers should be fine

**Top-k:**
I am going to try 5 chunks at first and maybe add some more if answers are poor. Too many adds irrelavent info.

Final: top-k = 10. I started at 5, but end-to-end testing showed the first-year-courses question refused at k=5 (and k=8) because the CS105/106 placement chunk only entered the retrieval window at k=10. Raising it recovered that answer.

**Production tradeoff reflection:**
(Had claude help) There are better models for student informal language and slang like text-embedding-3-large or Voyage/Cohere. Another embedding model could be useful for the long requirements and course lottery pages. 
---

# Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
Only answer based on the content provided. Do not use outside 
sources to answer questions. 

**How source attribution is surfaced in the response:**
We added a sources array to embed.py and the sources metadata lives in chromadb. metadata is grabbed on retrieval and attached to the answer. 

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What is CS245 about? | Programming Languages | Principles of Programming Languages. | Relevant | Accurate | 
| 2 | What is Professor Wonacott like? | Student reviews are mixed. He is noted as being friendly, not the best at teaching, and long-winded.  | mixed, with some students finding him to be an excellent teacher and others struggling with his lecture style.| Relevant | Accurate |
| 3 | What is the course lottery like at Haverford? | The lottery can be stressful because you are not guaranteed a course, but if you stick through it usually it's ok. | Very detailed info about lottery + student experiences summed up | Relevant | Accurate |
| 4 | What is the CS department like? | Generally nice. Pretty theoretical over applied. | Considered to not be one of the best but with its strengths | Relevant | Partially accurate |
| 5 | What courses should a first-year student take to start CS, and are they difficult? | Start with CS105/106 depending on background. CS105 is introductory and approachable; CS106 requires more background. Both are foundational before jumping into theory-heavy courses like CS245. Workload is moderate but consistent. | According to the provided documents, a first-year student should take introductory CS courses to start CS. The specific courses mentioned are CMSC H106, H107, or B151| Relevant | Accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**
What is CS245 about? (Partial Fail - lacking detail)

**What the system returned:**
Principles of Programming Languages

**Root cause (tied to a specific pipeline stage):**
Documents not having enough detail. Ultimately, with retrieval, we just get the name of the course.

**What you would change to fix it:**
Have more documents describing the courses, so the model would have more to serve users.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
It seems Claude really understood the planning.md well and
was able to give a decent implementation.

**One way your implementation diverged from the spec, and why:**
I had Claude generate ingest.py, and it found that one of the files
that I had decided to paragraph split became a big chunk 
because spacing was not present for some reason
so I told Claude that if a paragraph is too big then we will use
the fixed-length chunker.

Was planning on using top-5 retrieval, but one of the questions
only had enough info with top-8, so everything was upgraded to top-8
retrieval.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
Planning.md, Can you use planning.md as a basis to write a script to load all the documents from docs, define a method for paragraph chunking, define a method for fixed-length chunking as per parameters in planning.md? Do the previous as functions, then make the appropriate calls to paragraph chunk and fixed-length chunk respectively as define.

- *What it produced:*
Wrote the chunking based on paragraph + length.
- *What I changed or overrode:*
It suggested that we add a extra strategy that if we have too large of a paragraph it gets chunked fixed-length; I thought that was a good idea and integrated it.

**Instance 2**

- *What I gave the AI:*
Read the Retrieval Approach section in planning.md and look at the diagram (Architecture Diagram). Can you implement the embedding which is loading the chunks from the ingestion script, embedding with all-MiniLM-l6-v2, and storing in ChromaDB with the metadata. And write a retrieval function.
- *What it produced:*
Embed.py which gets Chromadb set up with the chunks and metadata and retrieves. 
- *What I changed or overrode:*
 Keep this code and load up all evaluation questions from planning.md as a sample question array in the main