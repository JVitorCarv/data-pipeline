from sqlalchemy import create_engine, Column, DateTime, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
import csv
from datetime import datetime

db_host = "0.0.0.0" 
db_port = "5432"       
db_name = "etl-database"   
db_user = "postgres"  
db_password = "root"  
db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(db_url)

Base = declarative_base()

class WorldStockPrice(Base):
    __tablename__ = 'Stock Prices'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    dividends = Column(Float)
    stock_splits = Column(Float)
    brand_name = Column(String(50))
    ticket = Column(String(50))
    industry_tag = Column(String(50))
    country = Column(String(50))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

csv_file = 'raw_data/World-Stock-Prices-Dataset.csv'

try:
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            stock_price = WorldStockPrice(
                date=datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S%z'),
                open=float(row[1]),
                high=float(row[2]),
                low=float(row[3]),
                close=float(row[4]),
                volume=float(row[5]),
                dividends=float(row[6]),
                stock_splits=float(row[7]),
                brand_name=row[8],
                ticket=row[9],
                industry_tag=row[10],
                country=row[11]
            )
            session.add(stock_price)
    
    session.commit()
    print("CSV data has been transferred to the PostgreSQL table using SQLAlchemy ORM.")

except Exception as e:
    print(f"Error: {e}")
finally:
    session.close()
