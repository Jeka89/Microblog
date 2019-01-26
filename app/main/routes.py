from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app
from flask_login import current_user, login_required
from app import db
from app.main.forms import PostForm
from app.models import Post
from app.main import bp
from datetime import datetime
from flask_babel import get_locale
from guess_language import guess_language
from app.translate import translate

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
  page = request.args.get('page', 1, type=int)
  form = PostForm()
  if form.validate_on_submit():
    language = guess_language(form.post.data)
    if language == 'UNKNOWN' or len(language) > 5:
      language = ''
    post = Post(body=form.post.data, author=current_user, language=language)
    db.session.add(post)
    db.session.commit()
    flash('Your post is now live!')
    return redirect(url_for('main.index'))

  posts = current_user.followed_posts().paginate(
    page, current_app.config['POSTS_PER_PAGE'], False)
  next_url = url_for('main.index', page=posts.next_num) \
    if posts.has_next else None
  prev_url = url_for('main.index', page=posts.prev_num) \
    if posts.has_prev else None
  return render_template("index.html", title='Home Page', form=form, posts=posts.items,
    next_url=next_url, prev_url=prev_url)

@bp.route('/explore')
@login_required
def explore():
  page = request.args.get('page', 1, type=int)
  posts = Post.query.order_by(Post.timestamp.desc()).paginate(
    page, current_app.config['POSTS_PER_PAGE'], False)
  next_url = url_for('main.explore', page=posts.next_num) \
    if posts.has_next else None
  prev_url = url_for('main.explore', page=posts.prev_num) \
    if posts.has_prev else None
  return render_template('index.html', title='Explore', posts=posts.items,
    next_url=next_url, prev_url=prev_url)

@bp.before_request
def before_request():
  if current_user.is_authenticated:
    current_user.last_seen = datetime.utcnow()
    db.session.commit()
  g.locale = str(get_locale())

@bp.route('/translate', methods=['POST'])
@login_required
def translate_text():
  return jsonify({'text': translate(request.form['text'], request.form['source_language'],request.form['dest_language'])})