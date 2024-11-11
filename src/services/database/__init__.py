from sqlalchemy import create_engine, Engine
import os, ssl
from dotenv import load_dotenv

root_dir = os.path.abspath(os.path.join(os.path.dirname(__name__), "../../../.."))
dotenv_path = os.path.join(root_dir, ".env")

load_dotenv(dotenv_path)

engine = None

db_driver = os.environ.get("DB_CONNECTION", "mysql")

match db_driver:
    case "mysql":
        host = os.environ.get("MYSQL_HOST")
        port = os.environ.get("MYSQL_PORT")
        user = os.environ.get("MYSQL_USERNAME")
        password = os.environ.get("MYSQL_PASSWORD")
        database = os.environ.get("MYSQL_DATABASE")
        
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}", connect_args={
            "ssl": {
                "check_hostname": False,
                "verify_mode": ssl.CERT_NONE
            },
            "charset": "utf8mb4"
        })
        
    case "sqlite":
        engine = create_engine('sqlite:////tmp/test.db')