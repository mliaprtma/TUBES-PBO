import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(
    "simobs-bengkel-firebase-adminsdk-fbsvc-8a002d20de.json"
)

firebase_admin.initialize_app(cred)

db = firestore.client()