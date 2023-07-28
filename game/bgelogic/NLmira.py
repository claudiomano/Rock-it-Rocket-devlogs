# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionMousePick()
    CON0001 = nodes.ConditionOnUpdate()
    PAR0002 = nodes.ParameterVector3Split()
    ACT0003 = nodes.ActionSetGameObjectGameProperty()
    ACT0004 = nodes.ActionSetObjectAttribute()
    CON0005 = nodes.ConditionOnUpdate()
    PAR0006 = nodes.ParameterObjectAttribute()
    ACT0007 = nodes.ActionSetObjectAttribute()
    PAR0008 = nodes.ParameterObjectAttribute()
    CON0009 = nodes.ConditionAnd()
    CON0010 = nodes.ObjectPropertyOperator()
    CON0011 = nodes.ObjectPropertyOperator()
    CON0012 = nodes.ObjectPropertyOperator()
    ACT0013 = nodes.ActionSetObjectAttribute()
    CON0014 = nodes.ObjectPropertyOperator()
    ACT0015 = nodes.ActionSetObjectAttribute()
    ACT0000.condition = CON0005
    ACT0000.camera = "NLO:Camera"
    ACT0000.property = ""
    ACT0000.xray = False
    ACT0000.distance = 100.0
    PAR0002.input_v = PAR0006
    ACT0003.condition = CON0001
    ACT0003.game_object = "NLO:U_O"
    ACT0003.property_name = "LocZ"
    ACT0003.property_value = PAR0002.OUTZ
    ACT0004.condition = ACT0000
    ACT0004.xyz = {'x': False, 'y': False, 'z': True}
    ACT0004.game_object = "NLO:U_O"
    ACT0004.attribute_value = ACT0000.OUTPOINT
    ACT0004.value_type = 'worldPosition'
    PAR0006.game_object = "NLO:U_O"
    PAR0006.attribute_name = "worldPosition"
    ACT0007.condition = CON0009
    ACT0007.xyz = {'x': False, 'y': False, 'z': True}
    ACT0007.game_object = "NLO:Esfera UV"
    ACT0007.attribute_value = PAR0008
    ACT0007.value_type = 'worldPosition'
    PAR0008.game_object = "NLO:U_O"
    PAR0008.attribute_name = "worldPosition"
    CON0009.condition_a = CON0011
    CON0009.condition_b = CON0010
    CON0010.game_object = "NLO:U_O"
    CON0010.property_name = "LocZ"
    CON0010.compare_value = 2.059999942779541
    CON0010.operator = 2
    CON0011.game_object = "NLO:U_O"
    CON0011.property_name = "LocZ"
    CON0011.compare_value = 7.78000020980835
    CON0011.operator = 3
    CON0012.game_object = "NLO:U_O"
    CON0012.property_name = "LocZ"
    CON0012.compare_value = 2.059999942779541
    CON0012.operator = 3
    ACT0013.condition = CON0012
    ACT0013.xyz = {'x': False, 'y': False, 'z': True}
    ACT0013.game_object = "NLO:Esfera UV"
    ACT0013.attribute_value = mathutils.Vector((0.0, 0.0, 2.061000108718872))
    ACT0013.value_type = 'worldPosition'
    CON0014.game_object = "NLO:U_O"
    CON0014.property_name = "LocZ"
    CON0014.compare_value = 7.78000020980835
    CON0014.operator = 2
    ACT0015.condition = CON0014
    ACT0015.xyz = {'x': False, 'y': False, 'z': True}
    ACT0015.game_object = "NLO:Esfera UV"
    ACT0015.attribute_value = mathutils.Vector((0.0, 0.0, 7.78000020980835))
    ACT0015.value_type = 'worldPosition'
    network.add_cell(CON0001)
    network.add_cell(CON0005)
    network.add_cell(PAR0008)
    network.add_cell(CON0010)
    network.add_cell(CON0012)
    network.add_cell(CON0014)
    network.add_cell(ACT0000)
    network.add_cell(ACT0004)
    network.add_cell(CON0011)
    network.add_cell(ACT0015)
    network.add_cell(PAR0006)
    network.add_cell(CON0009)
    network.add_cell(PAR0002)
    network.add_cell(ACT0007)
    network.add_cell(ACT0003)
    network.add_cell(ACT0013)
    owner["IGNLTree_mira"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__mira')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_mira")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
