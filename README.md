Manual Testing Performed:

- Added multiple sticky notes via the menu
- Viewed notes successfully
- Edited an existing note
- Deleted a note
- Tested invalid menu options
- Tested deleting a non-existing note

## Running with a virtual environment

1. Create a virtual environment:
   python -m venv venv

2. Activate it:
   venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run migrations:
   python manage.py migrate

5. Start server:
   python manage.py runserver

## Running with Docker

1. Build the image:
   docker build -t sticky-notes-app .

2. Run the container:
   docker run -p 8000:8000 sticky-notes-app
