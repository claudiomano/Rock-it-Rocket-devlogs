# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionApplyLocation()
    PAR0001 = nodes.ReceiveMessage()
    ACT0002 = nodes.ActionPlayAction()
    PAR0003 = nodes.GetObjectDataName()
    PAR0004 = nodes.ReceiveMessage()
    PAR0005 = nodes.ParameterObjectAttribute()
    ACT0006 = nodes.ActionSetObjectAttribute()
    ACT0007 = nodes.ActionPlayAction()
    CON0008 = nodes.ConditionOnUpdate()
    CON0009 = nodes.ConditionOnUpdate()
    ACT0010 = nodes.ActionSetGameObjectGameProperty()
    ACT0011 = nodes.ActionSetPhysics()
    CON0012 = nodes.ConditionNot()
    CON0013 = nodes.ObjectPropertyOperator()
    ACT0014 = nodes.ActionSetPhysics()
    ACT0015 = nodes.ActionSetPhysics()
    CON0016 = nodes.ConditionNot()
    CON0017 = nodes.ObjectPropertyOperator()
    ACT0018 = nodes.ActionSetPhysics()
    ACT0000.local = True
    ACT0000.condition = CON0008
    ACT0000.game_object = "NLO:U_O"
    ACT0000.movement = mathutils.Vector((-0.20999999344348907, 0.0, 0.0))
    PAR0001.subject = "vai"
    ACT0002.condition = PAR0001.OUT
    ACT0002.game_object = "NLO:U_O"
    ACT0002.action_name = "KeyAction"
    ACT0002.start_frame = 1.0
    ACT0002.end_frame = 48.279998779296875
    ACT0002.layer = 0
    ACT0002.priority = 0
    ACT0002.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0002.stop = False
    ACT0002.layer_weight = 1.0
    ACT0002.speed = 1.0
    ACT0002.blendin = 0.0
    ACT0002.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    PAR0003.game_object = "NLO:U_O"
    PAR0004.subject = PAR0003
    PAR0005.game_object = "NLO:Empty.002"
    PAR0005.attribute_name = "worldPosition"
    ACT0006.condition = PAR0004.OUT
    ACT0006.xyz = {'x': True, 'y': True, 'z': False}
    ACT0006.game_object = "NLO:U_O"
    ACT0006.attribute_value = PAR0005
    ACT0006.value_type = 'worldPosition'
    ACT0007.condition = ACT0002.FINISHED
    ACT0007.game_object = "NLO:U_O"
    ACT0007.action_name = "KeyAction"
    ACT0007.start_frame = 0.0
    ACT0007.end_frame = 0.029999999329447746
    ACT0007.layer = 0
    ACT0007.priority = 0
    ACT0007.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0007.stop = False
    ACT0007.layer_weight = 1.0
    ACT0007.speed = 1.0
    ACT0007.blendin = 0.0
    ACT0007.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0010.condition = CON0009
    ACT0010.game_object = "NLO:U_O"
    ACT0010.property_name = "oksak"
    ACT0010.property_value = ACT0002.FRAME
    ACT0011.condition = CON0013
    ACT0011.game_object = "NLO:Cubo.004"
    ACT0011.activate = True
    ACT0011.free_const = False
    CON0012.condition = CON0013
    CON0013.game_object = "NLO:U_O"
    CON0013.property_name = "oksak"
    CON0013.compare_value = 10
    CON0013.operator = 2
    ACT0014.condition = CON0012
    ACT0014.game_object = "NLO:Cubo.004"
    ACT0014.activate = False
    ACT0014.free_const = False
    ACT0015.condition = CON0017
    ACT0015.game_object = "NLO:Cubo.003"
    ACT0015.activate = True
    ACT0015.free_const = False
    CON0016.condition = CON0017
    CON0017.game_object = "NLO:U_O"
    CON0017.property_name = "oksak"
    CON0017.compare_value = 19
    CON0017.operator = 2
    ACT0018.condition = CON0016
    ACT0018.game_object = "NLO:Cubo.003"
    ACT0018.activate = False
    ACT0018.free_const = False
    network.add_cell(PAR0001)
    network.add_cell(PAR0003)
    network.add_cell(PAR0005)
    network.add_cell(CON0008)
    network.add_cell(CON0013)
    network.add_cell(CON0017)
    network.add_cell(ACT0000)
    network.add_cell(PAR0004)
    network.add_cell(CON0009)
    network.add_cell(ACT0011)
    network.add_cell(ACT0015)
    network.add_cell(ACT0002)
    network.add_cell(ACT0007)
    network.add_cell(CON0012)
    network.add_cell(CON0016)
    network.add_cell(ACT0006)
    network.add_cell(ACT0014)
    network.add_cell(ACT0010)
    network.add_cell(ACT0018)
    owner["IGNLTree_obstacle-animations"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__obstacle-animations')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_obstacle-animations")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
