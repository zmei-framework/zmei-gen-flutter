from copy import copy

from zmei_generator.domain.extensions import PageExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener
from zmei_generator.contrib.web.extensions.page.block import InlinePageBlock, InlineTemplatePageBlock


class FlutterPageExtension(PageExtension):

    def __init__(self, page) -> None:
        super().__init__(page)

        self.include_child = False

    @property
    def can_inherit(self):
        return self.include_child

    def filter_blocks(self, area, blocks, platform):
        filtered = []

        if platform == FlutterPageExtension:
            for block in blocks:
                if isinstance(block, InlineTemplatePageBlock):
                    if block.template_name.startswith('theme/'):
                        new_context = copy(block.context)
                        block = InlineTemplatePageBlock(template_name='flutter/' + block.template_name, ref=block.ref)
                        block.context = new_context
                else:
                    continue

                filtered.append(block)
        else:
            # other platforms:
            filtered = []
            for block in blocks:
                if isinstance(block, InlineTemplatePageBlock):
                    continue
                filtered.append(block)

        return filtered


class FlutterPageExtensionParserListener(BaseListener):

    def enterAn_flutter(self, ctx: ZmeiLangParser.An_flutterContext):
        extension = FlutterPageExtension(self.page)
        self.application.extensions.append(
            extension
        )

        self.set_flutter(self.page, extension)

    def enterAn_flutter_child(self, ctx: ZmeiLangParser.An_flutter_childContext):
        if str(ctx.BOOL()) == 'true':
            self.page[FlutterPageExtension].include_child = True



    def set_flutter(self, page, extension):
        page.register_extension(extension)

        if page.get_parent():
            parent = page.get_parent()
            if not parent.supports(FlutterPageExtension):
                self.set_flutter(parent, extension)
