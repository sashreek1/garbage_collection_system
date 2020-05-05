import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('firebase-test-4b2e17880be1.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def send_data(data):
	db.collection(u'dustbin').add(data)

def get_data():
	users_ref = db.collection(u'dustbin')
	docs = users_ref.stream()
	doc_list = []
	for doc in docs:
		data = doc.to_dict()
		print(data)
		doc_list.append(data)

	return doc_list
