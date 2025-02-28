import argparse  # For command-line argument parsing
import psycopg2  # For PostgreSQL database connection
from datetime import datetime  # For handling date and time
import logging  # For logging messages

# Configure logging settings
logging.basicConfig(filename='automate_chatwoot.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Function to get a database connection
def get_database_connection(db_url: str):
    """
    Establish a connection to the PostgreSQL database.

    Args:
        db_url (str): The database URL.

    Returns:
        connection: A connection object to the PostgreSQL database.
    """
    try:
        return psycopg2.connect(db_url)
    
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
        raise

# Function to update the status of conversations
def update_status(db_url: str):
    """
    Update the status of conversations in the database.

    Args:
        db_url (str): The database URL.
    """
    try:
        # Get a database connection
        conn = get_database_connection(db_url)
        cursor = conn.cursor()
        
        # Get today's date in 'YYYY-MM-DD' format
        today = datetime.today().strftime('%Y-%m-%d')
        
        # SQL query to select conversations with specific statuses created today
        select_query = """
        SELECT * FROM conversations
        WHERE status IN (0, 2) AND DATE(created_at) = %s
        """
        
        # SQL query to update the status of selected conversations
        update_query = """
        UPDATE conversations
        SET status = 1
        WHERE status IN (0, 2) AND DATE(created_at) = %s
        """
        
        # Execute the select query
        cursor.execute(select_query, (today,))
        rows = cursor.fetchall()
        
        # If there are rows to update, execute the update query
        if rows:
            cursor.execute(update_query, (today,))
            conn.commit()
        
        # Close the database connection
        conn.close()
        logging.info("Status updated successfully.")
    
    except Exception as e:
        logging.error(f"Error updating status: {e}")
        raise

# Main function to handle command-line arguments and execute commands
def main():
    """
    Main function to parse command-line arguments and execute the appropriate command.
    """
    parser = argparse.ArgumentParser(description='Automate Chatwoot CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for the 'update_status' command
    update_parser = subparsers.add_parser('update_status', help='Update conversation statuses')
    update_parser.add_argument('--db-url', type=str, required=True, help='Database URL')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Execute the 'update_status' command if specified
    if args.command == 'update_status':
        try:
            update_status(args.db_url)
        except Exception as e:
            logging.error(f"Failed to update status: {e}")
            print(f"An error occurred: {e}")
    else:
        parser.print_help()

# Entry point of the script
if __name__ == '__main__':
    main()
