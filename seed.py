from src.database import SessionLocal, engine
from src import models

# ensure tables exist before seeding
models.Base.metadata.create_all(bind=engine)


def seed_data():
    db = SessionLocal()

    # initial global locations
    locations = [
        {"country": "south africa", "currency": "ZAR"},
        {"country": "india", "currency": "INR"},
        {"country": "turkey", "currency": "TRY"},
        {"country": "china", "currency": "CNY"},
        {"country": "united states", "currency": "USD"},
        {"country": "european union", "currency": "EUR"},
        {"country": "australia", "currency": "AUD"}
    ]

    # initial bulk commodities
    commodities = [
        {"name": "heavy melting steel", "category": "scrap"},
        {"name": "shredded steel scrap", "category": "scrap"},
        {"name": "iron ore fines", "category": "raw material"}
    ]

    # insert locations into database
    for loc in locations:
        db_loc = models.Location(**loc)
        db.add(db_loc)

    # insert commodities into database
    for comm in commodities:
        db_comm = models.Commodity(**comm)
        db.add(db_comm)

    # commit transaction and close
    db.commit()
    db.close()
    print("database seeded successfully with global markets")


if __name__ == "__main__":
    seed_data()