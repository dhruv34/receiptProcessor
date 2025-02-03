# Receipt Processor

1. Build Docker image: `docker build -t receipt-processor .`
2. Run Docker container: `docker run -p 8000:8000 receipt-processor`
3. API is now running at http://localhost:8000

API Usage:
- POST /receipts/process with receipt JSON in body to get a receipt id
- GET /receipts/{id}/points to retrieve number of points for receipt with id