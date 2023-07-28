# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    PAR0000 = nodes.ParameterObjectProperty()
    ACT0001 = nodes.ActionSetGameObjectGameProperty()
    ACT0002 = nodes.ActionTimeDelay()
    ACT0003 = nodes.ActionSetGameObjectGameProperty()
    ACT0004 = nodes.ActionTimeDelay()
    PAR0005 = nodes.ReceiveMessage()
    ACT0006 = nodes.ActionSetGameObjectGameProperty()
    PAR0007 = nodes.ReceiveMessage()
    ACT0008 = nodes.ActionSetGameObjectGameProperty()
    ACT0009 = nodes.ActionAddToGameObjectGameProperty()
    CON0010 = nodes.ObjectPropertyOperator()
    CON0011 = nodes.ObjectPropertyOperator()
    CON0012 = nodes.ConditionOnce()
    ACT0013 = nodes.ActionStartSound()
    CON0014 = nodes.GE_OnInit()
    ACT0015 = nodes.ActionPlayAction()
    ACT0016 = nodes.ActionStartSound()
    ACT0017 = nodes.CreateMessage()
    PAR0018 = nodes.GESetOverlayCollection()
    PAR0000.game_object = "NLO:U_O"
    PAR0000.property_name = "compass"
    ACT0001.condition = ACT0002
    ACT0001.game_object = "NLO:U_O"
    ACT0001.property_name = "compass"
    ACT0001.property_value = 0.7299996614456177
    ACT0002.condition = ACT0006.OUT
    ACT0002.delay = 0.26999998092651367
    ACT0003.condition = ACT0004
    ACT0003.game_object = "NLO:U_O"
    ACT0003.property_name = "compass"
    ACT0003.property_value = 1.0
    ACT0004.condition = ACT0001.OUT
    ACT0004.delay = 0.26999998092651367
    PAR0005.subject = "damA"
    ACT0006.condition = PAR0005.OUT
    ACT0006.game_object = "NLO:U_O"
    ACT0006.property_name = "compass"
    ACT0006.property_value = 1.5099998712539673
    PAR0007.subject = "death"
    ACT0008.condition = PAR0007.OUT
    ACT0008.game_object = "NLO:U_O"
    ACT0008.property_name = "death"
    ACT0008.property_value = True
    ACT0009.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("SUB")
    ACT0009.condition = CON0010
    ACT0009.game_object = "NLO:U_O"
    ACT0009.property_name = "compass"
    ACT0009.property_value = 0.009999999776482582
    CON0010.game_object = "NLO:U_O"
    CON0010.property_name = "death"
    CON0010.compare_value = True
    CON0010.operator = 0
    CON0011.game_object = "NLO:U_O"
    CON0011.property_name = "compass"
    CON0011.compare_value = 0.20000000298023224
    CON0011.operator = 3
    CON0012.input_condition = CON0011
    CON0012.repeat = False
    CON0012.reset_time = 0.5
    ACT0013.condition = CON0014
    ACT0013.sound = "C:/Users/Claudemir/Documents/fl musics/rock it rocket sounds/sunny nigght.mp3"
    ACT0013.loop_count = 0
    ACT0013.pitch = PAR0000
    ACT0013.volume = 0.6916666626930237
    ACT0015.condition = CON0012
    ACT0015.game_object = "NLO:transition"
    ACT0015.action_name = "Plano.001Action.001"
    ACT0015.start_frame = 1.0
    ACT0015.end_frame = 15.0
    ACT0015.layer = 0
    ACT0015.priority = 0
    ACT0015.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0015.stop = False
    ACT0015.layer_weight = 1.0
    ACT0015.speed = 1.0
    ACT0015.blendin = 0.0
    ACT0015.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0016.condition = ACT0015.STARTED
    ACT0016.sound = "C:/Users/Claudemir/Documents/fl musics/rock it rocket sounds/sunny nigght slowed.mp3"
    ACT0016.loop_count = 0
    ACT0016.pitch = 1.0
    ACT0016.volume = 0.42500001192092896
    ACT0017.condition = PAR0018
    ACT0017.subject = "tex"
    ACT0017.body = nodes.Invalid()
    ACT0017.target = "NLO:U_O"
    PAR0018.condition = CON0012
    PAR0018.camera = "NLO:Câmara"
    PAR0018.collection = "text"
    network.add_cell(PAR0000)
    network.add_cell(PAR0005)
    network.add_cell(PAR0007)
    network.add_cell(CON0010)
    network.add_cell(CON0014)
    network.add_cell(ACT0006)
    network.add_cell(ACT0009)
    network.add_cell(ACT0013)
    network.add_cell(ACT0002)
    network.add_cell(ACT0008)
    network.add_cell(ACT0001)
    network.add_cell(ACT0004)
    network.add_cell(ACT0003)
    network.add_cell(CON0011)
    network.add_cell(CON0012)
    network.add_cell(PAR0018)
    network.add_cell(ACT0015)
    network.add_cell(ACT0017)
    network.add_cell(ACT0016)
    owner["IGNLTree_level 1"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__level 1')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_level 1")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
