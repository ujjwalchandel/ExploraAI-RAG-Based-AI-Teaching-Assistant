from flask import Flask, render_template, url_for, request, jsonify
from process_query_with_GEMINI_3.py import final_response


app = Flask(__name__)


def get_course_data():
    """
    Sample in-memory data. Replace with a database in a real app.
    """
    return {
        "title": "Python for beginner",
        "description": "Learn Python for Data Science step by step with a sequence of short, focused video lessons.",
        "instructor": "Dr. Ujjwal Chandel",
        "lectures": [
            {
                "id": 1,
                "title": "Tuples, Lists, Aliasing, Mutability, and Cloning",
                "duration": "08:32",
                "thumbnail": "thumbnails/image.png",
                "video_path": "videos/MIT6_0001F16_Lecture_05_300k.mp4",
                "summary": "In this lecture, Dr. Bell introduces compound data types, such as lists and tuples, and explains the concepts of aliasing, mutability, and cloning."
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
        
        response = final_response(query)
    return jsonify({"message" : response})


if __name__ == "__main__":
    app.run(debug=True)


