from fastapi import FastAPI

app=FastAPI()


@app.get("/sap")
def main():
    return dict(name="SAP service")