# Flipper-IRDB  

A **maintained** collective of different IRs for the Flipper! _(Maintainers: [ezod](https://github.com/ezod), [UberGuidoZ](https://github.com/UberGuidoZ), [DedHedZed](https://github.com/dedhedzed), [E_Surge](https://github.com/ESurge), [Zecred](https://github.com/bussardrobbie), [SkeletonMan](https://github.com/SkeletonMan03/), [Lucaslhm](https://github.com/Lucaslhm), and many others)_

## Organization  

This repo is organized in the following fashion in descending order:  
* Device Type
* Device Brand
* Device Series (Where known/applicable)

When adding remotes to this repo, it is helpful to ensure your device name(s) follow the `brand_model.ir` naming scheme. It is also helpful to ensure your model numbers are capitalized, as per the following example:

`LG_55UN7300AUD.ir`

Lastly, it's helpful to add further information as a comment directly into the IR file if possible. Example:

`Filetype: IR signals file`<br>
`Version: 1`<br>
`#`<br>
`# Dynex EN-21669D TV` <---<br>
`#`<br>
`name: Power`<br>

Make, model, link, or even a short description can be helpful if the name is changed or just in general!

## To Install New Remotes On Your Flipper:   

1. Git clone this repo to your local PC. [Multiple options are explained here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
2. Open the cloned repository in a File Explorer.
3. Connect your Flipper to your PC using a USB-C cable.
4. Open [QFlipper](https://flipperzero.one/update)
5. Verify that your Flipper shows "Connected"
6. Ensure your Flipper is fully up-to-date:
    1. Look for the green "Update" button near the middle-right of the application.
    2. Press "Update" and allow the Flipper to complete the Update process and then reboot before continuing.
7. Open the File Manager by selecting the "File Manager" icon (piece of paper) on the top left of the QFlipper application.
8. Select `SD Card`, then navigate to the `infrared` folder by double-clicking its icon.
9. Drag the .ir files you want on your Flipper from the File Explorer into the QFlipper File Manager.
10. Disconnect the Flipper from the PC and have fun!

NOTE: If you plan to copy them all, it's highly recommended to [dismount the SD card](https://docs.flipperzero.one/basics/sd-card#g4-removing-the-sd-card) and plug it into the computer directly.
