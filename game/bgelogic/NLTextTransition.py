# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionPlayAction()
    ACT0001 = nodes.ActionPlayAction()
    ACT0002 = nodes.ActionSetGameObjectGameProperty()
    ACT0003 = nodes.ActionTimeDelay()
    PAR0004 = nodes.ReceiveMessage()
    ACT0005 = nodes.ActionSetGameObjectGameProperty()
    CON0006 = nodes.ConditionAnd()
    CON0007 = nodes.ConditionKeyPressed()
    CON0008 = nodes.ObjectPropertyOperator()
    ACT0009 = nodes.ActionTimeDelay()
    ACT0010 = nodes.ActionStartGame()
    ACT0000.condition = ACT0009
    ACT0000.game_object = "NLO:U_O"
    ACT0000.action_name = "TextoAction"
    ACT0000.start_frame = 1.0
    ACT0000.end_frame = 20.0
    ACT0000.layer = 0
    ACT0000.priority = 0
    ACT0000.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0000.stop = True
    ACT0000.layer_weight = 1.0
    ACT0000.speed = 1.0
    ACT0000.blendin = 0.0
    ACT0000.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0001.condition = ACT0009
    ACT0001.game_object = "NLO:U_O"
    ACT0001.action_name = "Shader NodetreeAction.001"
    ACT0001.start_frame = 1.0
    ACT0001.end_frame = 20.0
    ACT0001.layer = 1
    ACT0001.priority = 0
    ACT0001.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0001.stop = True
    ACT0001.layer_weight = 1.0
    ACT0001.speed = 1.0
    ACT0001.blendin = 0.0
    ACT0001.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0002.condition = CON0006
    ACT0002.game_object = "NLO:U_O"
    ACT0002.property_name = "Text"
    ACT0002.property_value = "Loading..."
    ACT0003.condition = ACT0002.OUT
    ACT0003.delay = 0.14999999105930328
    PAR0004.subject = "tex"
    ACT0005.condition = ACT0009
    ACT0005.game_object = "NLO:U_O"
    ACT0005.property_name = "prop"
    ACT0005.property_value = True
    CON0006.condition_a = CON0007
    CON0006.condition_b = CON0008
    CON0007.key_code = bge.events.RKEY
    CON0007.pulse = False
    CON0008.game_object = "NLO:U_O"
    CON0008.property_name = "prop"
    CON0008.compare_value = True
    CON0008.operator = 0
    ACT0009.condition = PAR0004.OUT
    ACT0009.delay = 0.30000001192092896
    ACT0010.condition = ACT0003
    ACT0010.file_name = "//rock it rocket glitchs.blend1"
    network.add_cell(PAR0004)
    network.add_cell(CON0007)
    network.add_cell(ACT0009)
    network.add_cell(ACT0000)
    network.add_cell(ACT0005)
    network.add_cell(CON0008)
    network.add_cell(ACT0001)
    network.add_cell(CON0006)
    network.add_cell(ACT0002)
    network.add_cell(ACT0003)
    network.add_cell(ACT0010)
    owner["IGNLTree_TextTransition"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__TextTransition')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_TextTransition")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
