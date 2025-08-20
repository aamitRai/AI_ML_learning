from langchain_community.tools import DuckDuckGoSearchRun
search_tool=DuckDuckGoSearchRun()
results=search_tool.invoke('plane crash')
print("results",results)