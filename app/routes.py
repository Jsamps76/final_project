from flask import current_app as app, Flask, request, url_for, render_template, flash, redirect
from app import db
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/')
def index():
    return render_template('index2.html')



@app.route('/posts/update/<int:post_id>', methods=['GET', 'POST'])
@login_required
def post_update(post_id):
    update_form = BlogPostForm()
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST' and update_form.validate():
        title = update_form.title.data
        content = update_form.content.data
        user_id = current_user.id

        post.title = title
        post.content = content
        post.user_id = user_id

        db.session.commit()
        return redirect(url_for('blog.post_update', post_id=post.id))

    return render_template('post_update.html', form=update_form, post=post)





