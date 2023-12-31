import os

db_host = os.environ.get('DB_HOST', default='localhost') ## localhost should be replaced by the private ip address of the DB Cloud Server
db_name = os.environ.get('DB_NAME', default='dashboard')
db_password = os.environ.get('DB_PASSWORD', default='secure_password')
db_port = os.environ.get('DB_PORT', default='5432')
db_user = os.environ.get('DB_USERNAME', default='dashboard')

SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
