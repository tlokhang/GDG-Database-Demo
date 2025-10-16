# GDG-Database-Demo

A Python project to connect to Supabase and insert user data (name_surname and favourite_color).

## Prerequisites

- Python 3.11+
- A Supabase account and project
- Supabase URL and anon/service key

## Setup

1. **Clone or open this project**

2. **Install dependencies** (already done if using the virtual environment):
   ```bash
   pip install supabase python-dotenv
   ```

3. **Configure environment variables**:
   - Copy `.env.example` to `.env`
   - Add your Supabase credentials:
     ```
     SUPABASE_URL=https://your-project.supabase.co
     SUPABASE_KEY=your-anon-key-here
     ```

4. **Create a Supabase table**:
   - Go to your Supabase dashboard
   - Navigate to the SQL Editor or Table Editor
   - Create a table with the following structure:
     ```sql
     CREATE TABLE your_table_name (
       id BIGSERIAL PRIMARY KEY,
       name_surname TEXT NOT NULL,
       favourite_color TEXT NOT NULL,
       created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
     );
     ```
   - Update the table name in `main.py` (line 37)

## Usage

1. Open `main.py`
2. Update the table name on line 37: `supabase.table("your_table_name")`
3. Update your name and favorite color in the `main()` function (lines 50-51)
4. Run the script:
   ```bash
   python main.py
   ```

## Project Structure

- `main.py` - Main script to insert data into Supabase
- `.env` - Environment variables (not tracked in git)
- `.env.example` - Example environment variables template
- `.gitignore` - Git ignore file
- `README.md` - This file

## Example Output

```
=== Supabase Database Demo ===

Inserting: John_Doe with favorite color: Blue
✅ Data inserted successfully!
Inserted: {'name_surname': 'John_Doe', 'favourite_color': 'Blue'}
Response: [{'id': 1, 'name_surname': 'John_Doe', 'favourite_color': 'Blue', 'created_at': '2025-10-16T...'}]
```

## Troubleshooting

- **Missing credentials**: Ensure your `.env` file exists and contains valid Supabase credentials
- **Table not found**: Make sure you've created the table in Supabase and updated the table name in `main.py`
- **Connection error**: Verify your Supabase URL and key are correct