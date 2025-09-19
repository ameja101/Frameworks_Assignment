import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud
import streamlit as st

# -------------------------------
# Load cleaned dataset
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("metadata_sample.csv", low_memory=False)

    # Convert publish_time to datetime
    if "publish_time" in df.columns:
        df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
        df["year"] = df["publish_time"].dt.year

    # Abstract word count
    if "abstract" in df.columns:
        df["abstract_word_count"] = (
            df["abstract"].fillna("").apply(lambda x: len(str(x).split()))
        )
    return df

df = load_data()

# -------------------------------
# Streamlit Layout
# -------------------------------
st.title("CORD-19 Research Metadata Explorer")
st.write("An interactive dashboard to explore COVID-19 research papers.")

st.sidebar.header("Filters")
year_min = int(df["year"].dropna().min()) if "year" in df.columns else 2019
year_max = int(df["year"].dropna().max()) if "year" in df.columns else 2025
year_range = st.sidebar.slider("Select Year Range", year_min, year_max, (year_min, year_max))

df_filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# -------------------------------
# Show data sample
# -------------------------------
st.subheader("Sample of Data")
st.write(df_filtered.head())

# -------------------------------
# Publications over time
# -------------------------------
if "year" in df_filtered.columns:
    st.subheader("Publications Over Time")
    year_counts = df_filtered["year"].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(10,5))
    sns.lineplot(x=year_counts.index, y=year_counts.values, marker="o", ax=ax)
    ax.set_title("Number of Publications Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Papers")
    st.pyplot(fig)

# -------------------------------
# Top Journals
# -------------------------------
if "journal" in df_filtered.columns:
    st.subheader("Top Journals")
    top_n = st.sidebar.slider("Number of Top Journals", 5, 20, 10)
    top_journals = df_filtered["journal"].value_counts().head(top_n)

    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(x=top_journals.values, y=top_journals.index, palette="viridis", ax=ax)
    ax.set_title(f"Top {top_n} Journals Publishing COVID-19 Research")
    ax.set_xlabel("Number of Papers")
    ax.set_ylabel("Journal")
    st.pyplot(fig)

# -------------------------------
# Word Cloud of Titles
# -------------------------------
if "title" in df_filtered.columns:
    st.subheader("Word Cloud of Paper Titles")
    all_titles = " ".join(df_filtered["title"].dropna().astype(str))
    words = [w.lower() for w in all_titles.split()]
    word_freq = Counter(words)
    wc = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_freq)

    fig, ax = plt.subplots(figsize=(12,6))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

# -------------------------------
# Paper counts by Source
# -------------------------------
if "source_x" in df_filtered.columns:
    st.subheader("Distribution of Papers by Source")
    source_counts = df_filtered["source_x"].value_counts()

    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(x=source_counts.index, y=source_counts.values, palette="magma", ax=ax)
    ax.set_title("Distribution of Papers by Source")
    ax.set_xlabel("Source")
    ax.set_ylabel("Number of Papers")
    plt.xticks(rotation=45)
    st.pyplot(fig)

st.write("✅ Dashboard complete!")
