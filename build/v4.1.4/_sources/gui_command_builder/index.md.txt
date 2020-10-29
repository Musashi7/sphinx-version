# GUI Command Builder

GUI Command Builder is an interactive builder of PSJ-GUI, help making Jupiter dialog or wizard by drag and drop operations. User hence does not need to know Python programming language to make UI components in Jupiter.

## Tool Menu

Perform operations related to the creation of dialogs and wizards.

![Tool menu](./../_images/GUI_CommandBuilder_MenuWindow_ToolMenu.png)

|                               Icon                               | Name                             | Description                                                          |           Shortcut Key            |
| :--------------------------------------------------------------: | :------------------------------- | :------------------------------------------------------------------- | :-------------------------------: |
|         ![New icon](./../_images/ToolMenu_icon/New.png)          | Make a new dialog                | Clear the being created settings and open a new environment          | {badge}`F5,badge-dark badge-pill` |
|        ![Open icon](./../_images/ToolMenu_icon/Open.png)         | Open an existing database        | Open and load a database file                                        | {badge}`F4,badge-dark badge-pill` |
|        ![Save icon](./../_images/ToolMenu_icon/Save.png)         | Save dialog settings to database | Save the being created dialoge settings to an external database file | {badge}`F6,badge-dark badge-pill` |
|        ![Undo icon](./../_images/ToolMenu_icon/Undo.png)         | Undo                             | Click this icon to undo the previously executed operation            |                                   |
|        ![Redo icon](./../_images/ToolMenu_icon/Redo.png)         | Redo                             | Click this icon to redo the previously cancelled operation           |                                   |
| ![Show/Hide code icon](./../_images/ToolMenu_icon/Show_hide.png) | Show or hide code window         | Switch showing or hiding the code window                             | {badge}`F1,badge-dark badge-pill` |
|     ![Preview icon](./../_images/ToolMenu_icon/Preview.png)      | Preview dialog                   | Display a preview of the being created dialog                        | {badge}`F2,badge-dark badge-pill` |
|   ![Integrate icon](./../_images/ToolMenu_icon/Integrate.png)    | Integrate                        | Save dialog to customer folder and display it in Jupiter's ribbon    | {badge}`F3,badge-dark badge-pill` |
|        ![Help icon](./../_images/ToolMenu_icon/Help.png)         | Help                             | Display a short tutorial (being created)                             |                                   |

## Tool Box Window

Contain all the components used to create dialogs and wizards.

![tool box window](./../_images/GUI_CommandBuilder_MenuWindow_ToolBox.png)

|                                   Icon                                   | Name              | Description                                                                      |
| :----------------------------------------------------------------------: | :---------------- | :------------------------------------------------------------------------------- |
|           ![Layout icon](./../_images/ToolBox_icon/Layout.png)           | Layout            | Create a layout to arrange components inside                                     |
|        ![Group Box icon](./../_images/ToolBox_icon/GroupBox.png)         | Group Box         | Create a group box which can contain some components                             |
|      ![Tab Control icon](./../_images/ToolBox_icon/TabControl.png)       | Tab Control       | Create a tab container                                                           |
|            ![Tab icon](./../_images/ToolBox_icon/TabItem.png)            | Tab Item          | Create a tab inside the tab container                                            |
|            ![Label icon](./../_images/ToolBox_icon/Label.png)            | Label             | Create a label                                                                   |
|         ![Text Box icon](./../_images/ToolBox_icon/TextBox.png)          | Text Box          | Create a text box                                                                |
| ![Rich Edit Control icon](./../_images/ToolBox_icon/RichEditControl.png) | Rich Edit Control | Create a text box that can be entered in various data formats and multiple lines |
|        ![Combo Box icon](./../_images/ToolBox_icon/ComboBox.png)         | Combo Box         | Create a combo box                                                               |
|         ![List Box icon](./../_images/ToolBox_icon/Listbox.png)          | List Box          | Create a list box                                                                |
|        ![Check box icon](./../_images/ToolBox_icon/Checkbox.png)         | Check Box         | Create a check box                                                               |
|     ![Radio button icon](./../_images/ToolBox_icon/RadioButton.png)      | Radio Button      | Create a radio button                                                            |
|           ![Button icon](./../_images/ToolBox_icon/Button.png)           | Button            | Create a button                                                                  |
|    ![Image Control icon](./../_images/ToolBox_icon/ImageControl.png)     | Image Control     | Create an image container                                                        |
|             ![Spin icon](./../_images/ToolBox_icon/Spin.png)             | Spin              | Create a spin button                                                             |
|       ![Slider bar icon](./../_images/ToolBox_icon/SliderBar.png)        | Slider Bar        | Create a slide bar                                                               |
|        ![Separator icon](./../_images/ToolBox_icon/Separator.png)        | Separator         | Create a separator line                                                          |
|  ![Open File/Folder icon](./../_images/ToolBox_icon/OpenFileFolder.png)  | Open File/Folder  | Create a open file/folder selection                                              |
|            ![Table icon](./../_images/ToolBox_icon/Table.png)            | Table             | Create a table                                                                   |
|     ![Page control icon](./../_images/ToolBox_icon/PageControl.png)      | Page Control      | Create a page container (used for wizard)                                        |
|        ![Page item icon](./../_images/ToolBox_icon/PageItem.png)         | Page Item         | Create a page inside the page container (used for wizard)                        |

Below is the detail properties for each component:

```{toctree}
:maxdepth: 1
:hidden:

component/index
```

## Hierrachy Window

All components in use are displayed in a tree format.
User can change the position, duplicate or delete components.

![Hierrachy window](./../_images/GUI_CommandBuilder_MenuWindow_Hierarchy.png)

|                                 Icon                                 | Name                               | Description                                                                          |
| :------------------------------------------------------------------: | :--------------------------------- | ------------------------------------------------------------------------------------ |
|  ![Move out icon](./../_images/Hierarchy_icon/Move_upperlevel.png)   | Move item out of current container | Move the selected component out of the current container which it is being belong to |
|  ![Move into icon](./../_images/Hierarchy_icon/Move_lowerlevel.png)  | Move item into next container      | Move the selected component into the above container                                 |
|  ![Move forward icon](./../_images/Hierarchy_icon/Move_forward.png)  | Move item forward one level        | Move the selected component up one level but still inside the current container      |
| ![Move backward icon](./../_images/Hierarchy_icon/Move_backward.png) | Move item backward one level       | Move the selected component down one level but still inside the current container    |
|      ![Copy icon](./../_images/Hierarchy_icon/Copy_insert.png)       | Copy item and insert it            | Duplicate the selected component                                                     |
|        ![Delete icon](./../_images/Hierarchy_icon/Delete.png)        | Delete selected item               | Delete the selected component                                                        |

## Properties Window

Display all properties of the selected component.
The settings of the dialog created can also be set from the Properties window.
By selecting a component in the Hierarchy window, user can change its parameters in this Properties window.

![Properties window](./../_images/GUI_CommandBuilder_MenuWindow_Properties.png)
