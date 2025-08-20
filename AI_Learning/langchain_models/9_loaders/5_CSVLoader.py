from langchain_community.document_loaders import CSVLoader

# Provide path to your CSV file
loader = CSVLoader(file_path="email-test_credentials.csv")

# Load documents (each row becomes a document)
docs = loader.load()

# Print information
print("Number of documents loaded:", len(docs))
print("First document content:\n", docs[0].page_content)
print("Metadata:\n", docs[0].metadata)
