from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

# helper function
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

@app.get("/")
def greet():
    return "Hello, This is Patient Management System"

@app.get("/about")
def about():
    return "This is a dynamic API for Patient Management for Doctors."

@app.get("/view")
def view():
    data  = load_data()
    return data

# Path Parameters with path() function
@app.get("/patient/{patient_id}")
def patient_view(patient_id: str = Path(..., description="Enter ID of the patient", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient Not Found")

# Query Parameter and Query() function
@app.get("/sort")
def patient_sort(sort_by:str = Query(..., description = 'sort on the basis of height, weight or bmi'),
                 order:str=Query('asc',description = 'Sort in asc or desc order')):
    valid_field = ['height','weight','bmi']
    if sort_by not in valid_field:
        raise HTTPException(status_code = 400, detail = f'Invalid field select from {valid_field}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code = 400, detail = 'Invalid order select between asc & desc')

    data = load_data()
    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x:x.get(sort_by,0), reverse=sort_order)
    return sorted_data