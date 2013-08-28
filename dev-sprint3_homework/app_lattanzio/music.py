import flask, flask.views
import os
import utils


class Music (flask.views.MethodView):
	@login_required
	def get(self):
		songs = os.listdir('static/music/')
		return flask.render_template('music.html', "music.html", songs=songs)

		
		
