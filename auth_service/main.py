from fastapi import FastAPI

app=FastAPI()


@app.get("/auth")
def main():
    return dict(name="auth service")