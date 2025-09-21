run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

build:
	docker build -t ade/portfolio-api:local .

start:
	docker run -p 8000:8000 ade/portfolio-api:local

scan:
	trivy image ade/portfolio-api:local || true
