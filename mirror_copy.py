import sublime
import sublime_plugin


class MirrorCopyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        contents = []
        for r in self.view.sel():
            if r.empty():
                r = self.view.line(r)
            content = self.view.substr(r)
            contents.append(content)
        sublime.set_clipboard('\n\n'.join(contents))
