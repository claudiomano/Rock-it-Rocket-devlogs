# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.GE_OnInit()
    ACT0001 = nodes.ActionApplyImpulse()
    PAR0002 = nodes.ParameterVector3Simple()
    ACT0003 = nodes.ActionRandomFloat()
    ACT0004 = nodes.ActionRandomFloat()
    ACT0005 = nodes.ActionRandomFloat()
    ACT0006 = nodes.ActionRandomFloat()
    PAR0007 = nodes.ParameterVector3Simple()
    ACT0008 = nodes.ActionApplyTorque()
    PAR0009 = nodes.ParameterArithmeticOp()
    PAR0010 = nodes.ParameterArithmeticOp()
    ACT0001.local = True
    ACT0001.condition = CON0000
    ACT0001.game_object = "NLO:U_O"
    ACT0001.point = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0001.impulse = PAR0002.OUTV
    PAR0002.input_x = ACT0003.DONE
    PAR0002.input_y = 0.0
    PAR0002.input_z = ACT0004.DONE
    ACT0003.condition = 1.2999999523162842
    ACT0003.max_value = 1.0
    ACT0004.condition = 1.0
    ACT0004.max_value = -1.2999999523162842
    ACT0005.condition = 2.299999952316284
    ACT0005.max_value = 2.0
    ACT0006.condition = 2.0
    ACT0006.max_value = -2.299999952316284
    PAR0007.input_x = PAR0009
    PAR0007.input_y = 0.0
    PAR0007.input_z = PAR0010
    ACT0008.local = True
    ACT0008.condition = CON0000
    ACT0008.game_object = "NLO:U_O"
    ACT0008.torque = PAR0007.OUTV
    PAR0009.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0009.operand_a = ACT0005.DONE
    PAR0009.operand_b = 2.0
    PAR0010.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0010.operand_a = ACT0006.DONE
    PAR0010.operand_b = 2.0
    network.add_cell(CON0000)
    network.add_cell(ACT0003)
    network.add_cell(ACT0005)
    network.add_cell(PAR0009)
    network.add_cell(ACT0004)
    network.add_cell(PAR0002)
    network.add_cell(ACT0001)
    network.add_cell(ACT0006)
    network.add_cell(PAR0010)
    network.add_cell(PAR0007)
    network.add_cell(ACT0008)
    owner["IGNLTree_particle"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__particle')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_particle")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
