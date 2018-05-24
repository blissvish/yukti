import wolframalpha

input_ = input("Question: ")
app_id = "3UU3P8-7PWA3PYLUH"
client = wolframalpha.Client(app_id)

res = client.query(input_)
answer = next(res.results).text

print(answer)
