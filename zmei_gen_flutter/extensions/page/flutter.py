from zmei_generator.domain.extensions import PageExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class FlutterPageExtension(PageExtension):

    def __init__(self, page) -> None:
        super().__init__(page)

        self.include_child = False


class FlutterPageExtensionParserListener(BaseListener):

    def enterAn_flutter(self, ctx: ZmeiLangParser.An_flutterContext):
        extension = FlutterPageExtension(self.page)
        self.application.extensions.append(
            extension
        )

        self.set_flutter(self.page, extension)
        print('Flutter', self.application)
        self.application.flutter = True

    def enterAn_flutter_child(self, ctx: ZmeiLangParser.An_flutter_childContext):
        if str(ctx.BOOL()) == 'true':
            self.page.flutter.include_child = True

    def set_flutter(self, page, extension):
        page._flutter = extension

        if page.get_parent():
            parent = page.get_parent()
            if not parent._flutter:
                self.set_flutter(parent, extension)
