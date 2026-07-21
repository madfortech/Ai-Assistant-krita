import json

class Protocol:

    @staticmethod
    def parse(response):

        if response is None:
            return []

        if isinstance(response, str):
            response = json.loads(response)

        # NEW: text field me JSON string ho to parse karo
        if "text" in response:
            try:
                response = json.loads(response["text"])
            except Exception:
                return []

        return response.get("commands", [])