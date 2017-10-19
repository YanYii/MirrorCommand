import sublime
import sublime_plugin


class MirrorPasteCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        content = sublime.get_clipboard()
        r = self.view.sel()[0]
        if not r.empty():
            print('Not empty')
            self.view.erase(edit, r)
        self.view.insert(edit, r.a, content)
