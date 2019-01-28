from textwrap import dedent

from zmei_gen_flutter.extensions.page.flutter import FlutterPageExtension
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_page_flutter():
    app = _("""

        [boo]
        @flutter
        
        #foo
        ------
        lala
    """)

    assert len(app.pages) == 1

    assert app.flutter is True
    boo = app.pages['boo']

    assert boo.name == 'boo'
    assert isinstance(boo.flutter, FlutterPageExtension)


def test_page_flutter_parent_is_also_flutter():
    app = _("""
    
        [foo]

        [foo->boo]
        @flutter
        
        #foo
        ------
        lala
    """)

    assert len(app.pages) == 2

    assert app.flutter is True
    boo = app.pages['boo']
    foo = app.pages['foo']

    assert boo.name == 'boo'
    assert isinstance(boo.flutter, FlutterPageExtension)
    assert isinstance(foo.flutter, FlutterPageExtension)


def test_page_flutter_child_if_not_marked():
    app = _("""
    
        [foo]
        @flutter()

        [foo->boo]
    """)

    assert len(app.pages) == 2

    assert app.flutter is True
    foo = app.pages['foo']
    boo = app.pages['boo']

    assert boo.name == 'boo'
    assert isinstance(foo.flutter, FlutterPageExtension)
    assert foo.flutter.include_child is False
    assert not boo.flutter


def test_page_flutter_child_if_marked():
    app = _("""
    
        [foo]
        @flutter(child: true)

        [foo->boo]
    """)

    assert len(app.pages) == 2

    assert app.flutter is True
    foo = app.pages['foo']
    boo = app.pages['boo']

    assert boo.name == 'boo'
    assert isinstance(foo.flutter, FlutterPageExtension)
    print(foo.flutter.include_child)
    assert foo.flutter.include_child is True
    assert isinstance(boo.flutter, FlutterPageExtension)


def test_page_flutter_child_if_marked_deeper():
    app = _("""
    
        [foo]
        @flutter(child: true)

        [foo->boo]
        [boo->zoo]
    """)

    assert len(app.pages) == 3

    assert app.flutter is True
    foo = app.pages['foo']
    boo = app.pages['boo']
    zoo = app.pages['zoo']

    assert boo.name == 'boo'
    assert isinstance(foo.flutter, FlutterPageExtension)
    assert foo.flutter.include_child is True

    assert isinstance(boo.flutter, FlutterPageExtension)
    assert isinstance(zoo.flutter, FlutterPageExtension)
    assert zoo.flutter is foo.flutter

