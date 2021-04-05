This is the project for the RightChoice project.
================================================================================

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
This permission notice shall be included in all copies or substantial 
portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

================================================================================
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
