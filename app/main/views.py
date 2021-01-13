from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    old_name = session.get('name')
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            # 修改用户名后自动发邮件提醒
            # if app.config['FLASKY_ADMIN']:
            #     send_email(app.config['FLASKY_ADMIN'], 'New_User', 'mail/new_user', user=user)
            if old_name is not None and old_name != form.name.data:
                flash('修改名字成功！')
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False), current_time=datetime.utcnow())


@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

