import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# Create the connection
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("contacts.sqlite")

# Open the connection
if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)

# Create a query and execute it right away using .exec()
createTableQuery = QSqlQuery()
createTableQuery.exec(
    """
    CREATE TABLE contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(40) NOT NULL,
        job VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )
    """
)

# Creating a query for later execution using .prepare()
insertDataQuery = QSqlQuery()
insertDataQuery.prepare(
    """
    INSERT INTO contacts (
        name,
        job,
        email
    )
    VALUES (?, ?, ?)
    """
)

# Sample data
data = [
    ("Nick", "Moustache Groomer", "nickselleck@fake.com"),
    ("Dylan", "Pizza Enthusiast", "pp@twitch.amazonprime"),
    ("Jordan", "Afternoon Napper", "nightowl@piczo.com"),
    ("Blaine", "The Bread AND the Butter", "thatsitfolks@helpme.com"),
    ("John", "Toddler Wrangler/Instructor", "whendo-i-sleep@cna.ed.nl")
]

# Use .addBindValue() to insert data
for name, job, email in data:
    insertDataQuery.addBindValue(name)
    insertDataQuery.addBindValue(job)
    insertDataQuery.addBindValue(email)
    insertDataQuery.exec()

con.close()