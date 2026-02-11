# MathViz

MathViz is a Django app that turns math text or images into LaTeX using the Gemini API, then renders the LaTeX into a PNG with Matplotlib.

## Features
- Text to LaTeX and rendered image
- Drawing canvas to LaTeX
- Image upload to LaTeX

## Local Setup
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the repo root:
   ```
   GEMINI_API_KEY=your_key_here
   DJANGO_SECRET_KEY=your_secret_here
   DEBUG=true
   DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
   ```
4. Run migrations:
   ```bash
   python math_viz_backend/manage.py migrate
   ```
5. Start the server:
   ```bash
   python math_viz_backend/manage.py runserver
   ```
6. Open `http://127.0.0.1:8000/`

## Routes
- `/drawer/` (draw)
- `/uploader/` (upload)
- `/about/`

## Notes
- The Gemini model name must be available for your API key. If you see `api_error`, verify model access.
- `.env` is ignored by git
