from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os


def connect_to_mongodb(database_name, collection_name, mongo_uri):
    client = MongoClient(mongo_uri)
    db = client[database_name]
    collection = db[collection_name]
    return client, collection


def create_document(input_data):
    doc = {
        'text': input_data,
        'timestamp': datetime.utcnow()
    }
    return doc


def insert_documents(collection):
    while True:
        input_data = input("Enter the text, or type 'e' to exit:\n")
        if input_data.lower() == 'e':
            break

        doc = create_document(input_data)
        collection.insert_one(doc)
    print("All documents inserted successfully.")


def main():
    load_dotenv()

    database_name = os.getenv('DATABASE_NAME')
    collection_name = os.getenv('COLLECTION_NAME')
    mongo_uri = os.getenv('MONGO_URI')

    client, collection = connect_to_mongodb(
        database_name, collection_name, mongo_uri)
    insert_documents(collection)
    client.close()


if __name__ == '__main__':
    main()
