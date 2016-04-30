import sublime
import sublime_plugin

class ResetFontSizeToDefaultCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        settings = sublime.load_settings('Preferences.sublime-settings')

        if settings.has('default_font_size'):
            settings.set('font_size', settings.get('default_font_size'))
        else:
            settings.erase('font_size')

        sublime.save_settings("Preferences.sublime-settings")