import os
import warnings

# Suppress Hugging Face warnings and clutter
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
warnings.filterwarnings("ignore")

import pandas as pd
from ann.embedder import TextEmbedder
from ann.hnsw_index import HNSWVectorIndex
from rag.retriever import ANNRetriever
from rag.reranker import CrossEncoderReranker
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

try:
    from google.colab import files
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

def generate_pdf_report(audit_data: list, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc = SimpleDocTemplate(output_path, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=16, textColor=colors.HexColor('#1e3c72'), spaceAfter=15, alignment=1)
    normal_style = styles['Normal']
    
    elements = []
    elements.append(Paragraph("HNSW ANN + Cross-Encoder RAG Compliance Audit Report", title_style))
    elements.append(Paragraph("Advanced Vector Graph Retrieval & Precision Re-ranking Pipeline (10k Dataset)", styles['Italic']))
    elements.append(Spacer(1, 15))

    table_data = [["Compliance Rule", "Vendor", "Top Reranked Clause", "Relevance Score"]]
    for item in audit_data:
        table_data.append([
            Paragraph(item["compliance_rule"], normal_style),
            Paragraph(str(item["matched_vendor"]), normal_style),
            Paragraph(item["contract_clause"], normal_style),
            f"{item['rerank_score']:.2f}"
        ])

    t = Table(table_data, colWidths=[120, 90, 250, 60])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e3c72')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f7f9fa')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    
    elements.append(t)
    doc.build(elements)
    print(f"-> Success: PDF Audit Report saved at {output_path}")

def main():
    print("--- Running HNSW ANN + Cross-Encoder Pipeline ---")
    
    csv_path = "data/contracts.csv"
    rulebook_path = "data/rulebook.txt"
    
    if not os.path.exists(csv_path) or not os.path.exists(rulebook_path):
        print("Error: Missing contracts.csv or rulebook.txt in data/ folder.")
        return

    df = pd.read_csv(csv_path)
    docs = df.to_dict(orient="records")

    # 1. Embedder & HNSW Indexing
    embedder = TextEmbedder()
    embeddings = embedder.encode_texts([d["clause_text"] for d in docs])
    
    hnsw_index = HNSWVectorIndex(dimension=384, M=32)
    hnsw_index.build_index(embeddings, docs)

    # 2. Retriever & Cross-Encoder Reranker
    retriever = ANNRetriever(embedder, hnsw_index)
    reranker = CrossEncoderReranker()

    with open(rulebook_path, "r", encoding="utf-8") as f:
        rules = [line.strip() for line in f if line.strip()]

    audit_results = []
    for rule in rules:
        candidates = retriever.retrieve(rule, top_k=3)
        best_matches = reranker.rerank(rule, candidates, top_n=1)
        
        for match in best_matches:
            audit_results.append({
                "compliance_rule": rule,
                "matched_vendor": match.get("vendor_name"),
                "contract_clause": match.get("clause_text"),
                "rerank_score": match.get("rerank_score")
            })

    output_pdf = "output/audit_report.pdf"
    generate_pdf_report(audit_results, output_pdf)

    if IN_COLAB:
        files.download(output_pdf)
    else:
        print("-> Pipeline executed cleanly and finished!")

if __name__ == "__main__":
    main()