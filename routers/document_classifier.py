from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

DOCUMENT_KEYWORDS = {
    "W2": ["w2", "w-2", "w_2"],
    "BankStatement": ["bank", "statement", "transactions"],
    "PayStub": ["paystub", "pay", "salary"]
}

class FileList(BaseModel):
    filenames: List[str]

    class Config:
        schema_extra = {
            "example": {
                "filenames": ["w2_2023.pdf", "bank_jan.csv", "paystub.pdf"]
            }
        }
    

@router.post("/classify-document")
def classify_docs(input: FileList):
    results = []
    for name in input.filenames:
        name_lower = name.lower()
        found = False
        for doc_type, keywords in DOCUMENT_KEYWORDS.items():
            if any(k in name_lower for k in keywords):
                results.append(doc_type)
                found = True
                break
        if not found:
            results.append("Unknown")
    return {"results": results}

# POST /classify-document
# { "filenames": ["w2_2023.pdf", "bank.csv", "paystub.pdf"] }
# Response
# { "results": ["W2", "BankStatement", "PayStub"] }
