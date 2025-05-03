from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
my_variable = os.getenv("Host")
print(my_variable)