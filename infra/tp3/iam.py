from pulumi_gcp import projects

from tp3.config import PROJECT, STUDENTS_GROUP


students_role = projects.IAMCustomRole(
    'students',
    role_id='students',
    title='Students',
    permissions=[
        'resourcemanager.projects.get',
        'storage.buckets.list',
        'bigquery.jobs.create'
    ]
)


projects.IAMBinding(
    'students-role-binding',
    project=PROJECT,
    role=students_role.name,
    members=['group:' + STUDENTS_GROUP],
)
