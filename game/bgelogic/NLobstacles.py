# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.ConditionOnUpdate()
    ACT0001 = nodes.ActionApplyLocation()
    PAR0002 = nodes.GetObjectDataName()
    PAR0003 = nodes.ReceiveMessage()
    PAR0004 = nodes.ParameterObjectAttribute()
    ACT0005 = nodes.ActionSetObjectAttribute()
    ACT0001.local = True
    ACT0001.condition = CON0000
    ACT0001.game_object = "NLO:U_O"
    ACT0001.movement = mathutils.Vector((-0.20999999344348907, 0.0, 0.0))
    PAR0002.game_object = "NLO:U_O"
    PAR0003.subject = PAR0002
    PAR0004.game_object = "NLO:Empty.002"
    PAR0004.attribute_name = "worldPosition"
    ACT0005.condition = PAR0003.OUT
    ACT0005.xyz = {'x': True, 'y': True, 'z': False}
    ACT0005.game_object = "NLO:U_O"
    ACT0005.attribute_value = PAR0004
    ACT0005.value_type = 'worldPosition'
    network.add_cell(CON0000)
    network.add_cell(PAR0002)
    network.add_cell(PAR0004)
    network.add_cell(ACT0001)
    network.add_cell(PAR0003)
    network.add_cell(ACT0005)
    owner["IGNLTree_obstacles"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__obstacles')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_obstacles")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
