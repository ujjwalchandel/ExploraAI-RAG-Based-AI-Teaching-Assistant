from flask import Flask, render_template, url_for, request

app = Flask(__name__)


def get_course_data():
    """
    Sample in-memory data. Replace with a database in a real app.
    """
    return {
        "title": "Python for Beginners",
        "description": "Learn Python step by step with a sequence of short, focused video lessons.",
        "instructor": "Dr. Jane Doe",
        "lectures": [
            {
                "id": 1,
                "title": "Introduction & Setup",
                "duration": "08:32",
                "thumbnail": "thumbnails/sddefault.webp",
                "video_path": "videos/lecture1.mp4",
                "summary": "Overview of the course, tools you need, and how to follow along."
            },
            {
                "id": 2,
                "title": "Python Basics: Variables & Types",
                "duration": "12:10",
                "thumbnail": "thumbnails/sddefault.webp",
                "video_path": "videos/lecture2.mp4",
                "summary": "Understanding variables, basic data types, and simple operations."
            },
            {
                "id": 3,
                "title": "Control Flow: If, For, While",
                "duration": "15:45",
                "thumbnail": "thumbnails/sddefault.webp",
                "video_path": "videos/lecture3.mp4",
                "summary": "Learn how to make decisions and repeat actions with control statements."
            },
            {
                "id": 4,
                "title": "Functions & Modules",
                "duration": "14:05",
                "thumbnail": "thumbnails/sddefault.webp",
                "video_path": "videos/lecture4.mp4",
                "summary": "Organize your code with functions and reuse logic across files."
            },
        ],
    }


@app.route("/", methods = ["GET", "POST"])
def index():

    course = get_course_data()

    # Prepend static URLs for thumbnails and videos
    for lecture in course["lectures"]:
        lecture["thumbnail_url"] = url_for("static", filename=lecture["thumbnail"])
        lecture["video_url"] = url_for("static", filename=lecture["video_path"])

    
    return render_template("index.html", course=course)


@app.route("/process", methods = ["GET", "POST"])
def process():
    if request.method == "POST":
        message = request.get_json()
        query = message["query"]
        print(query)


if __name__ == "__main__":
    app.run(debug=True)


