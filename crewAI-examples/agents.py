from crewai import Agent
from tools.search_tools import SearchTool
from tools.calculator_tools import CalculatorTool
from textwrap import dedent
from langchain_openai import ChatOpenAI


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class Travelagents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(
            model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def expert_travel_agent(self):
        return Agent(
            role="Expert travel agent",
            backstory=dedent(f"""
                        I am a travel agent with over 20 years of experience in the travel industry."""),
            goal=dedent(f"""
                        Create a 7 day travel itinerary with detailed per-day plans,
                        include budget-friendly options, and provide a list of recommended activities and attractions and safety tips.

                        """),
            tools=[SearchTool.search_internet, CalculatorTool.calculate],

            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="city selection expert",
            backstory=dedent(f"""I am a city selection expert with over 20 years of experience in the travel industry."""),
            goal=dedent(f"""find the best city to travel to based on  whether season, budget, and interests"""),
            tools=[SearchTool.search_internet],
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    def local_tour_guide(self):
        return Agent(
            role="Local tour guide",
            backstory=dedent(f"""I am a local tour guide with over 20 years of experience in the travel industry."""),
            goal=dedent(f"""provide a detailed tour of the city, including the best places to eat, shop, and visit"""),
            tools=[SearchTool.search_internet],
            verbose=True,
            llm=self.OpenAIGPT35,
        )