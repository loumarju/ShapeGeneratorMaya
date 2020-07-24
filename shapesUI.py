import maya.cmds as cmds


class ShapesUi:
# Properties of the window
    def __init__(self, shape_type, group_name, suffix_name):

        window_name = "win_controls"
        number_buttons_cell_width = 15
        form_offset = 2
        shapes_form = None

        self.shape_type = shape_type
        self.group_name = group_name
        self.suffix_name = suffix_name

    # method 1 to show the window
    def display(self):
        self.delete()
        main_window = cmds.window(self.window_name, title ="Creation Control Tool", rtf=True, sizeable=False)
        main_layout = cmds.rowColumnLayout(parent=main_window)


        width = columns * self.number_buttons_cell_width
        height = rows * self.number_buttons_cell_width

    # method 2 to delete if the window exists
    def delete(self):
        if cmds.window(self.window_name, exists=True):
            cmds.delete(self.window_name, window=True)

    # method 3 shape cube form
    def cube(self):
        pass

    # method 4
    def sphere(self):
        pass

    # method 5
    def piramidal(self):
        pass

ShapesUi.display()