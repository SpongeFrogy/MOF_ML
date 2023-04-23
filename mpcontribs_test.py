from mpcontribs.client import Client
client = Client()
c = client.get_contribution("6196c6e8a6be6ad338993956")
print(c.display())