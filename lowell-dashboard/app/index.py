from flask_appbuilder import IndexView

# File to display custom made index.html

class MyIndexView(IndexView):
    index_template = 'my_index.html'
