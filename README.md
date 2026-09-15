# Vendor Contract Compliance Auditor

## AI-Powered Vendor Contract Compliance Analysis System

Vendor Contract Compliance Auditor is an AI-based backend system that helps analyze vendor contracts according to company compliance rules. It uses semantic search, AI models, and a RAG-based approach to find relevant contract clauses and check them against the compliance rulebook.

The main purpose of this project is to make contract checking easier and reduce the time required for manual review.

## Project Objectives

* To automate vendor contract compliance checking.
* To reduce manual contract review work.
* To find relevant contract clauses using semantic search.
* To identify possible compliance issues.
* To generate audit reports automatically.
* To support the analysis of multiple vendor contracts.

## Key Features

### 1. Semantic Search

The system converts contract clauses into vector representations and searches for relevant information based on meaning.

### 2. FAISS HNSW Indexing

FAISS HNSW is used to search similar contract clauses efficiently.

### 3. RAG Pipeline

The project uses a two-stage RAG pipeline to retrieve relevant clauses and improve the search results.

### 4. Neural Re-Ranking

A Cross-Encoder is used to re-rank the retrieved clauses and improve their relevance.

### 5. Compliance Rulebook Analysis

The system compares contract information with the company's compliance rules and identifies possible violations.

### 6. PDF Audit Reports

The project generates PDF reports containing contract analysis and compliance results.

### 7. Analytics Graphs

Graphs are generated to show compliance violations and compare retrieval performance.

## Technologies Used

| Technology            | Purpose                    |
| --------------------- | -------------------------- |
| Python                | Main programming language  |
| Sentence Transformers | Text embeddings            |
| FAISS                 | Vector search and indexing |
| RAG                   | Relevant clause retrieval  |
| Cross-Encoder         | Neural re-ranking          |
| ReportLab             | PDF report generation      |
| Matplotlib            | Graphs and visualization   |
| NetworkX              | Architecture flowchart     |

## System Workflow

Vendor Contracts and Compliance Rulebook

↓

Text Preprocessing

↓

Sentence Embeddings

↓

FAISS HNSW Index

↓

Relevant Clause Retrieval

↓

Cross-Encoder Re-Ranking

↓

Compliance Evaluation

↓

Audit Report and Graphs

## Project Analytics

### 1. Compliance Violation Breakdown

This graph shows the different categories of compliance violations found during contract analysis.

Graph file:

`output/graphs/compliance_violation_breakdown.png`

### 2. Contract Analysis Performance

This graph compares the performance of different retrieval methods used in the contract compliance analysis.

Graph file:

`output/graphs/rag_precision_comparison.png`

Note: The graph filenames should match the actual files available in the `output/graphs/` folder.

## Project Structure

```text
vendor_compliance_auditor/
│
├── data/
│   ├── contracts.csv
│   └── rulebook.txt
│
├── ann/
│   ├── __init__.py
│   ├── embedder.py
│   └── hnsw_index.py
│
├── rag/
│   ├── __init__.py
│   ├── retriever.py
│   └── reranker.py
│
├── output/
│   ├── audit_report.pdf
│   └── graphs/
│
├── tests.py
├── generate_all_graphs.py
├── requirements.txt
├── main.py
└── README.md
```

## Installation and Execution

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd vendor_compliance_auditor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Tests

```bash
python tests.py
```

### 4. Run the Compliance Auditor

```bash
python main.py
```

### 5. Generate Analytics Graphs

```bash
python generate_all_graphs.py
```

## Output

After running the project, the system generates:

* Compliance audit report in PDF format.
* Compliance violation graphs.
* Retrieval and re-ranking performance graphs.
* Contract analysis results.



## Author

**Ashwini Mali**

GitHub:https://github.com/Ashwini182006

## Disclaimer
This project is an AI-assisted contract compliance auditing tool. The results are meant to support contract review. Final decisions should be checked by qualified legal or compliance professionals.

This project is an AI-assisted contract compliance auditing tool. The results are meant to support contract review. Final decisions should be checked by qualified legal or compliance professionals.
