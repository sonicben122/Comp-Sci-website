from website import create_app
from csnews import (
    latestupdatetitle, update2title, update3title, update4title,
    latestupdateurl, update2url, update3url, update4url
)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
