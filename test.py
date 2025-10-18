from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import time

# Turkish embedding models (publicly available)
models_to_test = [
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    "dbmdz/bert-base-turkish-cased",
    "microsoft/mdeberta-v3-base",
]

test_query = "Genel Başkan nasıl seçilir?"
test_docs = [
    "Genel Başkan, parti kurultayı tarafından gizli oyla seçilir.",
    "Üyelik için minimum yaş 18'dir.",
    "Parti kongreleri yılda bir kez toplanır."
]

print("=" * 60)
print("🧪 TURKISH EMBEDDING MODEL COMPARISON")
print("=" * 60)

for model_name in models_to_test:
    try:
        print(f"\n🔍 Testing: {model_name}")

        # Load model
        start = time.time()
        model = SentenceTransformer(model_name)
        load_time = time.time() - start
        print(f"   Load time: {load_time:.2f}s")

        # Encode
        start = time.time()
        query_emb = model.encode(test_query)
        doc_embs = model.encode(test_docs)
        encode_time = time.time() - start
        print(f"   Encode time: {encode_time:.2f}s")
        print(f"   Dimension: {len(query_emb)}")

        # Calculate similarities
        similarities = cosine_similarity([query_emb], doc_embs)[0]

        print("\n   Similarities:")
        for i, (sim, doc) in enumerate(zip(similarities, test_docs)):
            print(f"   Doc {i + 1}: {sim:.4f} - {doc[:50]}...")

        print(f"\n   ✅ Best match: Doc {similarities.argmax() + 1}")

    except Exception as e:
        print(f"   ❌ Error: {str(e)[:100]}")
        continue

print("\n" + "=" * 60)
print("✅ Testing complete!")
print("=" * 60)