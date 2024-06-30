# session_manager.py

class SessionManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SessionManager, cls).__new__(cls)
            cls._instance.full_name = ""
        return cls._instance

    def set_full_name(self, full_name):
        self.full_name = full_name
        print(f"SessionManager: full_name set to {self.full_name}")

    def get_full_name(self):
        print(f"SessionManager: full_name retrieved as {self.full_name}")
        return self.full_name

# Singleton instance
session_manager = SessionManager()
