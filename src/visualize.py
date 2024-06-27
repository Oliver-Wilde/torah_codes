def visualize_search_results(name, results):
    for pos, skip, context, translated_context in results:
        print(f"Position: {pos}, Skip: {skip}")
        print(f"Context: {context[:50]}...")  # Show only the first 50 characters of the context
        print(f"Translated Context: {translated_context[:50]}...")  # Show only the first 50 characters of the translated context
        print("-" * 50)

if __name__ == "__main__":
    name = "example"
    results = [(12345, 7, "example context here", "translated context here")]
    visualize_search_results(name, results)
