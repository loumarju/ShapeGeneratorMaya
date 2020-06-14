import maya.cmds as cmds
from shapeGenerator import ShapeGenerator

class HierarchyGenerator:
    def __init__(self, group_type, group_name='', sufix_name='n_00',
                 ori_prefix='ori', off_prefix='off',
                 lvu_prefix='lvu', lvd_prefix='lvd', ctl_prefix='ctl'):
        self.group_name = group_name

        if self.group_name == '':
            self.group_name = group_type

        self.group_type = group_type
        self.sufix_name = sufix_name
        self.ori_prefix = ori_prefix
        self.off_prefix = off_prefix
        self.lvu_prefix = lvu_prefix
        self.lvd_prefix = lvd_prefix
        self.ctl_prefix = ctl_prefix
        self.hierarchy = self.create_hierarchy ()

    def create_hierarchy(self):
        control = self.create_control()
        lvd = self.create_lvd()
        self.set_as_children(control, lvd)
        lvu = self.create_lvu()
        self.set_as_children(lvu, control)
        off = self.create_off()
        self.set_as_children(off, lvu)
        ori = self.create_ori()
        self.set_as_children(ori, off)

    def create_lvd(self):
        lvd_name = self.lvd_prefix + '_' + self.group_name + '_' + self.sufix_name
        return self.create_empty_object(lvd_name)

    def create_lvu(self):
        lvu_name = self.lvu_prefix + '_' + self.group_name + '_' + self.sufix_name
        return self.create_empty_object(lvu_name)

    def create_off(self):
        off_name = self.off_prefix + '_' + self.group_name + '_' + self.sufix_name
        return self.create_empty_object(off_name)

    def create_ori(self):
        ori_name = self.ori_prefix + '_' + self.group_name + '_' + self.sufix_name
        self.create_empty_object(ori_name)

    def set_as_children(self, parent, children):
        cmds.parent(children, parent)

    def create_empty_object(self, empty_name):
        return cmds.group(em=True, name=empty_name)

    def create_control(self):
        control_name = self.ctl_prefix + '_' + self.group_name + '_' + self.sufix_name
        control_generator = ShapeGenerator(self.group_type, control_name)
        control = control_generator.shape
        return control
