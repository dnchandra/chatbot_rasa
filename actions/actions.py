from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction , Restarted

class ActionProvideInfrastructureOptions(Action):
    def name(self) -> Text:
        return "action_provide_infrastructure_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(text="Please select the type of infrastructure:",
        #                          buttons=[
        #                              {"title": "Cloud Infra", "payload": "/choose_infrastructure{\"infrastructure\":\"cloud_infra\"}"},
        #                              {"title": "Physical Infra", "payload": "/choose_infrastructure{\"infrastructure\":\"physical_infra\"}"}
        #                          ])
        # return []
        message = {
            "payload": "dropDown",
            "data": [
                {"label": "Cloud Infra", "value": "/choose_infrastructure{\"infrastructure\":\"cloud_infra\"}"},
                {"label": "Physical Infra", "value": "/choose_infrastructure{\"infrastructure\":\"physical_infra\"}"}
            ]
        }
        dispatcher.utter_message(json_message=message)
        return []


class ActionProvideCloudInfraOptions(Action):
    def name(self) -> Text:
        return "action_provide_cloud_infra_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:

            dispatcher.utter_message(text="Please choose a cloud infrastructure option:",
                                    buttons=[
                                        {"title": "Public Cloud", "payload": "/choose_cloud_infra{\"cloud_infra\":\"public_cloud\"}"},
                                        {"title": "Private Cloud", "payload": "/choose_cloud_infra{\"cloud_infra\":\"private_cloud\"}"},
                                        {"title": "Hybrid Cloud", "payload": "/choose_cloud_infra{\"cloud_infra\":\"hybrid_cloud\"}"}
                                    ])
            return []
        except Exception as e:
            # Log the exception if needed (e.g., print it or send it to a logging service)
            dispatcher.utter_message(text="Something went wrong, please contact Support.")
            # Optionally, you can reset the conversation by triggering the action_restart action
            return [FollowupAction("action_restart")]
        
class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [Restarted()]
    
