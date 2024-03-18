# Currency worker

This is a Python project that fetches the current USD to UAH exchange rate and sends the data to Google Analytics.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Running the Application

You can run the application using Docker. Build the Docker image:

```bash
docker build -t currency-worker .
```

Then, run the Docker container:

```bash
docker run -d --env-file .env currency_worker 
```