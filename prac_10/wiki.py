def search_wikipedia():
    """Prompt the user for Wikipedia page titles and display summary and URL until a blank entry is given."""
    user_input = input("Enter page title (or press Enter to quit): ").strip()
    while user_input:
        try:
            page = wikipedia.page(user_input, auto_suggest=False)
            print(f"\nTitle: {page.title}\n")
            print(f"Summary: {page.summary[:500]}...\n")  # Avoid 2nd API call
            print(f"URL: {page.url}\n")
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f'Page title "{user_input}" does not exist. Try another.')
        except Exception as ex:
            print("An error occurred:", ex)

        user_input = input("\nEnter another page title (or press Enter to quit): ").strip()

    print("Thank you.")
