from flask import render_template
from rlib import Reddit
from embeddit import app
import HTMLParser


h = HTMLParser.HTMLParser()
reddit = Reddit()


@app.route('/r/<subreddit>/comments/<link_id>/<slug>/<comment_id>/', defaults={'domain': 'reddit.com'})
@app.route('/<domain>/r/<subreddit>/comments/<link_id>/<slug>/<comment_id>/')
@app.route('/<regex("\w+"):subreddit>.<domain>/comments/<link_id>/<slug>/<comment_id>/')
def view_comment(domain, subreddit, link_id, slug, comment_id):
    link, comment = reddit.get_comment(subreddit, link_id, comment_id, include_link=True)

    return render_template('comment.html', link=link, comment=comment)


@app.route('/r/<subreddit>/comments/<link_id>/', defaults={'domain': 'reddit.com', 'slug': None})
@app.route('/r/<subreddit>/comments/<link_id>/<slug>/', defaults={'domain': 'reddit.com'})
@app.route('/<domain>/r/<subreddit>/comments/<link_id>/', defaults={'slug': None})
@app.route('/<domain>/r/<subreddit>/comments/<link_id>/<slug>/')
@app.route('/<regex("\w+"):subreddit>.<domain>/comments/<link_id>/', defaults={'domain': 'reddit.com', 'slug': None})
@app.route('/<regex("\w+"):subreddit>.<domain>/comments/<link_id>/<slug>/', defaults={'domain': 'reddit.com'})
def view_link(domain, subreddit, link_id, slug):
    link = reddit.get_link(subreddit, link_id)

    return render_template('link.html', link=link)


@app.route('/r/<subreddit>/', defaults={'domain': 'reddit.com'})
@app.route('/<domain>/r/<subreddit>/')
@app.route('/<regex("\w+"):subreddit>.<domain>/', defaults={'domain': 'reddit.com'})
def view_subreddit(domain, subreddit):
    return '/r/%s' % subreddit
