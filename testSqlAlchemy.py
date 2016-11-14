from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine.reflection import Inspector 
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:MephiMoscow533!@127.0.0.1/?port=3306')
res = engine.execute("SHOW DATABASES")
for row in res:
    print(row)

meta = MetaData(engine)
engine.execute("USE test")

insp = Inspector.from_engine(engine)
table_names = insp.get_table_names('performance_schema')

print(table_names)
