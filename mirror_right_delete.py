import sublime
import sublime_plugin


class MirrorRightDeleteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		for sel in reversed(sels):
			if sel.begin() == sel.end():
				begin = sel.begin()
				end = sel.end()+1 if sel.end()+1 <= self.view.size() else self.view.size()
				sel = sublime.Region(begin, end)
			self.view.erase(edit, sel)
