import bpy
from .. utils.registration import get_prefs



class MenuMACHIN3tools(bpy.types.Menu):
    bl_idname = "MACHIN3_MT_MACHIN3tools"
    bl_label = "MACHIN3"

    def draw(self, context):
        layout = self.layout

        if getattr(bpy.types, "MACHIN3_OT_unmirror", False):
            layout.operator("machin3.unmirror", text="Un-Mirror")


class MenuAppendMaterials(bpy.types.Menu):
    bl_idname = "MACHIN3_MT_append_materials"
    bl_label = "Append Materials"

    def draw(self, context):
        layout = self.layout

        names = [mat.name for mat in get_prefs().appendmats]

        if names:
            names.insert(0, "ALL")
        else:
            layout.label(text="No Materials added yet!", icon="ERROR")
            layout.label(text="Check MACHIN3tools prefs.", icon="INFO")


        for name in names:

            if name == "ALL":
                layout.operator("machin3.append_material", text=name, icon="MATERIAL_DATA").name = name
                layout.separator()

            elif name == "---":
                layout.separator()

            else:
                mat = bpy.data.materials.get(name)
                icon_val = layout.icon(mat) if mat else 0

                layout.operator("machin3.append_material", text=name, icon_value=icon_val).name = name
