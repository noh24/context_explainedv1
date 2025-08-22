
# Context Explained

A Python project for generating structured daily Bible readings using OpenAI and storing lessons in a database. Includes scheduling, API integration, and deployment support.

## Features
- Generates daily Bible lessons with historical, theological, and reflective sections
- Uses OpenAI API for lesson generation
- Stores lessons in a database (PostgreSQL or SQLite)
- Scheduler for automated lesson creation
- Environment-based configuration
- Ready for deployment (e.g., AWS Lambda)

## Project Structure
```
app/
	config.py         # Loads environment variables and settings
	db.py             # Database setup and session management
	db_models/
		lesson.py       # SQLAlchemy model for lessons
	openai_client.py  # Handles OpenAI API requests
	schemas/
		lesson_data.py  # Pydantic schema for lesson data
		reference.py    # Pydantic schema for passage references
main.py             # Main script for lesson generation
lambda_function.py  # AWS Lambda handler for lesson generation
schedule.py         # APScheduler job for automated runs
requirements.txt    # Python dependencies
.env                # Environment variables (not tracked by git)
.gitignore          # Files and folders to ignore in git
```

## Setup
1. Clone the repository:
	 ```bash
	 git clone https://github.com/noh24/context_explainedv1.git
	 cd context-explained
	 ```
2. Create and activate a virtual environment:
	 ```bash
	 python -m venv .venv
	 source .venv/Scripts/activate  # On Windows
	 source .venv/bin/activate      # On Mac/Linux
	 ```
3. Install dependencies:
	 ```bash
	 pip install -r requirements.txt
	 ```
4. Create a `.env` file (see `.env.example` if provided) and fill in your API keys and database URLs.

## Usage
- **Run main script:**
	```bash
	python main.py
	```
- **Run scheduler:**
	```bash
	python schedule.py
	```
- **Deploy to AWS Lambda:**
	Use `lambda_function.py` as your handler and package dependencies as needed.

## Configuration
All settings are managed via environment variables in `.env`:
- `OPENAI_API_KEY`: Your OpenAI API key
- `DATABASE_URL`: Database connection string
- `MODEL_NAME`: OpenAI model name
- `TIMEZONE`: Timezone for scheduling
- `LESSON_PROMPT`: Prompt template for lesson generation
- `LOCAL_DB_URL`: Local SQLite database URL

## Contributing
Pull requests and issues are welcome! Please follow standard Python style and add tests for new features.

## License
MIT License

## Author
Brian Noh
