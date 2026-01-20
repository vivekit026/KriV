from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="KriV - Medical Chatbot API",
    description="AI-powered medical assistant (Educational Use Only)",
    version="0.1.0"
)

# CORS (for mobile app later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "KriV API is running",
        "disclaimer": "Not a medical diagnosis. Consult a doctor."
    }

@app.get("/health")
def health_check():
    return {"status": "OK"}

