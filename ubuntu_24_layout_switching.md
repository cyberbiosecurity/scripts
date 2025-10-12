# Ubuntu 24 [shift+alt] layout switching.
```
gsettings set org.gnome.desktop.wm.keybindings switch-input-source "['<Shift>Alt_L']"
gsettings set org.gnome.desktop.wm.keybindings switch-input-source-backward "['<Alt>Shift_L']"
```

```
gsettings get org.gnome.desktop.wm.keybindings switch-input-source
```

```
sudo apt install gnome-shell-extension-manager
```
Then, open Extension Manager -> Browse
"Quick Lang Switch"
This will remove EN-RU layout switching popup.


