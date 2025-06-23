from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

# Επιτρέπουμε αιτήματα από το frontend (π.χ. localhost:3002 ή όλα)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Μπορείς να το κάνεις ["http://localhost:3002"] για μεγαλύτερη ασφάλεια
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Το μοντέλο των δεδομένων που περιμένει το backend
class NameRequest(BaseModel):
    name: str

# Endpoint POST για υποδοχή ονόματος
@app.post("/greet")
def greet(request: NameRequest):
    return {"message": f"Γεια σου, {request.name}!"}

# Εκκίνηση του server (για το Render)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
