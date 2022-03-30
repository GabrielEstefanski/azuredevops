import json
import pandas as pd
from requests_pkcs12 import get

df = []


def get_request(url) -> str:
    response = get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Basic <token>111111111111111111111111111111111111111111111111111111111111111111111",
        },
        verify=False,
    )

    return json.loads(response.content.decode("utf-8"))


def search(data) -> None:
    for values in data["value"]:
        df.append(
            [
                values["id"],
                values["name"],
                values["url"],
                values["state"],
                values["revision"],
                values["visibility"],
            ]
        )

    dataframe = pd.DataFrame(
        df, columns=["id", "name", "url", "state", "revision", "visibility"]
    )
    print(dataframe)


data = get_request("https://dev.azure.com/desenv2rp/_apis/projects?")
resp = search(data)
