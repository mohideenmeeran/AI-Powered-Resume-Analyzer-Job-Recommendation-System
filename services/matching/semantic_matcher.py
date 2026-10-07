from ml.embeddings import semantic_similarity


def calculate_semantic_match(
    resume_text: str,
    job_description: str,
) -> float:

    try:

        return semantic_similarity(
            resume_text,
            job_description,
        )

    except Exception:

        # Safe fallback if the transformer
        # cannot be loaded.
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity

        if not resume_text or not job_description:
            return 0.0

        vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        matrix = vectorizer.fit_transform(
            [resume_text, job_description]
        )

        similarity = cosine_similarity(
            matrix[0:1],
            matrix[1:2],
        )[0][0]

        return round(float(similarity * 100), 2)