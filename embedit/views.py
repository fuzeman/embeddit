import HTMLParser
from flask import render_template
from rlib import Reddit
from embedit import app


h = HTMLParser.HTMLParser()
reddit = Reddit()


@app.route('/r/<subreddit>/comments/<link_id>/<slug>/<comment_id>')
def view_comment(subreddit, link_id, slug, comment_id):
    link, comment = reddit.get_comment(subreddit, link_id, comment_id, include_link=True)

    return render_template('comment.html', link=link, comment=comment)


@app.route('/r/<subreddit>/comments/<link_id>', defaults={'slug': None})
@app.route('/r/<subreddit>/comments/<link_id>/<slug>')
def view_link(subreddit, link_id, slug):
    link = reddit.get_link(subreddit, link_id)

    return render_template('link.html', link=link)


@app.route('/r/<subreddit>')
def view_subreddit(subreddit):
    return '/r/%s' % subreddit
