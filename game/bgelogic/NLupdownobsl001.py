# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetObjectAttribute()
    CON0001 = nodes.ConditionOnUpdate()
    PAR0002 = nodes.ParameterObjectAttribute()
    ACT0000.condition = CON0001
    ACT0000.xyz = {'x': False, 'y': False, 'z': True}
    ACT0000.game_object = "NLO:U_O"
    ACT0000.attribute_value = PAR0002
    ACT0000.value_type = 'worldPosition'
    PAR0002.game_object = "NLO:Empty.006"
    PAR0002.attribute_name = "worldPosition"
    network.add_cell(CON0001)
    network.add_cell(PAR0002)
    network.add_cell(ACT0000)
    owner["IGNLTree_up-down-obsl.001"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__up-down-obsl.001')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_up-down-obsl.001")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
