install :
		# install commands
		pip install --upgrade pip && \
		pip install -r requirements.txt

format :
		# format code
		black Course5_DjangoWebFramework/*.py

lint :
		pylint --disable=R,C Course5_DjangoWebFramework/*.py

test :
		#

deploy :
		#

all :
		install, lint, test, deploy