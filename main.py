"""
Supabase Database Demo - Insert Name and Favorite Color
"""
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# Get Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def get_supabase_client() -> Client:
    """Create and return a Supabase client."""
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("Please set SUPABASE_URL and SUPABASE_KEY in your .env file")
    
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def main():
    print("=== Supabase Database Demo ===\n")
    
    # Example usage - Replace with your actual data
    name = "John_Doe"  # Replace with your name_surname
    color = "Blue"     # Replace with your favourite_color
    
    print(f"Inserting: {name} with favorite color: {color}")
    
    try:
        # Initialize Supabase client
        supabase: Client = get_supabase_client()
        
        # Prepare data to insert
        data = {
            "name_surname": name,
            "favourite_color": color
        }
        
        # Insert data into the table (update 'your_table_name' with your actual table name)
        response = supabase.table("demotable").insert(data).execute()
        
        print("✅ Data inserted successfully!")
        print(f"Inserted: {data}")
        print(f"Response: {response.data}")
    
    except Exception as e:
        print(f"❌ Error inserting data: {e}")
        raise

if __name__ == "__main__":
        main()
