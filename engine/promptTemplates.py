from llama_index.core.prompts import PromptTemplate

df_info_str = """
App: Application name
Category: Category the app belongs to
Rating: Overall user rating of the app (as when scraped)
Reviews: Number of user reviews for the app (as when scraped)
Size: Size of the app (as when scraped)
Installs: Number of user downloads/installs for the app (as when scraped)
Type: Paid or Free
Price: Price of the app (as when scraped)
Content Rating: Age group the app is targeted at - Children / Mature 21+ / Adult
Genres: An app can belong to multiple genres (apart from its main category). For eg, a musical family game will belong to Music, Game, Family genres.
Last Updated: Date when the app was last updated on Play Store (as when scraped)
Current Ver: Current version of the app available on Play Store (as when scraped)
Android Ver: Min required Android version (as when scraped)
"""

instruction_str = (
    "1. Convert the query to executable Python code using Pandas.\n"
    "2. The final line of code should be a Python expression that can be called with the `eval()` function.\n"
    "3. The code should represent a solution to the query.\n"
    "4. GIVE ONLY THE EXPRESSION AND NOTHING ELSE AS AN ANSWER.\n"
    "5. SORT THE APPS ACCORDING TO RATINGS IN DECENDING ORDER IN EXPRESSION"
    "6. Do not quote the expression.\n"
    "7. The data is stored in the `df` variable"
    
)


pandas_prompt_tmplt = PromptTemplate(
    "You are working with a pandas dataframe in Python.\n"
    "The name of the dataframe is `df`.\n"
    "This is the result of `print(df.head())`:\n"
    "{df_str}\n\n"
    "This is the definition of all of the columns in the dataframe, there are no other columns besides this:\n"
    "{df_info_str}\n\n"
    "Follow these instructions:\n"
    "{instruction_str}\n"
    "Query: {query_str}\n\n"
    "Expression:"
)

response_synthesis_prompt_tmplt = PromptTemplate(
    "Given an input question, synthesize a response from the query results.\n"
    "Query: {query_str}\n\n"
    "Pandas Instructions (optional):\n{pandas_instructions}\n\n"
    "Pandas Output: {pandas_output}\n\n"
    "Response: "
)