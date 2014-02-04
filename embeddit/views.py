from flask import render_template
from rlib import Reddit
from embeddit import app
import HTMLParser


h = HTMLParser.HTMLParser()
reddit = Reddit()


def build_url(domain, fragments):
    return 'http://%s/%s' % (domain, '/'.join([x for x in fragments if x]) + '.json')


@app.route('/r/<subreddit>/comments/<link_id>/<slug>/<comment_id>/', defaults={'domain': 'reddit.com'})
@app.route('/<domain>/r/<subreddit>/comments/<link_id>/<slug>/<comment_id>/')
@app.route('/<regex("\w+"):subreddit>.<domain>/comments/<link_id>/<slug>/<comment_id>/')
def view_comment(domain, subreddit, link_id, slug, comment_id):
    url = build_url(domain, [
        'r', subreddit, 'comments',
        link_id,
        slug,
        comment_id
    ])

    app.logger.info('Requesting "%s"' % url)
    link, comment = reddit.get_comment(url=url, include_link=True)

    return render_template('comment.html', link=link, comment=comment)


@app.route('/r/<subreddit>/comments/<link_id>/', defaults={'domain': 'reddit.com', 'slug': None})
@app.route('/r/<subreddit>/comments/<link_id>/<slug>/', defaults={'domain': 'reddit.com'})
@app.route('/<domain>/r/<subreddit>/comments/<link_id>/', defaults={'slug': None})
@app.route('/<domain>/r/<subreddit>/comments/<link_id>/<slug>/')
@app.route('/<regex("\w+"):subreddit>.<domain>/comments/<link_id>/', defaults={'domain': 'reddit.com', 'slug': None})
@app.route('/<regex("\w+"):subreddit>.<domain>/comments/<link_id>/<slug>/', defaults={'domain': 'reddit.com'})
def view_link(domain, subreddit, link_id, slug):
    url = build_url(domain, [
        'r', subreddit, 'comments',
        link_id,
        slug
    ])

    app.logger.info('Requesting "%s"' % url)
    link = reddit.get_link(url=url)

    return render_template('link.html', link=link)


@app.route('/r/<subreddit>/', defaults={'domain': 'reddit.com'})
@app.route('/<domain>/r/<subreddit>/')
@app.route('/<regex("\w+"):subreddit>.<domain>/', defaults={'domain': 'reddit.com'})
def view_subreddit(domain, subreddit):
    return '/r/%s' % subreddit
