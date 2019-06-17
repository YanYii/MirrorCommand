import sublime
import sublime_plugin


class MirrorCutCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        contents = []
        for r in reversed(self.view.sel()):
            if r.empty():
                r = self.view.line(r)
                r = sublime.Region(r.begin(), r.end() + 1)
            content = self.view.substr(r)
            contents.append(content)
            self.view.erase(edit, r)
        result = '\n'.join([x for x in reversed(contents)])
        sublime.set_clipboard(result)
        sublime.status_message('Cut {} characters.'.format(len(result)))
