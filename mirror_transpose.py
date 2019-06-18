import sublime
import sublime_plugin


class MirrorTransposeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		last = None
		for sel in reversed(sels):
			content = self.view.substr(sel)
			if last:
				# print('sel {}, last {}, content {}'.format(sel, last, content))
				self.view.replace(edit, sel, last)
			last = content

		# last one replace with first one
		if last:
			self.view.replace(edit, sels[-1], last)
