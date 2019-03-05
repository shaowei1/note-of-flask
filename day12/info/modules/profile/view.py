from flask import render_template, g, request

from . import profile_blu

from info.utils.common import login_required


@profile_blu.route('/base_info', methods=['GET', 'POST'])
@login_required
def base_info():
    user = g.user
    if request.method == 'GET':
        data = {
            'user': user.to_dict(),
        }
        return render_template('news/user_base_info.html', data=data)
