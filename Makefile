install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

add-brain-games-to-path:
	export PATH=/Users/<user_name>/Library/Python/3.11/bin:$PATH

make lint:
	poetry run flake8 brain_games