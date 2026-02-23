from fastapi import FastAPI, HTTPException
from schemas import Student
from database import collection
from bson import ObjectId

app = FastAPI()

@app.get('/')
def hello():
    return{'message':'Hellow server is running'}

@app.post("/students")
async def create_student(student: Student):
    student_data = student.dict()
    result = await collection.insert_one(student_data)

    return {
        "message": "Student created",
        "id": str(result.inserted_id)
    }

@app.get("/students")
async def get_students():
    students = []
    async for student in collection.find():
        student["_id"] = str(student["_id"])
        students.append(student)
    return students

@app.put("/students/{id}")
async def update_student(id: str, student: Student):
    result = await collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": student.dict()}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student updated"}

@app.delete("/students/{id}")
async def delete_student(id: str):
    result = await collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted"}

