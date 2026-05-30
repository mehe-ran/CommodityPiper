# use official python runtime
FROM python:3.12-slim

# set working directory
WORKDIR /app

# copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project files
COPY . .

# expose port
EXPOSE 8000

# run application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]