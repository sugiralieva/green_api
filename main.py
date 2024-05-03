from flask import Flask, request
from flask import render_template, flash
from methods import get_settings, get_state_instance, send_message, send_file_by_url



SECRET_KEY = 'fdgdfgdfggf786hfg6hfg6h7f'
MAX_CONTENT_LENGTH = 1024 * 1024

app = Flask(__name__)

app.config['DEBUG'] = True
app.config.from_object(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    idinstance = ''
    apitokeninstance = ''
    response = ''
    if request.method == 'POST':
        apiurl = 'https://7103.api.greenapi.com'
        idinstance = request.form['idinstance']
        apitokeninstance = request.form['apitokeninstance']
        if idinstance and apitokeninstance:
            if 'getsettings' in request.form:
                response = get_settings(apiurl, idinstance, apitokeninstance)
            elif 'getstateinstance' in request.form:
                response = get_state_instance(apiurl, idinstance, apitokeninstance)
            elif 'sendmessage' in request.form:
                number = request.form['phonenumber']
                message_text = request.form['text']
                response = send_message(apiurl, idinstance, apitokeninstance, number, message_text)
            elif 'sendfilebyurl' in request.form:
                number = request.form['phonenumber2']
                file_url = request.form['fileurl']
                response = send_file_by_url(apiurl, idinstance, apitokeninstance, number, file_url)
        else:
            flash('Заполните поля idinstance и ApiTokenInstance')

    return render_template('index.html', response=response, idinstance=idinstance, apitokeninstance=apitokeninstance)


if __name__ == '__main__':
    app.run()
