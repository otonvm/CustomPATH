import os
import sublime


def plugin_loaded():
    if sublime.platform() == "windows":
            settings_file = "CustomPATH (Windows).sublime-settings"

    elif sublime.platform() == "osx":
        settings_file = "CustomPATH (OSX).sublime-settings"

    else:
        settings_file = "CustomPATH (Linux).sublime-settings"

    settings = sublime.load_settings(settings_file)

    append_to_path = settings.get("append_to_path")

    if append_to_path is None:
        print("CustomPATH: no platform specific PATH settings found! Check readme!")
        return

    if settings.get("enabled", True):
        if settings.get("override", False):
            os.environ["PATH"] = os.pathsep.join(append_to_path)

        else:
            for path in append_to_path:
                if path not in os.environ["PATH"]:
                    new_path = "{}{}".format(path, os.pathsep) + os.environ["PATH"]
                    os.environ["PATH"] = new_path

        print("CustomPATH: new PATH:", os.environ["PATH"])
