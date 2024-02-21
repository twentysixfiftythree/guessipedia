def deploy():
    from app import create_app, db
    from flask_migrate import migrate, upgrade, init, stamp
    from models import WikipediaPage

    app = create_app()
    app.app_context().push()

    db.create_all()

    stamp()
    migrate()
    upgrade()

deploy()