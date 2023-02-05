from sis.models.college import College
from werkzeug.utils import secure_filename
import cloudinary.uploader as cloud
import os
from os import getenv

def add_college_to_db(college: str = None) -> bool:
    code = (college['code'].strip()).upper()
    name = (college['name'].strip()).title()
    logo = college['logo']
    # code validation
    if code and code not in College().get_collegecodes():
        # name validation
        if name:
            College(
                code,
                name,
                logo
            ).add_new()
            return None
        else:
            return False
    return False
def save_image(file: str = None) -> str:
    local_upload = 'local' == getenv('LOGO_UPLOAD')
    if local_upload:
        parent_folder = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + \
                        '/static/entity_photos/colleges'
        image = file
        filename = secure_filename(file.filename)
        image.save(os.path.join(parent_folder, filename))
        return filename
    else:
        
        result = cloud.upload(file)
        url = result.get('url')
        print(url)
        return url


def delete_image(id: str = None) -> bool:
    local_upload = 'local' == getenv('LOCAL_UPLOAD')
    if not local_upload:
        image_url = (College().get_image_url(id))[0]
        file_name = (image_url.split('/')[-1]).split('.')[0]
        print(file_name)
        cloud.destroy(file_name)
    return 

def check_page_limit(min: bool = None, max: bool = None) -> str:
    if min:
        return 'min'
    elif max:
        return 'max'
    else:
        return

def check_limit_validity(number_input: int = None, max_limit: int = None) -> int:
    if number_input < 5:
        return 5
    elif number_input > max_limit:
        return max_limit
    else:
        
        return number_input

def update_college_record(college: str = None) -> bool:
    code = college['code']
    name = college['name'].strip()
    logo = college['logo']

    if name:
        if logo:
            College(
                code = code,
                name = name,
                logo= logo
            ).update()
        else:
            College(
            code = code,
            name = name
        ).update()
        return None
    else:
        return False