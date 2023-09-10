<img src="https://github.com/logickworkshop/Flipper-IRDB/assets/71837281/45975652-d443-4fc1-9fdf-e931ffd20c5d" width="100%" />

<p align="center">
    A maintained collective of different IR files for the <a href="https://flipperzero.one/">Flipper Zero</a>!
</p>

## Installation

### Method 1: Copy Files to SD Card

Directly copying the .ir files to the Flipper's SD card is the fastest and safest method, but you have to [dismount the SD card](https://docs.flipperzero.one/basics/sd-card#g4-removing-the-sd-card) and plug it into the computer directly.

1. [Download and extract](https://github.com/logickworkshop/Flipper-IRDB/archive/refs/heads/main.zip) or [Git-clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repo to your computer.
2. Open the downloaded / cloned repository in a File Explorer.
3. [Dismount the SD card](https://docs.flipperzero.one/basics/sd-card#g4-removing-the-sd-card) from the Flipper and mount it to your computer
4. Copy the desired files from the Flipper-IRDB to the `infrared/` folder on your SD Card
5. Dismount the SD card from your computer and mount it to your Flipper

### Method 2: Copy Files using [QFlipper](https://flipperzero.one/update)

> [!IMPORTANT]
> Because of Flipper limitations, the transfer via QFlipper can take a long time, depending on how many files you want to copy.
> If you only want to copy several files, this will work fine, but if you want to load the entire Flipper-IRDB onto your Flipper, **we strongly recommend copying the files directly onto the SD card**.

1. [Git-clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) or [Download and extract](https://github.com/logickworkshop/Flipper-IRDB/archive/refs/heads/main.zip) this repository to your computer.
2. Connect your Flipper to your PC using a USB-C cable.
3. Open [QFlipper](https://flipperzero.one/update)
4. Verify that your Flipper shows "Connected"
5. Ensure your Flipper is fully up-to-date:
   1. Look for the green "Update" button near the middle-right of the application.
   2. Press "Update" and allow the Flipper to complete the Update process and then reboot before continuing.
6. Open the File Manager by selecting the "File Manager" icon (piece of paper) on the top left of the QFlipper application.
7. Select `SD Card`, then navigate to the `infrared` folder by double-clicking its icon.
8. Drag the downloaded `.ir` files you want on your Flipper from the File Explorer into the QFlipper File Manager.


## Contributing

We welcome contributions to Flipper-IRDB! 
If you have any IR files that are not included in the repository, **we would love to have your additions**.

This repo is organized in the following fashion in descending order:

> `Device Type` > `Device Brand` > `Device Series` (if known/applicable)

When adding remotes to this repo, it is helpful to ensure your device name(s) follow the `<brand>_<model>.ir` naming scheme.
It is also helpful to ensure your model numbers are capitalized, as per the following examples:

* :white_check_mark: `LG_55UN7300AUD.ir`
* :x: `LG_55UN7300AUD.txt` (wrong extension)
* :x: `lg_55un7300aud.ir` (model numbers not capitalized)
* :x: `tv.ir` (too generic)

It's helpful to add further information as a comment directly into the IR file if possible. 
Make, model, link, or even a short description can be helpful if the name is changed 
(or just in general).

```bash
Filetype: IR signals file
Version: 1
#
# Dynex EN-21669D TV <--
#
name: Power
```

### Naming Scheme

Please use this naming scheme for buttons. 
This helps us create universal assets more easily and maintain cosistency.

| TVs       | Audio    | ACs       |
| --------- | -------- | --------- |
| `Power`   | `Power`  | `Off`     |
| `Vol_up`  | `Vol_up` | `Cool_hi` |
| `Vol_dn`  | `Vol_dn` | `Cool_lo` |
| `Ch_next` | `Next`   | `Heat_hi` |
| `Ch_prev` | `Prev`   | `Heat_lo` |
| `Mute`    | `Mute`   | `Dh`      |
|           | `Play`   |           |
|           | `Pause`  |           |


## Universal Remotes

The maintainers (mostly [amec0e](https://github.com/amec0e)) add individual additions to the various Universal Remotes in [unleashed-firmware](https://github.com/DarkFlippers/unleashed-firmware), which are adapted by many other firmware options.
If you would like to contribute to the Universal Remotes, please make sure to follow the [naming scheme](#naming-scheme) above. 
For ACs, [this is an important read](https://github.com/flipperdevices/flipperzero-firmware/blob/dev/documentation/UniversalRemotes.md).


## Make your own manually!

Did you know IR files are plain text files? 
If a remote is missing, you might be able to [make it manually](https://github.com/RandomDebugError/irdb).


## Maintainers

Maintainers / Major contributors include:

<table>
    <tr>
        <td align="center" valign="top" width="14.28%">
            <a href="https://github.com/Lucaslhm">
                <img src="https://avatars.githubusercontent.com/Lucaslhm?v=3?s=100" width="100px;" alt="Lucaslhm" />
                <br />
                <sub><b>Lucaslhm</b>
            </a>
        </td>
        <td align="center" valign="top" width="14.28%">
            <a href="https://github.com/UberGuidoZ">
                <img src="https://avatars.githubusercontent.com/UberGuidoZ?v=3?s=100" width="100px;" alt="UberGuidoZ" />
                <br />
                <sub><b>UberGuidoZ</b>
            </a>
        </td>
        <td align="center" valign="top" width="14.28%">
            <a href="https://github.com/ezod">
                <img src="https://avatars.githubusercontent.com/ezod?v=3?s=100" width="100px;" alt="ezod" />
                <br />
                <sub><b>ezod</b>
            </a>
        </td>
        <td align="center" valign="top" width="14.28%">
            <a href="https://github.com/amec0e">
                <img src="https://avatars.githubusercontent.com/amec0e?v=3?s=100" width="100px;" alt="amec0e" />
                <br />
                <sub><b>amec0e</b>
            </a>
        </td>
        <td align="center" valign="top" width="14.28%">
            <a href="https://github.com/darmiel">
                <img src="https://avatars.githubusercontent.com/darmiel?v=3?s=100" width="100px;" alt="darmiel" />
                <br />
                <sub><b>darmiel</b>
            </a>
        </td>
        <td align="center" valign="top" width="14.28%">
            <a href="https://github.com/dedhedzed">
                <img src="https://avatars.githubusercontent.com/dedhedzed?v=3?s=100" width="100px;" alt="dedhedzed" />
                <br />
                <sub><b>dedhedzed</b>
            </a>
        </td>
        <td align="center" valign="top" width="14.28%">
            <a href="https://github.com/SkeletonMan03">
                <img src="https://avatars.githubusercontent.com/SkeletonMan03?v=3?s=100" width="100px;" alt="SkeletonMan03" />
                <br />
                <sub><b>SkeletonMan03</b>
            </a>
        </td>
    </tr>
    <tr>
        <td align="center" valign="top" width="14.28%">
            <a href="https://github.com/sealldeveloper">
                <img src="https://avatars.githubusercontent.com/sealldeveloper?v=3?s=100" width="100px;" alt="sealldeveloper" />
                <br />
                <sub><b>sealldeveloper</b>
            </a>
        </td>
        <td align="center" valign="top" width="14.28%">
            <a href="https://github.com/jaroslavmraz">
                <img src="https://avatars.githubusercontent.com/jaroslavmraz?v=3?s=100" width="100px;" alt="jaroslavmraz" />
                <br />
                <sub><b>jaroslavmraz</b>
            </a>
        </td>
        <td align="center" valign="top" width="14.28%">
            <a href="https://github.com/ESurge">
                <img src="https://avatars.githubusercontent.com/ESurge?v=3?s=100" width="100px;" alt="ESurge" />
                <br />
                <sub><b>ESurge</b>
            </a>
        </td>
        <td align="center" valign="top" width="14.28%">
            <a href="https://github.com/bussardrobbie">
                <img src="https://avatars.githubusercontent.com/bussardrobbie?v=3?s=100" width="100px;" alt="bussardrobbie" />
                <br />
                <sub><b>bussardrobbie</b>
            </a>
        </td>
        <td align="center" valign="top" width="14.28%">
            <a href="https://github.com/wdoekes">
                <img src="https://avatars.githubusercontent.com/wdoekes?v=3?s=100" width="100px;" alt="wdoekes" />
                <br />
                <sub><b>wdoekes</b>
            </a>
        </td>
        <td align="center" valign="top" width="14.28%">
            <a href="https://github.com/emptythevoid">
                <img src="https://avatars.githubusercontent.com/emptythevoid?v=3?s=100" width="100px;" alt="emptythevoid" />
                <br />
                <sub><b>emptythevoid</b>
            </a>
        </td>
        <td align="center" valign="center" width="14.28%">
            plus <a href="https://github.com/logickworkshop/Flipper-IRDB/graphs/contributors"><i>MANY</i> others</a>!
        </td>
    </tr>
</table>
