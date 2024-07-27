from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinery(self, agent, city, date_range,interest):
        return Task(
            description=dedent(
                f"""
            **Task** : Develop a 7-day travel itinerary

            **Description** : Expand this guide into a a full 7-day travel 
        itinerary with detailed per-day plans, including 
        weather forecasts, places to eat, packing suggestions, 
        and a budget breakdown.
        
        You MUST suggest actual places to visit, actual hotels 
        to stay and actual restaurants to go to.
        
        This itinerary should cover all aspects of the trip, 
        from arrival to departure, integrating the city guide
        information with practical travel logistics.
        
        Your final answer MUST be a complete expanded travel plan,
        formatted as markdown, encompassing a daily schedule,
        anticipated weather conditions, recommended clothing and
        items to pack, and a detailed budget, ensuring THE BEST
        TRIP EVER, Be specific and give it a reason why you picked

            **Parameters** : 
            - City : {city}
            - Travel Date : {date_range}
            - Interest : {interest}

           **Note** : {self.__tip_section()}
              
        """
            ),
            agent=agent,
        )
    
    def gather_city_info(self, agent,city,interest,date_range):
        return Task(
            description=dedent(
                f"""
                   **Task** : Gather information about the city

                   **Description** :   As a local expert on this city you must compile an 
                      in-depth guide for someone traveling there and wanting 
                      to have THE BEST trip ever!
                      Gather information about  key attractions, local customs,
                      special events, and daily activity recommendations.
                      Find the best spots to go to, the kind of place only a
                      local would know.
                      This guide should provide a thorough overview of what 
                      the city has to offer, including hidden gems, cultural
                      hotspots, must-visit landmarks, weather forecasts, and
                      high level costs.
        
                      The final answer must be a comprehensive city guide, 
                      rich in cultural insights and practical tips, 
                      tailored to enhance the travel experience.

                  **Parameters** : 
                  - City : {city}
                  - Travel Date : {date_range}
                  - Interest : {interest}

                 **Note** : {self.__tip_section()}
            
        """
            ),
            agent=agent,
        )

    def identify_city(self, agent,origin,cities,interest,date_range):
        return Task(
            description=dedent(
                f"""
                   **Task** : identify the  best city for the travel itinerary

                   **Description** :  Analyze and select the best city for the trip based 
                        on the given criteria, including the origin, travel 
                        dates, interests, and budget.
                        Compare the cities based on factors such as weather, 
                        attractions, cost of living, and cultural experiences.
                        Provide a detailed recommendation for the best city to 
                        visit, including a rationale for your choice and a 
                        comparison of the other options.
            
                        The final answer must be a persuasive argument for 
                        the chosen city, supported by relevant data and 
                        insights, ensuring the traveler has THE BEST trip ever!

                  **Parameters** : 
                  -Origin : {origin}
                  - Cities : {cities}
                  - Travel Date : {date_range}
                  - Interest : {interest}

                 **Note** : {self.__tip_section()}
            
        """
            ),
            agent=agent,
        )