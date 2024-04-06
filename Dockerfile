FROM python:3.10

COPY requirements.txt code/requirements.txt

# Set the working directory to /code
WORKDIR /code

# Install requirements.txt 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the current directory contents into the container at .
COPY . .

ENV PORT 7860

# Start the FastAPI app on port 7860, the default port expected by Spaces
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
