from PyQt5.QtCore import QSettings

ORGANIZATION = "AI Assistant"
APPLICATION = "AI Assistant Plugin"

TIMEOUT = 120


def get_settings():
    return QSettings(ORGANIZATION, APPLICATION)


def save_api_url(url):
    settings = get_settings()
    settings.setValue("api_url", url)


def get_api_url():
    settings = get_settings()
    return settings.value(
        "api_url",
        "https://aiassistant.test/api/generate"
    )


def save_api_key(key):
    settings = get_settings()
    settings.setValue("api_key", key)


def get_api_key():
    settings = get_settings()
    return settings.value("api_key", "")