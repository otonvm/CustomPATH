# CustomPATH
Inject custom paths in the Subilme Text's PATH (or technicaly the plugin containers' PATH, but that is usualy good enough).

All settings are platform-dependent. That is, on each platform (windows, osx, linux), a new settings file is created and that
is used to update that platforms' PATH.

This is usefull while syncing the `Packages\User` folder with something like Dropbox. 

## Settings
```js
{   
    // enable or disable the plugin:
    "enabled": true,
    // completly replace the original PATH: 
    "override": false,
    // list of PATHs to prepend to (or use to replace) the original PATH
    "append_to_path": [
        "/usr/local/bin",
        "$HOME/bin"
    ]
}
```
