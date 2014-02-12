from embeddit import app
from flask import render_template
from rlib import Reddit
import HTMLParser


h = HTMLParser.HTMLParser()
r = Reddit()


@app.route('/favicon.ico')
def static_pass():
    return ''


@app.route('/r/<subreddit>/comments/<link_id>/<slug>/<comment_id>', defaults={'domain': 'reddit.com'})
@app.route('/<domain>/r/<subreddit>/comments/<link_id>/<slug>/<comment_id>')
@app.route('/<regex("\w+"):subreddit>.<domain>/comments/<link_id>/<slug>/<comment_id>')
def view_comment(domain, subreddit, link_id, slug, comment_id):
    comment, link = r.subreddit(subreddit, domain).comments(link_id, comment_id, include_link=True, limit=30)

    return render_template('comment.html', link=link, comment=comment)


@app.route('/r/<subreddit>/comments/<link_id>', defaults={'domain': 'reddit.com', 'slug': None})
@app.route('/r/<subreddit>/comments/<link_id>/<slug>', defaults={'domain': 'reddit.com'})
@app.route('/<domain>/r/<subreddit>/comments/<link_id>', defaults={'slug': None})
@app.route('/<domain>/r/<subreddit>/comments/<link_id>/<slug>')
@app.route('/<regex("\w+"):subreddit>.<domain>/comments/<link_id>', defaults={'domain': 'reddit.com', 'slug': None})
@app.route('/<regex("\w+"):subreddit>.<domain>/comments/<link_id>/<slug>', defaults={'domain': 'reddit.com'})
def view_link(domain, subreddit, link_id, slug):
    link = r.subreddit(subreddit, domain).link(link_id)

    return render_template('link.html', link=link)


@app.route('/r/<subreddit>', defaults={'domain': 'reddit.com'})
@app.route('/<domain>/r/<subreddit>')
@app.route('/<regex("\w+"):subreddit>.<domain>', defaults={'domain': 'reddit.com'})
def view_subreddit(domain, subreddit):
    return render_template(
        'subreddit.html',
        domain=domain,

        subreddit=r.subreddit(subreddit, domain).about()
    )
