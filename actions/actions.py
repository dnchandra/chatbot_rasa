from typing import Text, List, Any, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionAskForSupport(Action):
    def name(self) -> Text:
        return "action_ask_for_support"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("How may I assist you? Please select below services which I offer.")
        return []

class ActionSelectInfrastructure(Action):
    def name(self) -> Text:
        return "action_select_infrastructure"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("You have selected Infrastructure.")
        dispatcher.utter_message("Report Production Issue\nCloud VM provisioning")
        return []

class ActionSelectDocumentation(Action):
    def name(self) -> Text:
        return "action_select_documentation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("You have selected Support Documentation.")
        dispatcher.utter_message("Shift Rota\nSupport Contacts")
        return []

class ActionCloudVMProvisioning(Action):
    def name(self) -> Text:
        return "action_cloud_vm_provisioning"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("You have selected Cloud VM provisioning.")
        return []

class ActionReportProductionIssue(Action):
    def name(self) -> Text:
        return "action_report_production_issue"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("You have selected Infrastructure.\nReport Production Issue")
        return []

class ActionProvideShiftRota(Action):
    def name(self) -> Text:
        return "action_provide_shift_rota"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("You can find the Shift Rota information [here](https://chat.bing.com).")
        return []

class ActionProvideSupportContacts(Action):
    def name(self) -> Text:
        return "action_provide_support_contacts"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("You can find the Support Contacts [here](https://chat.openai.com).")
        return []
