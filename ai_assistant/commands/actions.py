from krita import Krita


class ActionExecutor:

    @staticmethod
    def trigger(action_id: str) -> bool:
        """
        Execute a Krita action by its ID.
        Returns True if successful, False otherwise.
        """

        app = Krita.instance()

        action = app.action(action_id)

        if action is None:
            print(f"[AI Assistant] Action not found: {action_id}")
            return False

        if not action.isEnabled():
            print(f"[AI Assistant] Action disabled: {action_id}")
            return False

        action.trigger()
        return True