from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

# Επιτρέπουμε αιτήματα από το frontend (π.χ. localhost:3002 ή όλα)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Μπορείς να το περιορίσεις π.χ. ["http://localhost:3002"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Μοντέλο εισόδου για το /greet endpoint
class NameRequest(BaseModel):
    name: str

# ✅ Root endpoint για να δείχνει κάτι στο "/"
@app.get("/")
def read_root():
    return {"message": "Το backend τρέχει σωστά με FastAPI 🚀"}

# POST endpoint που λαμβάνει όνομα και επιστρέφει χαιρετισμό
@app.post("/greet")
def greet(request: NameRequest):
    return {"message": f"Γεια σου, {request.name}!"}

# Εκκίνηση server όταν τρέχει το αρχείο απευθείας (για τοπική ανάπτυξη ή Render)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

