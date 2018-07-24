from flask import Blueprint, redirect, render_template
from flask import request, url_for
from flask_user import current_user, login_required, roles_required

from app import db
from app.models.user import UserProfileForm

main = Blueprint('main', __name__,
                        template_folder='templates',
                        static_folder='static',
                        static_url_path = '/main/static')

# The Home page is accessible to anyone
@main.route('/')
def home_page():
    return render_template('home.html')


# The User page is accessible to authenticated users (users that have logged in)
@main.route('/member')
@login_required  # Limits access to authenticated users
def member_page():
    return render_template('main.html')


# The Admin page is accessible to users with the 'admin' role
@main.route('/admin')
@roles_required('admin')  # Limits access to users with the 'admin' role
def admin_page():
    return render_template('admin_page.html')


@main.route('/profile', methods=['GET', 'POST'])
@login_required
def user_profile_page():
    # Initialize form
    form = UserProfileForm(request.form, obj=current_user)

    # Process valid POST
    if request.method == 'POST' and form.validate():
        # Copy form fields to user_profile fields
        form.populate_obj(current_user)

        # Save user_profile
        db.session.commit()

        # Redirect to home page
        return redirect(url_for('main.home_page'))

    # Process GET or invalid POST
    return render_template('main/user_profile_page.html',
                           form=form)
                           