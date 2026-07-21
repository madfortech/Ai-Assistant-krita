import json
import ssl
from urllib.request import Request, urlopen
from .settings import (
    get_api_url,
    get_api_key,
    TIMEOUT,
)

def generate(prompt):

    api_url = get_api_url()
    api_key = get_api_key()


    data = json.dumps({
    "prompt": prompt,
    "platform": "krita"
}).encode("utf-8")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    print("URL:", repr(api_url))
    print("KEY:", repr(api_key))
    print("HEADERS:", headers)

    request = Request(
        api_url,
        data=data,
        headers=headers,
        method="POST"
    )

    context = ssl._create_unverified_context()

    with urlopen(request, timeout=TIMEOUT, context=context) as response:

        body = response.read().decode("utf-8")

        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(None, "API Response", body)

        return json.loads(body)

def me():

    api_url = get_api_url().replace("/generate", "/me")
    api_key = get_api_key()

    headers = {
        "Accept": "application/json",
    }

    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    request = Request(
        api_url,
        headers=headers,
        method="GET"
    )

    context = ssl._create_unverified_context()

    with urlopen(request, timeout=TIMEOUT, context=context) as response:
        return json.loads(response.read().decode("utf-8"))