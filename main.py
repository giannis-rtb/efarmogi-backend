from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

# Επιτρέπουμε CORS ΜΟΝΟ από το Vercel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://efarmogi-frontend.vercel.app"],  # <-- Εδώ περιορίζουμε σωστά
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Μοντέλο εισόδου για το /greet endpoint
class NameRequest(BaseModel):
    name: str

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Το backend τρέχει σωστά με FastAPI 🚀"}

# POST endpoint που λαμβάνει όνομα και επιστρέφει χαιρετισμό
@app.post("/greet")
def greet(request: NameRequest):
    return {"message": f"Γεια σου, {request.name}!"}

# Εκκίνηση server (για Render & local)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

