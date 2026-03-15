from fastapi import FastAPI, HTTPException

import converters
from schemas import ConversionRequest, ConversionResponse

app = FastAPI(title="C.U.P. - Converter Utility Program", version="1.0.0")


@app.post("/convert/length", response_model=ConversionResponse)
def convert_length(request: ConversionRequest):
    try:
        result = converters.convert_length(
            request.value, request.from_unit, request.to_unit
        )
        return ConversionResponse(result=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/convert/weight", response_model=ConversionResponse)
def convert_weight(request: ConversionRequest):
    try:
        result = converters.convert_weight(
            request.value, request.from_unit, request.to_unit
        )
        return ConversionResponse(result=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/convert/temperature", response_model=ConversionResponse)
def convert_temperature(request: ConversionRequest):
    try:
        result = converters.convert_temperature(
            request.value, request.from_unit, request.to_unit
        )
        return ConversionResponse(result=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
