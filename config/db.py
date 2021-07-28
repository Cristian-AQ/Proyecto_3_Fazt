from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymsql://root:1234@127.0.0.1:3306/storedb")
conn = engine.connect()