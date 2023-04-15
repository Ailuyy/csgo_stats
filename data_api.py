import requests as rq
import pandas as pd

response = rq.get("https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key={API_KEY}&steamid={STEAM_ID}")
dic = response.json()
df = pd.DataFrame(dic)
df.to_json("main.json")
