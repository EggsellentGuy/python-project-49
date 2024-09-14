install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install-pipx:
	pipx install --force dist/*.whl

package-install-pip:
	pip install --force dist/*.whl
	
lint:
	poetry run flake8 brain_games
