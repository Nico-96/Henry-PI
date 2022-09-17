import uvicorn
from fastapi import FastAPI
from router import circuito, carrera, pilotos, resultado

app=FastAPI()

app.include_router(circuito.router)
app.include_router(carrera.router)
app.include_router(pilotos.router)
app.include_router(resultado.router)


@app.get("/")
def root():
    return{"Hello":"World"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)