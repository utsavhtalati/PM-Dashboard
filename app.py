from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample project data (you might use a database in a real application)
projects = [
    {"id": 1, "name": "Project A", "tasks": [{"id": 1, "description": "Task 1", "complete": False}, {"id": 2, "description": "Task 2", "complete": False}]}
    
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
        new_task = {"id": len(project['tasks']) + 1, "description": task_description, "complete": False}
        project["tasks"].append(new_task)
    
    return redirect(url_for('project', project_id=project_id))

@app.route('/complete_task/<int:project_id>/<int:task_id>')
def complete_task(project_id, task_id):
    project = next((p for p in projects if p["id"] == project_id), None)
    
    if project:
        task = next((t for t in project['tasks'] if t["id"] == task_id), None)
        
        if task:
            task["complete"] = True
    
    return redirect(url_for('project', project_id=project_id))

@app.route('/delete_task/<int:project_id>/<int:task_id>')
def delete_task(project_id, task_id):
    project = next((p for p in projects if p["id"] == project_id), None)
    
    if project:
        project["tasks"] = [t for t in project['tasks'] if t["id"] != task_id]
    
    return redirect(url_for('project', project_id=project_id))

if __name__ == '__main__':
    app.run(debug=True)
