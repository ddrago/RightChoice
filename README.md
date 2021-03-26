This is the project for the RightChoice project.
The dependencies for the project are included in requirements.txt file.
After the project has been cloned and dependencies installed,
pip install -r requirements.txt
it is required to SSH into the OpenStack cluster using this command:
ssh -N -L 5000:localhost:3306 -i se05key.pem ubuntu@130.209.251.52
The key is included in the git repository.
Once this connection is open, you can then run the server by using this command, ensuring you are in the correct directory:
cd se05-main/right_choice (assume currently in directory where git cloned)
python manage.py runserver
Then using any browser navigate to http://127.0.0.1:8000/
To access the database you need to be provided with a key, to request this please contact the group at 2389677W@student.gla.ac.uk.