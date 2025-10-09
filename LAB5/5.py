# Блок 1: matplotlib
try:
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("Графік")
    plt.savefig("grafik.png")
    plt.close()
    print("Графік збережено як grafik.png")
except Exception as e:
    print("Matplotlib error:", e)

# Блок 2: emoji
try:
    print(emoji.emojize("Привіт, Python :thumbs_up:"))
except Exception as e:
    print("Emoji error:", e)

# Блок 3: requests
try:
    r = requests.get("https://httpbin.org/get")
    print("Requests статус код:", r.status_code)
except Exception as e:
    print("Requests error:", e)

# Блок 4: numpy
try:
    arr = np.array([1, 2, 3, 4])
    print("Середнє значення масиву numpy:", np.mean(arr))
except Exception as e:
    print("Numpy error:", e)

# Блок 5: pandas
try:
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print("DataFrame pandas:\n", df)
except Exception as e:
    print("Pandas error:", e)
