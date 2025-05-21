from arabic_nlp import normalize_arabic, remove_diacritics, retrieve_top_k, evaluate_retriever, hallucination_test

def test_normalize_arabic():
    input_text = "إِنَّ اللَّهَ غَفُورٌ رَحِيمٌ"
    expected = "ان الله غفور رحيم"
    assert normalize_arabic(remove_diacritics(input_text)) == expected

def test_remove_diacritics():
    input_text = "إِنَّ"
    expected = "إن"
    assert remove_diacritics(input_text) == expected

def test_retrieve_top_k():
    corpus = ["الطقس مشمس", "الجو ممطر", "السماء صافية"]
    query = "كيف هو الطقس؟"
    top_k = retrieve_top_k(query, corpus, k=2)
    assert len(top_k) == 2
    assert all(i in range(len(corpus)) for i in top_k)

# You can add more tests for evaluation functions and hallucination test similarly.
