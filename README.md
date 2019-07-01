# MACHIN3tools
A collection of blender python scripts. w/ slow init temp fix

All credits of this script goes to it's original creator, machin3io.  
https://github.com/machin3io/MACHIN3tools

## Changes
I've added a bypass to get_addon() as a temp fix to the very slow plugin initiation after updating blender.  
The bypass skips the get_addon() checks and always return true.  
Not the most elegant solution, but fixes the issue for me.

Alternatively, if you have none of the following plguins: DECALmachine, Group Pro, BatchOps  
You can change the line I've added from returning 'return True, None, None, None' to 'return False, None, None, None'
