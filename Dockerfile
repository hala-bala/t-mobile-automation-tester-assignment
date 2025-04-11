FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install chromium
RUN playwright install-deps chromium

# Copy project files
COPY . .

# Add current directory to PYTHONPATH
ENV PYTHONPATH=/app

# Set default command
CMD ["pytest", "tests/"]
