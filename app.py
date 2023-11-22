from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample project data (you might use a database in a real application)
projects = [
    {"id": 1, "name": "Project A", "tasks": ["Task 1", "Task 2"]},
    {"id": 2, "name": "Project B", "tasks": ["Task 3", "Task 4"]},
]

@app.route('/')
def index():
    return render_template('index.html', projects=projects)

@app.route('/project/<int:project_id>')
def project(project_id):
    project = next((p for p in projects if p["id"] == project_id), None)
    if project:
        return render_template('project.html', project=project)
    else:
        return "Project not found", 404

@app.route('/add_task/<int:project_id>', methods=['POST'])
def add_task(project_id):
    task_description = request.form.get('task_description')
    project = next((p for p in projects if p["id"] == project_id), None)
    
    if project and task_description:
        project["tasks"].append(task_description)
    
    return redirect(url_for('project', project_id=project_id))

if __name__ == '__main__':
    app.run(debug=True)
