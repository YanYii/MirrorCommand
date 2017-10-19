import sublime
import sublime_plugin


class MirrorCutCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        contents = []
        for r in reversed(self.view.sel()):
            if r.empty():
                r = self.view.line(r)
                r = sublime.Region(r.a - 1, r.b)
            content = self.view.substr(r)
            contents.append(content)
            self.view.erase(edit, r)
        print(contents)
        sublime.set_clipboard('\n\n'.join([x for x in reversed(contents)]))
