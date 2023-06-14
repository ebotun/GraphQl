import requests
import json
url: str = "http://localhost:5000/graphql"
body: str = """
{
  listPosts{
      post{
            title
            description
            created_at
      }
  }
}
"""

r = requests.post(url=url, json={"query": body})

if r.status_code == 200:
    json_object = json.loads(r.content.decode())
    res = json.dumps(json_object, indent=2)
    print(res)



