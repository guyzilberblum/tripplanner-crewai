import requests
from langchain.tools import tool
import os 
import json
class SearchTool():
    @tool("Search The Web")
    def search_internet(query):
        """Useful to search the web for information.
        The input to this tool should be a query to search for.
        A couple of examples are "Who is the president of the USA?" or "What is the capital of France?" """
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': "application/json"
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        if 'organic' not in response.json():
            return "I'm sorry, I couldn't find any results for that query."
        else:
            results = response.json()['organic']
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}", f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}", "\n-------------------"
                    ]))
                except KeyError:
                        next
            return '\n'.join(string)        
        