from app.analyzer import analyze_error

error = "ValueError: Input contains NaN, check your training data"

response = analyze_error(error)
print(response)