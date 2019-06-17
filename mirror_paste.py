import sublime
import sublime_plugin


class MirrorPasteCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        content = sublime.get_clipboard()
        lines = content.split('\n')
        sels = self.view.sel()
        if len(lines) == len(sels):
        	self.line_paste(edit, sels, lines)
        else:
        	self.total_paste(edit, sels, content)

    def line_paste(self, edit, sels, lines):
    	for (sel, line) in (zip(reversed(sels), reversed(lines))):
    		self.view.replace(edit, sel, line)

    def total_paste(self, edit, sels, content):
    	for sel in reversed(sels):
    		self.view.replace(edit, sel, content)
