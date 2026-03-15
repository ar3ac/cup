from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import converters

app = FastAPI(title="C.U.P. - Converter Utility Program", version="1.0.0")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root():
    return RedirectResponse(url="/length")


@app.get("/length")
def get_length_form(request: Request):
    return templates.TemplateResponse("length.html", {"request": request})


@app.post("/length")
def convert_length(
    request: Request,
    value: float = Form(...),
    from_unit: str = Form(...),
    to_unit: str = Form(...),
):
    try:
        result = converters.convert_length(value, from_unit, to_unit)
        return templates.TemplateResponse(
            "length.html", {"request": request, "result": result}
        )
    except ValueError as e:
        return templates.TemplateResponse(
            "length.html", {"request": request, "error": str(e)}
        )


@app.get("/weight")
def get_weight_form(request: Request):
    return templates.TemplateResponse("weight.html", {"request": request})


@app.post("/weight")
def convert_weight(
    request: Request,
    value: float = Form(...),
    from_unit: str = Form(...),
    to_unit: str = Form(...),
):
    try:
        result = converters.convert_weight(value, from_unit, to_unit)
        return templates.TemplateResponse(
            "weight.html", {"request": request, "result": result}
        )
    except ValueError as e:
        return templates.TemplateResponse(
            "weight.html", {"request": request, "error": str(e)}
        )


@app.get("/temperature")
def get_temperature_form(request: Request):
    return templates.TemplateResponse("temperature.html", {"request": request})


@app.post("/temperature")
def convert_temperature(
    request: Request,
    value: float = Form(...),
    from_unit: str = Form(...),
    to_unit: str = Form(...),
):
    try:
        result = converters.convert_temperature(value, from_unit, to_unit)
        return templates.TemplateResponse(
            "temperature.html", {"request": request, "result": result}
        )
    except ValueError as e:
        return templates.TemplateResponse(
            "temperature.html", {"request": request, "error": str(e)}
        )
