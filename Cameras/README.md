# IRUI generator description

Pass IR files as parameters to generate IRUI shutter buttons.

**Warning**: Some IR files may have limited compatibility with this generator for the following reasons:

* If the IR file contains multiple entries only the first one matching /^(\\d+sec\_)?Shutter$/ will be displayed, making other signals after it unavailable in the mobile app. Only copy these files if you only care about the first button.
* If the camera doesn't have a shutter signal but rather a special remote (for a microscope), it may have a custom IRUI file not created by the generator, or may not have an IRUI file at all.

