from website import create_app

# This file is the entry point for the app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    # debug; any time we make a change to code it will re-run webserver
    # turn off for production