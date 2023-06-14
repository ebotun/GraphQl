import requests
import json
url: str = "http://localhost:5000/graphql"
body: str = """
mutation {
    createPost(title: "snickers420", description: "bounty"){
        post{
            id
            title
            description
            created_at
        }
        success
    }
}
"""

r = requests.post(url=url, json={"query": body})

if r.status_code == 200:
    json_object = json.loads(r.content.decode())
    res = json.dumps(json_object, indent=2)
    print(res)



