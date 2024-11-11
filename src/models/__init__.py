from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from src.services.database import engine

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()    
    import src.models.user
    import src.models.event
    import src.models.email_broadcast
    
    print("Attempting to create tables...")
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully.")
    except Exception as e:
        print(f"Error during table creation: {e}")