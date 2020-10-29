# Radio Button

Create a radio button.  

![](./../../_images/GUI_CommandBuilder_Component-Parameter_RadioButton.png)  
  
Preview dialog:

![](./../../_images/GUI_CommandBuilder_Component-Parameter_RadioButton2.png)  
  
## Parameters

**Text**

Enter the text appears next to the radio button.

**Name**

Enter the name of the Radio Button component.

**Checked**

Specify the default status.

- **True** : Check On
- **False** : Check Off

**Width**

Specify the minimum width of the radio button. (in pixels)

**Height**

Specify the minimum height of the radio button. (in pixels)

**Enable**

Specify whether to enable it or not.

- **Check On** : Available
- **Check Off** : Unavailable (grayed out)

**Left text**

Display the text on the left side of the radio button.

- **Check On** : Text will be on the left side
- **Check Off** : Text will be on the default (right) side

**Group**

The below Radio Button components in the Hierarchy window will be in the same group.

## Command to use

| Command                   | Description                  | Sample Code                  |
| ----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| dlg.isbutton_checked("component name")         | Check whether the radio button is checked or not <br> Return a Boolean value (`True`/`False`) | *Input:*<br>`dlg.isbutton_checked("CheckBoxButton")`  |
| dlg.set_radiobutton_state("name", Bool)        | Specify the radio button status (checked or unchecked) | *Input:*<br>`dlg.set_radiobutton_state("CheckBox1", True)`  |
