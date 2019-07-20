install:
	docker-compose -f docker-compose.build.yml run --rm install

quick-up:
	docker-compose -f docker-compose.build.yml run --rm quick-up

dev-build:
	docker build --no-cache -t whirlpool-urlfilter-dev:latest --target whirlpool-urlfilter-dev .

prod-build:
	docker build --no-cache -t whirlpool-urlfilter-prod:latest --target whirlpool-urlfilter-prod .

dev-up:
	docker-compose -f dev-docker-compose.yml up --build -d

prod-up:
	docker-compose -f prod-docker-compose.yml up --build -d

dev-logs:
	docker-compose -f dev-docker-compose.yml logs -f

prod-logs:
	docker-compose -f prod-docker-compose.yml logs -f

push-dev:
	docker push rihbyne/whirlpool-urlfilter-dev:latest

push-prod:
	docker push rihbyne/whirlpool-urlfilter-prod:latest
