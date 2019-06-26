from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class DBO():
    def save(self):
        """
        Salva o objeto no banco de dados
        """
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete(self):
        """
        Deleta o objeto do banco de dados
        """
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
