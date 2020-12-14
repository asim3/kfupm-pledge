#/bin/sh
if [ ! -d ./venv ]; then 
  python3 -m venv ./venv
fi;

source ./venv/bin/activate
cd ./pledge/


if [ "$1" = "install" ]; then
  pip3 install -r ../requirements.txt
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py runserver
elif [ "$1" = "newapp" ]; then
  python3 manage.py startapp $2
elif [ "$1" = "test" ]; then
  python3 manage.py test $2;
elif [ "$1" = "shell" ]; then
  python3 manage.py shell
elif [ "$1" = "user" ]; then
  python3 manage.py createsuperuser
elif [ "$1" = "help" ]; then
  echo "You can use:"
  echo "   ./run-me.sh install"
  echo "   ./run-me.sh newapp my_app"
  echo "   ./run-me.sh test"
  echo "   ./run-me.sh shell"
  echo "   ./run-me.sh user"
  echo "   ./run-me.sh"
else
  python3 manage.py runserver
fi

deactivate;
cd ..;
