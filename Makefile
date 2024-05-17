# Makefile

.PHONY: help lint build up down test-env-up test-env-down test clean

help:
	@echo "Choose a command to run:"
	@echo "  lint            - Launch flake8"
	@echo "  up              - Run docker compose"
	@echo "  down            - Stop docker compose"
	@echo "  test-env-up     - Start test database"
	@echo "  test-env-down   - Stop test database"
	@echo "  test            - Run tests"
	@echo "  build           - Build the Docker image"
	@echo "  clean           - Clean up Docker containers and images"

lint:
	flake8 app tests

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

test-env-up:
	docker-compose -f tests/docker-compose.test-db.yml up -d

test-env-down:
	docker-compose -f tests/docker-compose.test-db.yml down

test: test-env-up
	@echo "Running tests..."
	poetry run pytest --cov=app --cov-report=html
	@$(MAKE) test-env-down

clean:
	docker-compose down --rmi all --volumes --remove-orphans
	docker-compose -f docker-compose.test-db.yml down --rmi all --volumes --remove-orphans

