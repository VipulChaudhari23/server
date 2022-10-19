from flask import Flask, redirect, render_template, request, jsonify, url_for

from logic.Video_01 import createVideo01
from logic.Video_02 import createVideo02
from logic.Video_07 import createVideo07

form_elemets = {
    "templateVideo01": [
        {
            "id": "caption",
            "label": "Caption",
            "type": "text",
            "hint": "Caption"
        }
    ],
# Add parameters of the form as needed in the form as below
    "templateVideo02": [
        {
            "id": "bride_name",
            "label": "Bride Name",
            "type": "text",
            "hint": "Bride Name"
        },
        {
            "id": "bride_parent_name",
            "label": "Bride Parent Name",
            "type": "text",
            "hint": "Bride Parent Name"
        },
        {
            "id": "groom_name",
            "label": "Groom Name",
            "type": "text",
            "hint": "Groom Name"
        },
        {
            "id": "groom_parent_name",
            "label": "Groom Parent Name",
            "type": "text",
            "hint": "Groom Parent Name"
        }
    ],
    "templateVideo07": [
        {
            "id": "bride_name",
            "label": "Bride Name",
            "type": "text",
            "hint": "Bride Name"
        },
        {
            "id": "groom_name",
            "label": "Groom Name",
            "type": "text",
            "hint": "Groom Name"
        },
        {
            "id": "venue",
            "label": "Venue",
            "type": "text",
            "hint": "Venue"
        },
        {
            "id": "wedding_date",
            "label": "Wedding Date",
            "type": "date",
            "hint": "Wedding Date"
        }
    ],
}

application = Flask(__name__)
application.config["SECRET_KEY"] = 'jhdbjhabdklscsbcasbi87973y3jensjkdn984y3'


@application.route('/')
def index():
    return render_template('index.html')

# video name is the variable to declare the video name dynamically
# take data from form_fields and post theme

@application.route('/create/<video_name>')
def video(video_name):
    form_fields = form_elemets[video_name]
    return render_template('video.html', data={
        "video_name": video_name,
        "form_fields": form_fields,
    })

# Post the videos to the following python files

@application.route('/create-video', methods=["POST"])
def createVideo():
    video_name = request.form.get('video_name')
    print(request.form)
    url = ""
    ####################
    if video_name == 'templateVideo01':
        url = createVideo01(request.form.get('caption'))
    elif video_name == 'templateVideo02':
        url = createVideo02(request.form.get('bride_name'), request.form.get(
            'bride_parent_name'), request.form.get('groom_name'), request.form.get('groom_parent_name'))

    # create elif as the createVideo__ and parametters which are required in the Form as below

    elif video_name == 'templateVideo07':
        url = createVideo07(request.form.get('bride_name'), request.form.get(
            'groom_name'), request.form.get('venue'), request.form.get('wedding_date'))
    print(url)
    ########################
    return redirect(url_for('result', url = url))

@application.route('/result')
def result():
    return render_template('result.html', url = request.args['url'])

if __name__ == '__main__':
    # application.run(debug=True)
    application.run(host='0.0.0.0', port=8000, debug=True)
    # application.run(host='0.0.0.0', port=8000, debug=False)
