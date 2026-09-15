# Vendor Contract Compliance Auditor

### AI-Powered Vendor Contract Compliance Analysis System

An intelligent backend automation system that analyzes vendor contracts against corporate compliance rules using Artificial Intelligence, semantic search, and neural re-ranking.

---

## 📌 Project Overview

The **Vendor Contract Compliance Auditor** is an AI-based system designed to automate the process of checking vendor contracts against a company's compliance rulebook.

Traditional contract auditing requires manual reading and comparison of multiple documents. This project uses AI and Retrieval-Augmented Generation (RAG) techniques to identify relevant contract clauses, compare them with compliance rules, and generate audit reports.

The system focuses on efficient contract analysis, semantic retrieval, compliance checking, and automated reporting.

## 🎯 Project Objectives

* Automate vendor contract compliance auditing.
* Reduce manual contract review effort.
* Retrieve relevant contract clauses using semantic similarity.
* Identify potential compliance violations.
* Generate structured audit reports.
* Support large-scale contract analysis.

## ✨ Key Features

* **AI-Based Semantic Search:** Converts contract clauses into meaningful vector representations.
* **FAISS HNSW Indexing:** Enables efficient similarity-based retrieval.
* **Two-Stage RAG Pipeline:** Retrieves and re-ranks relevant contract clauses.
* **Neural Re-Ranking:** Uses a Cross-Encoder to improve relevance scoring.
* **Compliance Rulebook Analysis:** Compares contract content against corporate rules.
* **Automated PDF Reports:** Generates professional audit reports.
* **Analytics Graphs:** Visualizes compliance results and system performance.

## 🛠️ Technologies Used

| Technology            | Purpose                    |
| --------------------- | -------------------------- |
| Python                | Core development           |
| Sentence Transformers | Text embeddings            |
| FAISS                 | Vector indexing and search |
| RAG                   | Relevant clause retrieval  |
| Cross-Encoder         | Neural re-ranking          |
| ReportLab             | PDF report generation      |
| Matplotlib            | Analytics visualization    |
| NetworkX              | Architecture flowchart     |

## 🔄 System Workflow

```text
Vendor Contracts + Compliance Rulebook
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
        Audit Report + Graphs
```

## 📊 Project Analytics

### 1. Compliance Violation Breakdown

This graph shows the distribution of identified compliance violations across different categories.

![Compliance Violation Breakdown](output/graphs/compliance_violation_breakdown.png)

### 2. Contract Analysis Performance

This graph presents the performance comparison of different retrieval approaches used in the compliance auditing pipeline.

![RAG Precision Accuracy Comparison](output/graphs/rag_precision_comparison.png)

> Note: Graph filenames should match the actual files available in the `output/graphs/` folder.

## 📁 Project Structure

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

## ⚙️ Installation & Execution

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

## 📄 Output

The system generates:

* Automated compliance audit report in PDF format.
* Compliance violation analytics.
* Retrieval and re-ranking performance graphs.
* Contract analysis results.

## 👩‍💻 Author

**Ashwini Mali**

GitHub: https://github.com/Ashwini182006

---

### Disclaimer

This project is an AI-assisted compliance auditing tool. Its results are intended to support contract review and should be validated by qualified legal or compliance professionals before making final decisions.
