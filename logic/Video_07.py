import os
import time
from requests import get, post
from requests.auth import HTTPBasicAuth

def createVideo07(bride_name, groom_name, venue, wedding_date):
    headers = {'Authorization': 'Token 4b6a7b35dd9e04cf889eb996933e16499b2f23ca'}
    r = get("http://13.235.139.86/", headers=headers)
    PATH = os.path.dirname(os.path.realpath(__file__))
    CLOUD_URL = 'http://13.235.139.86/'
    CLOUD_AUTH = HTTPBasicAuth('Celebrare-Openshot', 'openshot')

    # project Endpoint

    end_point = '/projects/'
    r = get(CLOUD_URL + end_point, auth=CLOUD_AUTH)
    # print(r.json())

    #Project Name
    end_point = '/projects/'
    project_data = {
        "name": "Video_07",
        "width": 1920,
        "height": 1080,
        "fps_num": 30,
        "fps_den": 1,
        "sample_rate": 44100,
        "channels": 2,
        "channel_layout": 3,
        "json": "{}",
    }
    r = post(CLOUD_URL + end_point, data=project_data, auth=CLOUD_AUTH)
    print(r.json())
    project_id = r.json().get("id")
    project_url = r.json().get("url")

    #file (image1)
    end_point = '/projects/%s/files/' % project_id
    source_path = os.path.join(PATH, "assets/Video 07/bg.jpg")
    source_name = os.path.split(source_path)[1]
    file_data = {
        "media": None,
        "project": project_url,
        "json": "{}"
    }
    r = post(CLOUD_URL + end_point, data=file_data, files={"media": (source_name, open(source_path, "rb"))}, auth=CLOUD_AUTH)
    file_url = r.json().get("url")
    # print(r.json())

    # file Clip (image1)
    end_point = '/projects/%s/clips/' % project_id
    clip_data = {
        "file": file_url,
        "position": 0.0,
        "start": 0.0,
        "end": 15.0,
        "layer": 1,
        "project": project_url,
        "json": "{}"
    }
    r = post(CLOUD_URL + end_point, data=clip_data, auth=CLOUD_AUTH)
    # print(r.json())

    #Title Wedding Invitation
    end_point = '/projects/%s/title/' % project_id
    file_data = {
        "template": "Center-Text.svg",
        "text": "Wedding Invitation",
        "font_size": 100.0,
        "font_name": "Bewilder Thick BRK",
        "fill_color": "#FF5349",
        "fill_opacity": 1.0,
        "stroke_color": "#000000",
        "stroke_size": 0.0,
        "stroke_opacity": 0.0,
        "drop_shadow": False,
        "background_color": "#000000",
        "background_opacity": 0.0
    }
    r = post(CLOUD_URL + end_point, data=file_data, files={"media": (source_name, open(source_path, "rb"))}, auth=CLOUD_AUTH)
    file_url = r.json().get("url")
    # print(r.json())

    # Title Clip (Wedding Invitation)
    end_point = '/projects/%s/clips/' % project_id
    clip_data = {
        "file": file_url,
        "position": 0.0,
        "start": 0.0,
        "end": 6.0,
        "layer": 2,
        "project": project_url,
        "json": '{"alpha": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 31, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 61, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 121, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 181, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "anchor": 0, "channel_filter": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "channel_mapping": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "display": 0, "duration": 0, "effects": [], "gravity": 4, "has_audio": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "has_video": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_y": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "mixing": 0, "origin_x": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "origin_y": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "parentObjectId": "", "perspective_c1_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c1_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "reader": {"acodec": "", "audio_bit_rate": 0, "audio_stream_index": -1, "audio_timebase": {"den": 1, "num": 1}, "channel_layout": 4, "channels": 0, "display_ratio": {"den": 9, "num": 16}, "duration": 3600, "file_size": "8294400", "fps": {"den": 1, "num": 30}, "has_audio": false, "has_single_image": true, "has_video": true, "height": 1080, "interlaced_frame": false, "metadata": {}, "path": "/home/ubuntu/api/video/files/39/title-9c73769d.svg", "pixel_format": -1, "pixel_ratio": {"den": 1, "num": 1}, "sample_rate": 0, "top_field_first": true, "type": "QtImageReader", "vcodec": "QImage", "video_bit_rate": 0, "video_length": "108000", "video_stream_index": -1, "video_timebase": {"den": 30, "num": 1}, "width": 1920, "media_type": "image"}, "rotation": {"Points": []}, "scale": 1, "scale_x": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "scale_y": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_y": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "time": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "volume": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "wave_color": {"alpha": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "blue": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "green": {"Points": [{"co": {"X": 1, "Y": 123}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "red": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}}, "waveform": false, "title": "title-9c73769d.svg"}'
    }
    r = post(CLOUD_URL + end_point, data=clip_data, auth=CLOUD_AUTH)
    # print(r.json())

    #Title Neha Sharma
    end_point = '/projects/%s/title/' % project_id
    file_data = {
        "template": "Center-Text.svg",
        "text": bride_name,
        "font_size": 100.0,
        "font_name": "Bewilder Thick BRK",
        "fill_color": "#FF5349",
        "fill_opacity": 1.0,
        "stroke_color": "#000000",
        "stroke_size": 0.0,
        "stroke_opacity": 0.0,
        "drop_shadow": False,
        "background_color": "#000000",
        "background_opacity": 0.0
    }
    r = post(CLOUD_URL + end_point, data=file_data, files={"media": (source_name, open(source_path, "rb"))}, auth=CLOUD_AUTH)
    file_url = r.json().get("url")
    # print(r.json())

    # Title Clip (Neha Sharma)
    end_point = '/projects/%s/clips/' % project_id
    clip_data = {
        "file": file_url,
        "position": 6.0,
        "start": 6.0,
        "end": 15.0,
        "layer": 3,
        "project": project_url,
        "json": '{"alpha": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "anchor": 0, "channel_filter": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "channel_mapping": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "display": 0, "duration": 0, "effects": [], "gravity": 4, "has_audio": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "has_video": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_x": {"Points": [{"co": {"X": -0.04, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_y": {"Points": [{"co": {"X": 1, "Y": -0.21}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "mixing": 0, "origin_x": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "origin_y": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "parentObjectId": "", "perspective_c1_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c1_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "reader": {"acodec": "", "audio_bit_rate": 0, "audio_stream_index": -1, "audio_timebase": {"den": 1, "num": 1}, "channel_layout": 4, "channels": 0, "display_ratio": {"den": 9, "num": 16}, "duration": 3600, "file_size": "8294400", "fps": {"den": 1, "num": 30}, "has_audio": false, "has_single_image": true, "has_video": true, "height": 1080, "interlaced_frame": false, "metadata": {}, "path": "/home/ubuntu/api/video/files/39/title-d1ac4933.svg", "pixel_format": -1, "pixel_ratio": {"den": 1, "num": 1}, "sample_rate": 0, "top_field_first": true, "type": "QtImageReader", "vcodec": "QImage", "video_bit_rate": 0, "video_length": "108000", "video_stream_index": -1, "video_timebase": {"den": 30, "num": 1}, "width": 1920, "media_type": "image"}, "rotation": {"Points": []}, "scale": 1, "scale_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 181, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 271, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 361, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 451, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "scale_y": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 181, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 271, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 361, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 451, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_y": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "time": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "volume": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "wave_color": {"alpha": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "blue": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "green": {"Points": [{"co": {"X": 1, "Y": 123}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "red": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}}, "waveform": false, "title": "title-d1ac4933.svg"}'
    }
    r = post(CLOUD_URL + end_point, data=clip_data, auth=CLOUD_AUTH)
    # print(r.json())

    #Title Wed's
    end_point = '/projects/%s/title/' % project_id
    file_data = {
        "template": "Center-Text.svg",
        "text": "WED's",
        "font_size": 70.0,
        "font_name": "Bewilder Thick BRK",
        "fill_color": "#FF5349",
        "fill_opacity": 1.0,
        "stroke_color": "#000000",
        "stroke_size": 0.0,
        "stroke_opacity": 0.0,
        "drop_shadow": False,
        "background_color": "#000000",
        "background_opacity": 0.0
    }
    r = post(CLOUD_URL + end_point, data=file_data, files={"media": (source_name, open(source_path, "rb"))}, auth=CLOUD_AUTH)
    file_url = r.json().get("url")
    # print(r.json())

    # Title Clip (Wed's)
    end_point = '/projects/%s/clips/' % project_id
    clip_data = {
        "file": file_url,
        "position": 6.0,
        "start": 6.0,
        "end": 15.0,
        "layer": 4,
        "project": project_url,
        "json": '{"alpha": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 181, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 241, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 391, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 451, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "anchor": 0, "channel_filter": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "channel_mapping": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "display": 0, "duration": 0, "effects": [], "gravity": 4, "has_audio": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "has_video": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_y": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "mixing": 0, "origin_x": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "origin_y": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "parentObjectId": "", "perspective_c1_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c1_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "reader": {"acodec": "", "audio_bit_rate": 0, "audio_stream_index": -1, "audio_timebase": {"den": 1, "num": 1}, "channel_layout": 4, "channels": 0, "display_ratio": {"den": 9, "num": 16}, "duration": 3600, "file_size": "8294400", "fps": {"den": 1, "num": 30}, "has_audio": false, "has_single_image": true, "has_video": true, "height": 1080, "interlaced_frame": false, "metadata": {}, "path": "/home/ubuntu/api/video/files/39/title-9c73769d.svg", "pixel_format": -1, "pixel_ratio": {"den": 1, "num": 1}, "sample_rate": 0, "top_field_first": true, "type": "QtImageReader", "vcodec": "QImage", "video_bit_rate": 0, "video_length": "108000", "video_stream_index": -1, "video_timebase": {"den": 30, "num": 1}, "width": 1920, "media_type": "image"}, "rotation": {"Points": []}, "scale": 1, "scale_x": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "scale_y": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_y": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "time": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "volume": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "wave_color": {"alpha": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "blue": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "green": {"Points": [{"co": {"X": 1, "Y": 123}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "red": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}}, "waveform": false, "title": "title-9c73769d.svg"}'
    }
    r = post(CLOUD_URL + end_point, data=clip_data, auth=CLOUD_AUTH)
    # print(r.json())

    #Title Parth Kapoor
    end_point = '/projects/%s/title/' % project_id
    file_data = {
        "template": "Center-Text.svg",
        "text": groom_name,
        "font_size": 100.0,
        "font_name": "Bewilder Thick BRK",
        "fill_color": "#FF5349",
        "fill_opacity": 1.0,
        "stroke_color": "#000000",
        "stroke_size": 0.0,
        "stroke_opacity": 0.0,
        "drop_shadow": False,
        "background_color": "#000000",
        "background_opacity": 0.0
    }
    r = post(CLOUD_URL + end_point, data=file_data, files={"media": (source_name, open(source_path, "rb"))}, auth=CLOUD_AUTH)
    file_url = r.json().get("url")
    # print(r.json())

    # Title Clip (Parth Kapoor)
    end_point = '/projects/%s/clips/' % project_id
    clip_data = {
        "file": file_url,
        "position": 6.0,
        "start": 6.0,
        "end": 15.0,
        "layer": 5,
        "project": project_url,
        "json": '{"alpha": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "anchor": 0, "channel_filter": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "channel_mapping": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "display": 0, "duration": 0, "effects": [], "gravity": 4, "has_audio": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "has_video": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_x": {"Points": [{"co": {"X": 0.14, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_y": {"Points": [{"co": {"X": 1, "Y": 0.21}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "mixing": 0, "origin_x": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "origin_y": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "parentObjectId": "", "perspective_c1_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c1_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "reader": {"acodec": "", "audio_bit_rate": 0, "audio_stream_index": -1, "audio_timebase": {"den": 1, "num": 1}, "channel_layout": 4, "channels": 0, "display_ratio": {"den": 9, "num": 16}, "duration": 3600, "file_size": "8294400", "fps": {"den": 1, "num": 30}, "has_audio": false, "has_single_image": true, "has_video": true, "height": 1080, "interlaced_frame": false, "metadata": {}, "path": "/home/ubuntu/api/video/files/39/title-d1ac4933.svg", "pixel_format": -1, "pixel_ratio": {"den": 1, "num": 1}, "sample_rate": 0, "top_field_first": true, "type": "QtImageReader", "vcodec": "QImage", "video_bit_rate": 0, "video_length": "108000", "video_stream_index": -1, "video_timebase": {"den": 30, "num": 1}, "width": 1920, "media_type": "image"}, "rotation": {"Points": []}, "scale": 1, "scale_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 181, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 271, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 361, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 451, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "scale_y": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 181, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 271, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 361, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 451, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_y": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "time": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "volume": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "wave_color": {"alpha": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "blue": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "green": {"Points": [{"co": {"X": 1, "Y": 123}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "red": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}}, "waveform": false, "title": "title-d1ac4933.svg"}'
    }
    r = post(CLOUD_URL + end_point, data=clip_data, auth=CLOUD_AUTH)
    # print(r.json())

    #file (hole bg)
    end_point = '/projects/%s/files/' % project_id
    source_path = os.path.join(PATH, "assets/Video 07/hole_bg.png")
    source_name = os.path.split(source_path)[1]
    file_data = {
        "media": None,
        "project": project_url,
        "json": "{}"
    }
    r = post(CLOUD_URL + end_point, data=file_data, files={"media": (source_name, open(source_path, "rb"))}, auth=CLOUD_AUTH)
    file_url = r.json().get("url")
    # print(r.json())

    # file Clip (hole bg)
    end_point = '/projects/%s/clips/' % project_id
    clip_data = {
        "file": file_url,
        "position": 15.0,
        "start": 15.0,
        "end": 22.0,
        "layer": 2,
        "project": project_url,
        "json": '{}'
    }
    r = post(CLOUD_URL + end_point, data=clip_data, auth=CLOUD_AUTH)
    # print(r.json())

    #file (Both Image)
    end_point = '/projects/%s/files/' % project_id
    source_path = os.path.join(PATH, "assets/Video 07/Geetha Govindam.jpg")
    source_name = os.path.split(source_path)[1]
    file_data = {
        "media": None,
        "project": project_url,
        "json": "{}"
    }
    r = post(CLOUD_URL + end_point, data=file_data, files={"media": (source_name, open(source_path, "rb"))}, auth=CLOUD_AUTH)
    file_url = r.json().get("url")
    # print(r.json())

    # file Clip (Both Image)
    end_point = '/projects/%s/clips/' % project_id
    clip_data = {
        "file": file_url,
        "position": 15.0,
        "start": 15.0,
        "end": 22.0,
        "layer": 1,
        "project": project_url,
        "json": '{"alpha": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 451, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 511, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 601, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 661, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "anchor": 0, "channel_filter": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "channel_mapping": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "display": 0, "duration": 0, "effects": [], "gravity": 4, "has_audio": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "has_video": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_x": {"Points": [{"co": {"X": 0, "Y": 0.19}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_y": {"Points": [{"co": {"X": 0, "Y": -0.02}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "mixing": 0, "origin_x": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "origin_y": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "parentObjectId": "", "perspective_c1_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c1_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "reader": {"acodec": "", "audio_bit_rate": 0, "audio_stream_index": -1, "audio_timebase": {"den": 1, "num": 1}, "channel_layout": 4, "channels": 0, "display_ratio": {"den": 2, "num": 3}, "duration": 3600, "file_size": "960000", "fps": {"den": 1, "num": 30}, "has_audio": false, "has_single_image": true, "has_video": true, "height": 400, "interlaced_frame": false, "metadata": {}, "path": "/home/ubuntu/api/video/files/39/Geetha_Govindam.jpg", "pixel_format": -1, "pixel_ratio": {"den": 1, "num": 1}, "sample_rate": 0, "top_field_first": true, "type": "QtImageReader", "vcodec": "QImage", "video_bit_rate": 0, "video_length": "108000", "video_stream_index": -1, "video_timebase": {"den": 30, "num": 1}, "width": 600, "media_type": "image"}, "rotation": {"Points": []}, "scale": 1, "scale_x": {"Points": [{"co": {"X": 0, "Y": 0.33}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "scale_y": {"Points": [{"co": {"X": 0, "Y": 0.36}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_y": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "time": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "volume": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "wave_color": {"alpha": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "blue": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "green": {"Points": [{"co": {"X": 1, "Y": 123}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "red": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}}, "waveform": false, "title": "Geetha_Govindam.jpg"}'
    }
    r = post(CLOUD_URL + end_point, data=clip_data, auth=CLOUD_AUTH)
    # print(r.json())

    #file (image2)
    end_point = '/projects/%s/files/' % project_id
    source_path = os.path.join(PATH, "assets/Video 07/bg.jpg")
    source_name = os.path.split(source_path)[1]
    file_data = {
        "media": None,
        "project": project_url,
        "json": "{}"
    }
    r = post(CLOUD_URL + end_point, data=file_data, files={"media": (source_name, open(source_path, "rb"))}, auth=CLOUD_AUTH)
    file_url = r.json().get("url")
    # print(r.json())

    # file Clip (image2)
    end_point = '/projects/%s/clips/' % project_id
    clip_data = {
        "file": file_url,
        "position": 22.0,
        "start": 22.0,
        "end": 30.0,
        "layer": 1,
        "project": project_url,
        "json": "{}"
    }
    r = post(CLOUD_URL + end_point, data=clip_data, auth=CLOUD_AUTH)
    # print(r.json())

    #Title Venue
    end_point = '/projects/%s/title/' % project_id
    file_data = {
        "template": "Center-Text.svg",
        "text": "Venue",
        "font_size": 80.0,
        "font_name": "Bewilder Thick BRK",
        "fill_color": "#FF5349",
        "fill_opacity": 1.0,
        "stroke_color": "#000000",
        "stroke_size": 0.0,
        "stroke_opacity": 0.0,
        "drop_shadow": False,
        "background_color": "#000000",
        "background_opacity": 0.0
    }
    r = post(CLOUD_URL + end_point, data=file_data, files={"media": (source_name, open(source_path, "rb"))}, auth=CLOUD_AUTH)
    file_url = r.json().get("url")
    # print(r.json())

    # Title Clip (venue)
    end_point = '/projects/%s/clips/' % project_id
    clip_data = {
        "file": file_url,
        "position": 22.0,
        "start": 22.0,
        "end": 30.0,
        "layer": 2,
        "project": project_url,
        "json": '{"alpha": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 661, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 721, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 841, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 901, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "anchor": 0, "channel_filter": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "channel_mapping": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "display": 0, "duration": 0, "effects": [], "gravity": 4, "has_audio": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "has_video": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_y": {"Points": [{"co": {"X": 1, "Y": -0.29}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "mixing": 0, "origin_x": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "origin_y": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "parentObjectId": "", "perspective_c1_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c1_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "reader": {"acodec": "", "audio_bit_rate": 0, "audio_stream_index": -1, "audio_timebase": {"den": 1, "num": 1}, "channel_layout": 4, "channels": 0, "display_ratio": {"den": 9, "num": 16}, "duration": 3600, "file_size": "8294400", "fps": {"den": 1, "num": 30}, "has_audio": false, "has_single_image": true, "has_video": true, "height": 1080, "interlaced_frame": false, "metadata": {}, "path": "/home/ubuntu/api/video/files/39/title-9c73769d.svg", "pixel_format": -1, "pixel_ratio": {"den": 1, "num": 1}, "sample_rate": 0, "top_field_first": true, "type": "QtImageReader", "vcodec": "QImage", "video_bit_rate": 0, "video_length": "108000", "video_stream_index": -1, "video_timebase": {"den": 30, "num": 1}, "width": 1920, "media_type": "image"}, "rotation": {"Points": []}, "scale": 1, "scale_x": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "scale_y": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_y": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "time": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "volume": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "wave_color": {"alpha": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "blue": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "green": {"Points": [{"co": {"X": 1, "Y": 123}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "red": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}}, "waveform": false, "title": "title-9c73769d.svg"}'
    }
    r = post(CLOUD_URL + end_point, data=clip_data, auth=CLOUD_AUTH)
    # print(r.json())

    #Title Leaf Resort
    end_point = '/projects/%s/title/' % project_id
    file_data = {
        "template": "Center-Text.svg",
        "text": venue,
        "font_size": 100.0,
        "font_name": "Bewilder Thick BRK",
        "fill_color": "#FF5349",
        "fill_opacity": 1.0,
        "stroke_color": "#000000",
        "stroke_size": 0.0,
        "stroke_opacity": 0.0,
        "drop_shadow": False,
        "background_color": "#000000",
        "background_opacity": 0.0
    }
    r = post(CLOUD_URL + end_point, data=file_data, files={"media": (source_name, open(source_path, "rb"))}, auth=CLOUD_AUTH)
    file_url = r.json().get("url")
    # print(r.json())

    # Title Clip (Leaf Resort)
    end_point = '/projects/%s/clips/' % project_id
    clip_data = {
        "file": file_url,
        "position": 24.0,
        "start": 24.0,
        "end": 30.0,
        "layer": 3,
        "project": project_url,
        "json": '{"alpha": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "anchor": 0, "channel_filter": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "channel_mapping": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "display": 0, "duration": 0, "effects": [], "gravity": 4, "has_audio": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "has_video": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_y": {"Points": [{"co": {"X": 1, "Y": -0.12}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "mixing": 0, "origin_x": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "origin_y": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "parentObjectId": "", "perspective_c1_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c1_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "reader": {"acodec": "", "audio_bit_rate": 0, "audio_stream_index": -1, "audio_timebase": {"den": 1, "num": 1}, "channel_layout": 4, "channels": 0, "display_ratio": {"den": 9, "num": 16}, "duration": 3600, "file_size": "8294400", "fps": {"den": 1, "num": 30}, "has_audio": false, "has_single_image": true, "has_video": true, "height": 1080, "interlaced_frame": false, "metadata": {}, "path": "/home/ubuntu/api/video/files/39/title-d1ac4933.svg", "pixel_format": -1, "pixel_ratio": {"den": 1, "num": 1}, "sample_rate": 0, "top_field_first": true, "type": "QtImageReader", "vcodec": "QImage", "video_bit_rate": 0, "video_length": "108000", "video_stream_index": -1, "video_timebase": {"den": 30, "num": 1}, "width": 1920, "media_type": "image"}, "rotation": {"Points": []}, "scale": 1, "scale_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 721, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 781, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 841, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 901, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "scale_y": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 721, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 781, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 841, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 901, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_y": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "time": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "volume": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "wave_color": {"alpha": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "blue": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "green": {"Points": [{"co": {"X": 1, "Y": 123}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "red": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}}, "waveform": false, "title": "title-d1ac4933.svg"}'
    }
    r = post(CLOUD_URL + end_point, data=clip_data, auth=CLOUD_AUTH)
    # print(r.json())

    #Title Save The Date
    end_point = '/projects/%s/title/' % project_id
    file_data = {
        "template": "Center-Text.svg",
        "text": "Save The Date",
        "font_size": 80.0,
        "font_name": "Bewilder Thick BRK",
        "fill_color": "#FF5349",
        "fill_opacity": 1.0,
        "stroke_color": "#000000",
        "stroke_size": 0.0,
        "stroke_opacity": 0.0,
        "drop_shadow": False,
        "background_color": "#000000",
        "background_opacity": 0.0
    }
    r = post(CLOUD_URL + end_point, data=file_data, files={"media": (source_name, open(source_path, "rb"))}, auth=CLOUD_AUTH)
    file_url = r.json().get("url")
    # print(r.json())

    # Title Clip (Save The Date)
    end_point = '/projects/%s/clips/' % project_id
    clip_data = {
        "file": file_url,
        "position": 22.0,
        "start": 22.0,
        "end": 30.0,
        "layer": 4,
        "project": project_url,
        "json": '{"alpha": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 661, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 721, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 841, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 901, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "anchor": 0, "channel_filter": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "channel_mapping": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "display": 0, "duration": 0, "effects": [], "gravity": 4, "has_audio": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "has_video": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_y": {"Points": [{"co": {"X": 1, "Y": 0.12}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "mixing": 0, "origin_x": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "origin_y": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "parentObjectId": "", "perspective_c1_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c1_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "reader": {"acodec": "", "audio_bit_rate": 0, "audio_stream_index": -1, "audio_timebase": {"den": 1, "num": 1}, "channel_layout": 4, "channels": 0, "display_ratio": {"den": 9, "num": 16}, "duration": 3600, "file_size": "8294400", "fps": {"den": 1, "num": 30}, "has_audio": false, "has_single_image": true, "has_video": true, "height": 1080, "interlaced_frame": false, "metadata": {}, "path": "/home/ubuntu/api/video/files/39/title-9c73769d.svg", "pixel_format": -1, "pixel_ratio": {"den": 1, "num": 1}, "sample_rate": 0, "top_field_first": true, "type": "QtImageReader", "vcodec": "QImage", "video_bit_rate": 0, "video_length": "108000", "video_stream_index": -1, "video_timebase": {"den": 30, "num": 1}, "width": 1920, "media_type": "image"}, "rotation": {"Points": []}, "scale": 1, "scale_x": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "scale_y": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_y": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "time": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "volume": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "wave_color": {"alpha": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "blue": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "green": {"Points": [{"co": {"X": 1, "Y": 123}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "red": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}}, "waveform": false, "title": "title-9c73769d.svg"}'
    }
    r = post(CLOUD_URL + end_point, data=clip_data, auth=CLOUD_AUTH)
    # print(r.json())

    #Title 30th July 2022
    end_point = '/projects/%s/title/' % project_id
    file_data = {
        "template": "Center-Text.svg",
        "text": wedding_date,
        "font_size": 100.0,
        "font_name": "Bewilder Thick BRK",
        "fill_color": "#FF5349",
        "fill_opacity": 1.0,
        "stroke_color": "#000000",
        "stroke_size": 0.0,
        "stroke_opacity": 0.0,
        "drop_shadow": False,
        "background_color": "#000000",
        "background_opacity": 0.0
    }
    r = post(CLOUD_URL + end_point, data=file_data, files={"media": (source_name, open(source_path, "rb"))}, auth=CLOUD_AUTH)
    file_url = r.json().get("url")
    # print(r.json())

    # Title Clip (30th July 2022)
    end_point = '/projects/%s/clips/' % project_id
    clip_data = {
        "file": file_url,
        "position": 24.0,
        "start": 24.0,
        "end": 30.0,
        "layer": 5,
        "project": project_url,
        "json": '{"alpha": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "anchor": 0, "channel_filter": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "channel_mapping": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "display": 0, "duration": 0, "effects": [], "gravity": 4, "has_audio": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "has_video": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "location_y": {"Points": [{"co": {"X": 1, "Y": 0.29}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "mixing": 0, "origin_x": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "origin_y": {"Points": [{"co": {"X": 1, "Y": 0.5}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "parentObjectId": "", "perspective_c1_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c1_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c2_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c3_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_x": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "perspective_c4_y": {"Points": [{"co": {"X": 1, "Y": -1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "reader": {"acodec": "", "audio_bit_rate": 0, "audio_stream_index": -1, "audio_timebase": {"den": 1, "num": 1}, "channel_layout": 4, "channels": 0, "display_ratio": {"den": 9, "num": 16}, "duration": 3600, "file_size": "8294400", "fps": {"den": 1, "num": 30}, "has_audio": false, "has_single_image": true, "has_video": true, "height": 1080, "interlaced_frame": false, "metadata": {}, "path": "/home/ubuntu/api/video/files/39/title-d1ac4933.svg", "pixel_format": -1, "pixel_ratio": {"den": 1, "num": 1}, "sample_rate": 0, "top_field_first": true, "type": "QtImageReader", "vcodec": "QImage", "video_bit_rate": 0, "video_length": "108000", "video_stream_index": -1, "video_timebase": {"den": 30, "num": 1}, "width": 1920, "media_type": "image"}, "rotation": {"Points": []}, "scale": 1, "scale_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 721, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 781, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 841, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 901, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "scale_y": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 721, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 781, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 841, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}, {"co": {"X": 901, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_x": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "shear_y": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "time": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "volume": {"Points": [{"co": {"X": 1, "Y": 1}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "wave_color": {"alpha": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "blue": {"Points": [{"co": {"X": 1, "Y": 255}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "green": {"Points": [{"co": {"X": 1, "Y": 123}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}, "red": {"Points": [{"co": {"X": 1, "Y": 0}, "handle_left": {"X": 0.5, "Y": 1}, "handle_right": {"X": 0.5, "Y": 0}, "handle_type": 0, "interpolation": 0}]}}, "waveform": false, "title": "title-d1ac4933.svg"}'
    }
    r = post(CLOUD_URL + end_point, data=clip_data, auth=CLOUD_AUTH)
    # print(r.json())


    ################################################################################################################
    # Create export for final rendered video
    end_point = '/projects/%s/exports/' % project_id
    export_data = {
        "video_format": "mp4",
        "video_codec": "libx264",
        "video_bitrate": 8000000,
        "audio_codec": "ac3",
        "audio_bitrate": 1920000,
        "start_frame": 1,
        "end_frame": None,
        "project": project_url,
        "json": "{}"
    }
    r = post(CLOUD_URL + end_point, data=export_data, auth=CLOUD_AUTH)
    export_url = r.json().get("url")
    # print(r.json())


    # Wait for Export to finish (give up after around 40 minutes)
    export_output_url = None
    is_exported = False
    countdown = 500
    while not is_exported and countdown > 1:
        r = get(export_url, auth=CLOUD_AUTH)
        print(r.json())
        is_exported = float(r.json().get("progress", 0.0)) == 100.0
        countdown -= 1
        time.sleep(2.0)

    # Get final rendered url
    r = get(export_url, auth=CLOUD_AUTH)
    export_output_url = r.json().get("output")
    # print(r.json())
    print("Export Successfully Completed: %s" % export_output_url)
    return export_output_url