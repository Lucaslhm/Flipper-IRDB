# Flipper-IRDB  

A **maintained** collective of different IR files for the Flipper! We'd love to have your additions! [See here.](https://github.com/UberGuidoZ/Flipper-IRDB/blob/main/README.md#organization)

Maintainers/Major contributors include:
* [Lucaslhm](https://github.com/Lucaslhm) (*[Maintained Repo](https://github.com/Lucaslhm/Flipper-IRDB)*)
* [UberGuidoZ](https://github.com/UberGuidoZ) (*[Maintained Fork](https://github.com/UberGuidoZ/Flipper-IRDB)*)
* [ezod](https://github.com/ezod) (*[Maintained Fork](https://github.com/logickworkshop/Flipper-IRDB)*)
* [amec0e](https://github.com/amec0e)
* [DedHedZed](https://github.com/dedhedzed)
* [SkeletonMan](https://github.com/SkeletonMan03/)
* [jaroslavmraz](https://github.com/jaroslavmraz)
* [darmiel](https://github.com/darmiel)
* [E_Surge](https://github.com/ESurge)
* [Zecred](https://github.com/bussardrobbie)
* [wdoekes](https://github.com/wdoekes)
* ... plus MANY others!

## Make your own manually!

Did you know IR files are plain text files? If a remote is missing, you might be able to [make it manually](https://github.com/RandomDebugError/irdb).

## Organization  

This repo is organized in the following fashion in descending order:  
* Device Type
* Device Brand
* Device Series (Where known/applicable)

When adding remotes to this repo, it is helpful to ensure your device name(s) follow the `brand_model.ir` naming scheme. It is also helpful to ensure your model numbers are capitalized, as per the following example:

`LG_55UN7300AUD.ir`

Please use this naming scheme for buttons.

**FOR TV**

POWER<br>
MUTE<br>
VOL+<br>
CH+<br>
VOL-<br>
CH-

**FOR AC**

POWER<br>
TEMP+<br>
TEMP-<br>
MODE<br>
SWING

**FOR AUDIO**

POWER<br>
VOL+<br>
VOL-<br>
MUTE

Lastly, it's helpful to add further information as a comment directly into the IR file if possible. Example:

`Filetype: IR signals file`<br>
`Version: 1`<br>
`#`<br>
`# Dynex EN-21669D TV` <---<br>
`#`<br>
`name: POWER`<br>

Make, model, link, or even a short description can be helpful if the name is changed (or just in general)!

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
