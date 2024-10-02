from flask import Blueprint, render_template, request
from database.db import fetch_dropdown_options, fetch_code_by_title

# Create a Blueprint for the routes
app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def index():
    # Fetch data for dropdowns
    asset_types, buildings, departments = fetch_dropdown_options()

    # Pass data to the template
    return render_template('index.html', asset_types=asset_types, buildings=buildings, departments=departments)

@app_routes.route('/generate_tag', methods=['POST'])
def generate_tag():
    # Fetch form data
    asset_number = request.form.get('asset_number', '').strip()
    asset_type = request.form.get('asset_type', '').strip()
    building = request.form.get('building', '').strip()
    room_number = request.form.get('room_number', '').strip()
    employee_department = request.form.get('employee_department', '').strip()
    employee_id = request.form.get('employee_id', '').strip()

    # Validate inputs
    if not asset_number or not asset_number.isdigit() or len(asset_number) != 4 or int(asset_number) <= 0:
        return "Invalid Asset Number", 400
    if 'Employee asset' in asset_type:
        # No room number is required for Employee Asset
        if employee_id and (not employee_id.isdigit() or len(employee_id) != 3 or int(employee_id) <= 0):
            return "Invalid Employee ID", 400
    else:
        # Validate Room Number only for Office assets
        if not room_number.isdigit() or len(room_number) != 3 or int(room_number) <= 0:
            return "Invalid Room Number", 400

    # Fetch codes from the database
    asset_type_code = fetch_code_by_title('AssetType', asset_type)
    if not asset_type_code:
        return "Invalid Asset Type", 400

    building_code = fetch_code_by_title('Building', building)
    if not building_code:
        return "Invalid Building", 400

    department_code = fetch_code_by_title('Department', employee_department)
    if not department_code:
        return "Invalid Department", 400

    # Check if the asset is an Office asset or Employee asset based on the selection
    if 'Employee asset' in asset_type:
        # Generate tag for Employee asset
        if employee_id:
            tag = f"{asset_number}-{asset_type_code}-{department_code}-ID{employee_id.zfill(3)}"
        else:
            return "Employee ID is required for Employee asset", 400
    else:
        # Generate tag for Office asset
        tag = f"{asset_number}-{asset_type_code}-{building_code}-RN{room_number.zfill(3)}"

    return render_template('result.html', tag=tag)
