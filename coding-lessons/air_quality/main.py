import fetch
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    url = "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=49.2&longitude=9.2&hourly=pm10,pm2_5&timezone=Europe%2FBerlin&forecast_days=1"
    data = fetch.fetch_data(url)
    print(data["hourly"]["pm10"][0])
    df = pd.DataFrame(data["hourly"])
    print(df.to_string())
    df.plot()
    plt.show()
