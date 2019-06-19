import sublime
import sublime_plugin


class MirrorLeftDeleteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		for sel in reversed(sels):
			if sel.begin() == sel.end():
				begin = sel.begin() - 1 if sel.begin() > 0 else 0
				end = sel.end()
				sel = sublime.Region(begin, end)
			self.view.erase(edit, sel)


