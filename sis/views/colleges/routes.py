from flask import request, render_template, redirect, flash,session
from flask.helpers import url_for
from sis.models.student import Student
from sis.models.course import Course
from sis.models.college import College
from .utils import add_college_to_db, update_college_record,save_image,delete_image,check_page_limit,check_limit_validity
from . import college
from math import ceil

current_page = 1
college_limit = 5

@college.route('/colleges', methods=['GET', 'POST'])
def colleges() -> str:
    global college_limit
    students = Student().get_all(paginate=False)
    courses = Course().get_all(paginate=False)
    colleges = College().get_all(current_page,college_limit)
    departments = College().get_departments()

    min_page = request.args.get('min_page')
    max_page = request.args.get('max_page')
    page_limit = check_page_limit(min_page, max_page)
    colleges_count = str(College().get_total())
    print(colleges[0])
    if 5 == colleges_count:
        page_limit = 'min-and-max'
    try:
        college_limit = check_limit_validity(5, int(colleges_count))
    except:
        college_limit = college_limit
    return render_template('/college/colleges.html', 
                            data=[students,courses,colleges,departments], 
                            datacount= colleges_count,
                            college_limit = college_limit,
                            limit = page_limit
                           )


@college.route('/colleges/next', methods=['GET', 'POST'])
def next() -> str:
    global current_page
    college_count = College().get_total()
    current_page += 1
    limit_page = ceil(college_count/5)
    max_page_reached = current_page > limit_page

    if not max_page_reached:
        return redirect(url_for('college.colleges', page_num=current_page))
    else:
        current_page -= 1
        return redirect(url_for('college.colleges', page_num=current_page, limit=True))



@college.route('/colleges/prev', methods=['GET', 'POST'])
def prev() -> str:
    global current_page
    college_count = College().get_total()
    current_page -= 1
    max_page_reached = current_page <1

    if not max_page_reached:
        return redirect(url_for('college.colleges', page_num=current_page))
    else:
        current_page = 1
        return redirect(url_for('college.colleges', page_num=current_page, limit=True))



@college.route('/colleges/add', methods=['GET', 'POST'])
def add() -> str:        
    if request.method == 'POST':
        image = request.files['selected-image-1']
        try:
            cloud_link = save_image(image)
        except Exception as e:
            print("Can't save image")
            print(e)
        college = {
            'code': request.form.get('college-code'),
            'name': request.form.get('college-name'),
            'logo': cloud_link
        }
        added= add_college_to_db(college)
        if added:
            flash(f'{college["code"]} is added succesfully!', 'success')
        else:
            flash(f'{college["code"]} cannot be added. Make sure the ID is unique.', 'info')
        
        return redirect(url_for('college.colleges'))
    else:
        return render_template('/college/form.html')





@college.route('/colleges/search', methods=['GET', 'POST'])
def search() -> str:
    user_input = request.form.get('user-input')
    field = request.form.get('field')

    if field == 'select':
        result = College().search(keyword=user_input)
    elif field == 'code':
        result = College().search(keyword=user_input, field='code')
    elif field == 'name':
        result = College().search(keyword=user_input, field='name')
    elif field == 'coursecount':
        result = College().search(keyword=user_input, field='coursecount')
    elif field == 'studentcount':
        result = College().search(keyword=user_input, field='studentcount')
    else:
        result = []

    if len(result) != 0:
        return render_template('/college/colleges.html', 
                                data=['', '', result], 
                                datacount= str(len(result)))
    else:
        flash(f'No college found', 'info')
        return render_template('/college/colleges.html', 
                                data=['', '', result], 
                                datacount= str(len(result)))


@college.route('/colleges/delete/<string:id>')
def delete(id: str) -> str:
    try:
        College().delete(id)
        flash(f'{id} deleted from the database.', 'info')
        return redirect(url_for('college.colleges'))
    except:
        flash(f'{id} cannot be deleted. Students or courses are registered under the selected college.', 'info')
        return redirect(url_for('college.colleges'))


@college.route('/colleges/update/<string:id>', methods=['GET', 'POST'])
def update(id: str) -> str:
    if request.method == 'POST':
        image = request.files['selected-image-1'+id]
        cloud_link = ''
        try:
            cloud_link = save_image(image)
        except Exception as e:
            print("Can't save image")
            print(e)

        if cloud_link:
            college = {
            'code': id,
            'name': request.form.get('college-name'),
            'logo' : cloud_link
            }
            update_college_record(college)        
        else:
            college = {
            'code': id,
            'name': request.form.get('college-name'),
            'logo' : cloud_link
            }
            update_college_record(college)
        flash(f"{college['code']} has been updated succesfully!", 'info')
        return redirect(url_for('college.colleges'))
    else:
        return redirect(url_for('college.colleges'))