def devserver():
    from application.app import app
    app.run(debug=True, port=5000)


def migrate():
    raise NotImplementedError


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        {
            'devserver': devserver,
            'migrate': migrate
        }.get(sys.argv[1], lambda: None)()
