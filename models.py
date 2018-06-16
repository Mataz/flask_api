from flask_api import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    created_time = db.Column(db.DateTime, nullable=False)
    last_update_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<ID: {}, Title: {}, Description: {}, Status: {}, ' \
               'Created time: {}, Last update: {}>'.format(self.id, self.title,
                                                           self.description,
                                                           self.status,
                                                           self.created_time,
                                                           self.last_update_time)
