from authlib.integrations.flask_client import OAuth

from urllib.parse import quote_plus, urlencode
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, request, Response, url_for, send_file, jsonify

import base64
import datetime
public_entry={'_id':'5',
'last_update': 1688212610,
    'title':'Entry',
    'chats':[{},{},
    {'role':'user', 'content': 'Hi'},
    {'role':'assistant', 'content': 'Hi, what is up?'},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    {'role':'user', 'content': 'not much. Hey, have you ever wondered what it would be like to live on a tropical island?'},
    {'role':'assistant', 'content': "Absolutely! The thought of waking up to the sound of waves and feeling the warm sand beneath my feet sounds like paradise. I'd love to escape the daily hustle and bustle"},
    ]}

app = Flask(__name__)

@app.template_filter('b64encode')
def b64encode_filter(s):
    return base64.b64encode(s).decode('utf-8')


# home page of the authenticated user
@app.route("/")
def home():
    in_progress_entries=[{'_id':'1', 'title': 'My first entry', 'last_update': 1688212610},{'_id':'2', 'title': 'My second entry', 'last_update': 1688012610}]
    completed_entries = [{'_id':'3', 'title': 'My third entry', 'last_update': 1688312610},{'_id':'4', 'title': 'My fourth entry',  'last_update': 1688112610}]

    return render_template('home.html', in_progress_entries=in_progress_entries, completed_entries=completed_entries)

# landing page of an un-authenticated user
@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route("/shared")
def public_entries():
    entries = [{'_id':'3', 'title': 'My third entry', 'last_update': 1688012610, 'excerpt':'This is the begining of the entry'},
    {'_id':'4', 'title': 'My fourth entry', 'last_update': 1688112610, 'excerpt':'This is the begining of the fourth entry'}]
    return render_template('shared.html', entries=entries)
  

@app.route('/terms')
def terms():
    return render_template('terms.html')



@app.route("/register_terms")
def register_terms():
    try:
        return redirect("/")
    except:
        return 'please try again'


@app.route('/chat/', defaults={'entry_id': 'new'}, methods=['GET'])
@app.route("/chat/<entry_id>")
def chat(entry_id):
    entry={'_id':'5',
    'title':'Entry',
    'chats':[{},{}]}

    return render_template('chat.html', entry=entry)


@app.route('/get_response', methods=['POST'])
def get_response():
    return "The response goes here"


@ app.route("/past_entries/<entry_id>")
def past_entries(entry_id):
    entry=public_entry
    return render_template('journal-entry.html', entry=entry)

@ app.route("/admin/<entry_id>")
def admin(entry_id):
    entries = [{'_id':'3', 'title': 'My third entry', 'last_update': 1688012610, 'excerpt':'This is the begining of the entry'},
    {'_id':'4', 'title': 'My fourth entry', 'last_update': 1688112610, 'excerpt':'This is the begining of the fourth entry'}]  
    return render_template('admin-entries.html', entries=entries)


@ app.route("/privacy")
def privacy():
    return render_template('privacy.html')

@app.route('/logo')
def get_log0():
    return send_file('./static/gagalilogo.jpg', mimetype='image/jpg')


@app.route('/static/<folder>/<filename>')
def get_static_file(folder, filename):
    return send_file('./static/'+folder+'/'+filename)


@app.route('/analyze/<analysis_type>/<entry_id>')
def analyze(entry_id, analysis_type):
    """
    return a json like {'text':'......'}
    """
    return 'The analysis results goes here'


@app.route('/entry-done/<entry_id>')
def entry_done(entry_id):
    return {'success':True}

@app.route('/email_content',  methods=['POST'])
def email_content():
    return {'success':True}


@app.route('/entry-title', methods=['POST'])
def update_entry_title():

    return {'success':True}


@app.route('/delete-entry/<entry_id>', methods=['DELETE'])
def delte_entry(entry_id):
    return {'success':True}



@app.route('/change-to-in-progress', methods=['POST'])
def change_to_in_progress():

    return {'success':True}



@ app.route("/update-privacy", methods=['POST'])
def update_privacy():
    return 'success'

@app.route('/feedback', methods=['GET','POST'])
def submit_feedback():
    if request.method=='GET':
        return render_template('feedback.html')
    else:
        feedback = request.form.get('feedback')
        return redirect("/")

@app.route('/how-it-works')
def how_it_works():
    return render_template('how-it-works.html')

@app.template_filter('timestamp_to_local_time')
def timestamp_to_local_time(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/chat-feedback', methods=['POST'])
def chat_feedback():
    return {'success':True}


@app.route('/like_comment/<comment_id>')
def like_comment(comment_id):
    return redirect('/shared')

@app.route('/add_comment', methods=['POST'])
def add_comment():
  
    return redirect(f'/shared')

@app.route('/public-entry/<entry_id>')
def get_public_entry(entry_id):
    entry=public_entry
    comments = [{'entry_id':'1', 'content': 'comment is here', 'last_update':1688685053},
    {'entry_id':'2', 'content': 'comment is there', 'last_update':1688686053}]
    return render_template('public-entry.html', entry=entry, comments=comments)


@app.route('/profile')
def profile():
    profile={'first_name':'John', 'last_name':'Smith', 'therapist_email':'therapist@gmail.com'}

    return render_template('profile.html', profile=profile)


@app.route('/update-profile', methods=['POST'])
def update_profile():

    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
