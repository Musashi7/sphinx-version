# Check Box

Create a check box.  

![](./../../_images/GUI_CommandBuilder_Component-Parameter_CheckBox.png)  
  
Preview dialog:

![](./../../_images/GUI_CommandBuilder_Component-Parameter_CheckBox2.png)
  
## Parameters

**Text**

Enter the text appears next to the check box.

**Name**

Enter the name of the check box component.

**Checked**

Specify the default status.

- **Check On** : Checked.
- **Check Off** : Not Checked

**Width**

Specify the minimum width of the check box. (in pixels)

**Height**

Specify the minimum height of the check box. (in pixels)

**Enable**

Specify whether to enable it or not.

- **Check On** : Available
- **Check Off** : Unavailable (grayed out)

**Left text**

   Display the text on the left side of the check box.

- **Check On** : Text will be on the left side
- **Check Off** : Text will be on the default (right) side

## Command to use

| Command                                                     | Description                                                  | Sample Code                                                  |
| ----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| dlg.isbutton_checked("component name")                        | Check if the check box is checked or not<br> Returns a Boolean value (`True`/`False`)    | *Input:*<br>`dlg.isbutton_checked("CheckBoxButton")`    |
| dlg.set_checkbox_state("name", Bool)                       | Specify the status (checked/unchecked) of the check box   | *Input:*<br>`dlg.set_checkbox_state("CheckBox1", True)`    |
