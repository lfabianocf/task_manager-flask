from todo_project import app, db

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print("DB init error:", e)

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
