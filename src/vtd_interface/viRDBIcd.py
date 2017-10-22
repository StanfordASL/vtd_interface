# Automatically generated from the C message definitions

import cstruct

RDB_DEFAULT_PORT = 48190
RDB_FEEDBACK_PORT = 48191
RDB_IMAGE_PORT = 48192
RDB_MAGIC_NO = 35712
RDB_VERSION = 0x011D
RDB_SIZE_OBJECT_NAME = 32
RDB_SIZE_SCP_NAME = 64
RDB_SIZE_FILENAME = 1024
RDB_SIZE_TRLIGHT_PHASES = 8
RDB_PKG_ID_START_OF_FRAME = 1
RDB_PKG_ID_END_OF_FRAME = 2
RDB_PKG_ID_COORD_SYSTEM = 3
RDB_PKG_ID_COORD = 4
RDB_PKG_ID_ROAD_POS = 5
RDB_PKG_ID_LANE_INFO = 6
RDB_PKG_ID_ROADMARK = 7
RDB_PKG_ID_OBJECT_CFG = 8
RDB_PKG_ID_OBJECT_STATE = 9
RDB_PKG_ID_VEHICLE_SYSTEMS = 10
RDB_PKG_ID_VEHICLE_SETUP = 11
RDB_PKG_ID_ENGINE = 12
RDB_PKG_ID_DRIVETRAIN = 13
RDB_PKG_ID_WHEEL = 14
RDB_PKG_ID_PED_ANIMATION = 15
RDB_PKG_ID_SENSOR_STATE = 16
RDB_PKG_ID_SENSOR_OBJECT = 17
RDB_PKG_ID_CAMERA = 18
RDB_PKG_ID_CONTACT_POINT = 19
RDB_PKG_ID_TRAFFIC_SIGN = 20
RDB_PKG_ID_ROAD_STATE = 21
RDB_PKG_ID_IMAGE = 22
RDB_PKG_ID_LIGHT_SOURCE = 23
RDB_PKG_ID_ENVIRONMENT = 24
RDB_PKG_ID_TRIGGER = 25
RDB_PKG_ID_DRIVER_CTRL = 26
RDB_PKG_ID_TRAFFIC_LIGHT = 27
RDB_PKG_ID_SYNC = 28
RDB_PKG_ID_DRIVER_PERCEPTION = 29
RDB_PKG_ID_LIGHT_MAP = 30
RDB_PKG_ID_TONE_MAPPING = 31
RDB_PKG_ID_ROAD_QUERY = 32
RDB_PKG_ID_SCP = 33
RDB_PKG_ID_TRAJECTORY = 34
RDB_PKG_ID_DYN_2_STEER = 35
RDB_PKG_ID_STEER_2_DYN = 36
RDB_PKG_ID_PROXY = 37
RDB_PKG_ID_MOTION_SYSTEM = 38
RDB_PKG_ID_OCCLUSION_MATRIX = 39
RDB_PKG_ID_FREESPACE = 40
RDB_PKG_ID_DYN_EL_SWITCH = 41
RDB_PKG_ID_DYN_EL_DOF = 42
RDB_PKG_ID_IG_FRAME = 43
RDB_PKG_ID_RAY = 44
RDB_PKG_ID_RT_PERFORMANCE = 45
RDB_PKG_ID_CUSTOM_SCORING = 10000
RDB_PKG_ID_CUSTOM_OBJECT_CTRL_TRACK = 10001
RDB_PKG_ID_CUSTOM_LIGHT_B = 10002
RDB_PKG_ID_CUSTOM_LIGHT_A = 10003
RDB_PKG_ID_CUSTOM_LIGHT_GROUP_B = 10004
RDB_PKG_ID_CUSTOM_AUDI_FORUM = 12000
RDB_PKG_ID_CUSTOM_OPTIX_START = 12100
RDB_PKG_ID_OPTIX_BUFFER = 12101
RDB_PKG_ID_CUSTOM_OPTIX_END = 12149
RDB_PKG_ID_CUSTOM_USER_A_START = 12150
RDB_PKG_ID_CUSTOM_USER_A_END = 12174
RDB_PKG_ID_CUSTOM_USER_B_START = 12175
RDB_PKG_ID_CUSTOM_USER_B_END = 12200
RDB_OBJECT_CATEGORY_NONE = 0
RDB_OBJECT_CATEGORY_PLAYER = 1
RDB_OBJECT_CATEGORY_SENSOR = 2
RDB_OBJECT_CATEGORY_CAMERA = 3
RDB_OBJECT_CATEGORY_LIGHT_POINT = 4
RDB_OBJECT_CATEGORY_COMMON = 5
RDB_OBJECT_CATEGORY_OPENDRIVE = 6
RDB_OBJECT_TYPE_NONE = 0
RDB_OBJECT_TYPE_PLAYER_NONE = 0
RDB_OBJECT_TYPE_PLAYER_CAR = 1
RDB_OBJECT_TYPE_PLAYER_TRUCK = 2
RDB_OBJECT_TYPE_PLAYER_VAN = 3
RDB_OBJECT_TYPE_PLAYER_BIKE = 4
RDB_OBJECT_TYPE_PLAYER_PEDESTRIAN = 5
RDB_OBJECT_TYPE_PLAYER_PED_GROUP = 6
RDB_OBJECT_TYPE_POLE = 7
RDB_OBJECT_TYPE_TREE = 8
RDB_OBJECT_TYPE_BARRIER = 9
RDB_OBJECT_TYPE_OPT1 = 10
RDB_OBJECT_TYPE_OPT2 = 11
RDB_OBJECT_TYPE_OPT3 = 12
RDB_OBJECT_TYPE_PLAYER_MOTORBIKE = 13
RDB_OBJECT_TYPE_PLAYER_BUS = 14
RDB_OBJECT_TYPE_STREET_LAMP = 15
RDB_OBJECT_TYPE_TRAFFIC_SIGN = 16
RDB_OBJECT_TYPE_HEADLIGHT = 17
RDB_OBJECT_TYPE_PLAYER_TRAILER = 18
RDB_OBJECT_TYPE_BUILDING = 19
RDB_OBJECT_TYPE_PARKING_SPACE = 20
RDB_OBJECT_TYPE_ROAD_WORKS = 21
RDB_OBJECT_TYPE_ROAD_MISC = 22
RDB_OBJECT_TYPE_TUNNEL = 23
RDB_OBJECT_TYPE_LEGACY = 24
RDB_OBJECT_TYPE_VEGETATION = 25
RDB_OBJECT_TYPE_MISC_MOTORWAY = 26
RDB_OBJECT_TYPE_MISC_TOWN = 27
RDB_OBJECT_TYPE_PATCH = 28
RDB_OBJECT_TYPE_OTHER = 29
RDB_OBJECT_PLAYER_SEMI_TRAILER = 30
RDB_OBJECT_PLAYER_RAILCAR = 31
RDB_OBJECT_PLAYER_RAILCAR_SEMI_HEAD = 32
RDB_OBJECT_PLAYER_RAILCAR_SEMI_BACK = 33
RDB_OBJECT_TYPE_VEH_LIGHT_FRONT_LEFT = 34
RDB_OBJECT_TYPE_VEH_LIGHT_FRONT_RIGHT = 35
RDB_OBJECT_TYPE_VEH_LIGHT_REAR_LEFT = 36
RDB_OBJECT_TYPE_VEH_LIGHT_REAR_RIGHT = 37
RDB_OBJECT_TYPE_VEH_CABIN = 38
RDB_LANE_BORDER_UNKNOWN = 0
RDB_LANE_BORDER_NONE = 1
RDB_LANE_BORDER_POLE = 2
RDB_LANE_BORDER_BARRIER = 3
RDB_LANE_BORDER_SOFT_SHOULDER = 4
RDB_LANE_BORDER_HARD_SHOULDER = 5
RDB_LANE_BORDER_CURB = 6
RDB_ROADMARK_TYPE_NONE = 0
RDB_ROADMARK_TYPE_SOLID = 1
RDB_ROADMARK_TYPE_BROKEN = 2
RDB_ROADMARK_TYPE_CURB = 3
RDB_ROADMARK_TYPE_GRASS = 4
RDB_ROADMARK_TYPE_BOTDOT = 5
RDB_ROADMARK_TYPE_OTHER = 6
RDB_ROADMARK_COLOR_NONE = 0
RDB_ROADMARK_COLOR_WHITE = 1
RDB_ROADMARK_COLOR_RED = 2
RDB_ROADMARK_COLOR_YELLOW = 3
RDB_ROADMARK_COLOR_OTHER = 4
RDB_ROADMARK_COLOR_BLUE = 5
RDB_ROADMARK_COLOR_GREEN = 6
RDB_WHEEL_ID_FRONT_LEFT = 0
RDB_GEAR_BOX_TYPE_AUTOMATIC = 0
RDB_GEAR_BOX_TYPE_MANUAL = 1
RDB_GEAR_BOX_POS_AUTO = 0
RDB_GEAR_BOX_POS_P = 1
RDB_GEAR_BOX_POS_R = 2
RDB_GEAR_BOX_POS_N = 3
RDB_GEAR_BOX_POS_D = 4
RDB_GEAR_BOX_POS_1 = 5
RDB_GEAR_BOX_POS_2 = 6
RDB_GEAR_BOX_POS_3 = 7
RDB_GEAR_BOX_POS_4 = 8
RDB_GEAR_BOX_POS_5 = 9
RDB_GEAR_BOX_POS_6 = 10
RDB_GEAR_BOX_POS_7 = 11
RDB_GEAR_BOX_POS_8 = 12
RDB_GEAR_BOX_POS_9 = 13
RDB_GEAR_BOX_POS_10 = 14
RDB_GEAR_BOX_POS_11 = 15
RDB_GEAR_BOX_POS_12 = 16
RDB_GEAR_BOX_POS_13 = 17
RDB_GEAR_BOX_POS_14 = 18
RDB_GEAR_BOX_POS_15 = 19
RDB_GEAR_BOX_POS_16 = 20
RDB_GEAR_BOX_POS_R1 = 21
RDB_GEAR_BOX_POS_R2 = 22
RDB_GEAR_BOX_POS_R3 = 23
RDB_GEAR_BOX_POS_M = 24
RDB_GEAR_BOX_POS_M_UP = 25
RDB_GEAR_BOX_POS_M_DOWN = 26
RDB_GEAR_BOX_POS_C = 27
RDB_GEAR_BOX_POS_MS = 28
RDB_GEAR_BOX_POS_CS = 29
RDB_GEAR_BOX_POS_PS = 30
RDB_GEAR_BOX_POS_RS = 31
RDB_GEAR_BOX_POS_NS = 32
RDB_GEAR_BOX_POS_DS = 33
RDB_DRIVETRAIN_TYPE_FRONT = 0
RDB_DRIVETRAIN_TYPE_REAR = 1
RDB_DRIVETRAIN_TYPE_AWD = 2
RDB_PIX_FORMAT_RGB = 0
RDB_PIX_FORMAT_RGB_16 = 1
RDB_PIX_FORMAT_RGB_24 = 2
RDB_PIX_FORMAT_RGBA = 3
RDB_PIX_FORMAT_RGBA_16 = 4
RDB_PIX_FORMAT_RGBA_24 = 5
RDB_PIX_FORMAT_BW_8 = 6
RDB_PIX_FORMAT_BW_16 = 7
RDB_PIX_FORMAT_BW_24 = 8
RDB_PIX_FORMAT_DEPTH_8 = 9
RDB_PIX_FORMAT_DEPTH_16 = 10
RDB_PIX_FORMAT_DEPTH_24 = 11
RDB_PIX_FORMAT_RGB_32_F = 12
RDB_PIX_FORMAT_RGBA_32_F = 13
RDB_PIX_FORMAT_LUM_32_F = 14
RDB_PIX_FORMAT_LUMA_32_F = 15
RDB_PIX_FORMAT_RGB_16_F = 16
RDB_PIX_FORMAT_RGBA_16_F = 17
RDB_PIX_FORMAT_LUM_16_F = 18
RDB_PIX_FORMAT_LUMA_16_F = 19
RDB_PIX_FORMAT_DEPTH_32 = 20
RDB_PIX_FORMAT_BW_32 = 21
RDB_PIX_FORMAT_RGB_32 = 22
RDB_PIX_FORMAT_RGBA_32 = 23
RDB_PIX_FORMAT_R3_G2_B2 = 24
RDB_PIX_FORMAT_R3_G2_B2_A8 = 25
RDB_PIX_FORMAT_R5_G6_B5 = 26
RDB_PIX_FORMAT_R5_G6_B5_A16 = 27
RDB_PIX_FORMAT_RED8 = 28
RDB_PIX_FORMAT_RED16 = 29
RDB_PIX_FORMAT_RED16F = 30
RDB_PIX_FORMAT_RED24 = 31
RDB_PIX_FORMAT_RED32 = 32
RDB_PIX_FORMAT_RED32F = 33
RDB_PIX_FORMAT_RG8 = 34
RDB_PIX_FORMAT_RG16 = 35
RDB_PIX_FORMAT_RG16F = 36
RDB_PIX_FORMAT_RG32 = 37
RDB_PIX_FORMAT_RG32F = 38
RDB_PIX_FORMAT_RGB8 = 39
RDB_PIX_FORMAT_RGBA8 = 40
RDB_PIX_FORMAT_RGB8_A24 = 41
RDB_PIX_FORMAT_RGB16 = 42
RDB_PIX_FORMAT_RGB16F = 43
RDB_PIX_FORMAT_RGBA16 = 44
RDB_PIX_FORMAT_RGBA16F = 45
RDB_PIX_FORMAT_RGB32 = 46
RDB_PIX_FORMAT_RGB32F = 47
RDB_PIX_FORMAT_RGBA32 = 48
RDB_PIX_FORMAT_RGBA32F = 49
RDB_PIX_FORMAT_DEPTH8 = 50
RDB_PIX_FORMAT_DEPTH16 = 51
RDB_PIX_FORMAT_DEPTH24 = 52
RDB_PIX_FORMAT_DEPTH32 = 53
RDB_PIX_FORMAT_CUSTOM_01 = 151
RDB_PIX_FORMAT_CUSTOM_02 = 152
RDB_PIX_FORMAT_CUSTOM_03 = 153
RDB_SENSOR_TYPE_NONE = 0
RDB_SENSOR_TYPE_RADAR = 1
RDB_SENSOR_TYPE_VIDEO = 2
RDB_TRLIGHT_PHASE_OFF = 0
RDB_TRLIGHT_PHASE_STOP = 1
RDB_TRLIGHT_PHASE_STOP_ATTN = 2
RDB_TRLIGHT_PHASE_GO = 3
RDB_TRLIGHT_PHASE_GO_EXCL = 4
RDB_TRLIGHT_PHASE_ATTN = 5
RDB_TRLIGHT_PHASE_BLINK = 6
RDB_TRLIGHT_PHASE_UNKNOWN = 7
RDB_COORD_TYPE_INERTIAL = 0
RDB_COORD_TYPE_RESERVED_1 = 1
RDB_COORD_TYPE_PLAYER = 2
RDB_COORD_TYPE_SENSOR = 3
RDB_COORD_TYPE_USK = 4
RDB_COORD_TYPE_USER = 5
RDB_COORD_TYPE_WINDOW = 6
RDB_COORD_TYPE_TEXTURE = 7
RDB_COORD_TYPE_RELATIVE_START = 8
RDB_COORD_TYPE_GEO = 9
RDB_COORD_TYPE_TRACK = 10
RDB_ENV_CLOUD_STATE_OFF = 0
RDB_ENV_CLOUD_STATE_0_8 = 1
RDB_ENV_CLOUD_STATE_4_8 = 2
RDB_ENV_CLOUD_STATE_6_8 = 3
RDB_ENV_CLOUD_STATE_8_8 = 4
RDB_FUNCTION_TYPE_NONE = 0
RDB_FUNCTION_TYPE_TONE_MAPPING = 1
RDB_ROAD_TYPE_UNKNOWN = 0
RDB_ROAD_TYPE_RURAL = 1
RDB_ROAD_TYPE_MOTORWAY = 2
RDB_ROAD_TYPE_TOWN = 3
RDB_ROAD_TYPE_LOW_SPEED = 4
RDB_ROAD_TYPE_PEDESTRIAN = 5
RDB_DRIVER_SOURCE_UNKNOWN = 0
RDB_DRIVER_SOURCE_GHOSTDRIVER = 1
RDB_SHM_SIZE_TC = 5242880
RDB_FREESPACE_STATE_OBJECT_NONE = 0
RDB_FREESPACE_STATE_OBJECT_SAME_DIR = 1
RDB_FREESPACE_STATE_OBJECT_ONCOMING = 2
RDB_DYN_EL_SCOPE_UNKNOWN = 0
RDB_DYN_EL_SCOPE_STATIC_DB = 1
RDB_DYN_EL_SCOPE_DYN_OBJECT = 2
RDB_DYN_EL_SCOPE_ANY = 3
RDB_DYN_EL_SCOPE_FIRST = 4
RDB_DYN_EL_SCOPE_STATIC_DB_SIGNAL = 5
RDB_DYN_EL_SCOPE_STATIC_DB_SWITCH = 6
RDB_RAY_TYPE_UNKNOWN = 0
RDB_RAY_TYPE_EMIT = 1
RDB_RAY_TYPE_HIT = 2
RDB_PKG_FLAG_NONE = 0x0000
RDB_PKG_FLAG_EXTENDED = 0x0001
RDB_PKG_FLAG_HIDDEN = 0x0002
RDB_OBJECT_VIS_FLAG_ALL = 0xffff
RDB_OBJECT_VIS_FLAG_NONE = 0x0000
RDB_OBJECT_VIS_FLAG_GFX = 0x0001
RDB_OBJECT_VIS_FLAG_TRAFFIC = 0x0002
RDB_OBJECT_VIS_FLAG_RECORDER = 0x0004
RDB_VEHICLE_LIGHT_OFF = 0x00000000
RDB_VEHICLE_LIGHT_PARK = 0x00000001
RDB_VEHICLE_LIGHT_LOW_BEAM = 0x00000002
RDB_VEHICLE_LIGHT_HIGH_BEAM = 0x00000004
RDB_VEHICLE_LIGHT_REAR_BRAKE = 0x00000008
RDB_VEHICLE_LIGHT_REAR_DRIVE = 0x00000010
RDB_VEHICLE_LIGHT_INDICATOR_L = 0x00000020
RDB_VEHICLE_LIGHT_INDICATOR_R = 0x00000040
RDB_VEHICLE_LIGHT_FLASH = 0x00000080
RDB_VEHICLE_LIGHT_FRONT_FOG = 0x00000100
RDB_VEHICLE_LIGHT_REAR_FOG = 0x00000200
RDB_VEHICLE_LIGHT_VIRES1 = 0x00000400
RDB_VEHICLE_LIGHT_DRL = 0x00000800
RDB_VEHICLE_LIGHT_DRL_LEFT_LOW = 0x00001000
RDB_VEHICLE_LIGHT_DRL_RIGHT_LOW = 0x00002000
RDB_VEHICLE_LIGHT_EMERGENCY = 0x00004000
RDB_VEHICLE_LIGHT_INDICATOR_LAMP_ON = 0x00008000
RDB_VEHICLE_LIGHT_FORCE = 0x00010000
RDB_VEHICLE_ACC_FLAG_OFF = 0x00
RDB_VEHICLE_ACC_FLAG_DIST_1 = 0x01
RDB_VEHICLE_ACC_FLAG_DIST_2 = 0x02
RDB_VEHICLE_ACC_FLAG_DIST_3 = 0x03
RDB_VEHICLE_ACC_FLAG_TARGET = 0x04
RDB_VEHICLE_ACC_FLAG_SPEED = 0x08
RDB_VEHICLE_DISPLAY_LIGHT_OFF = 0x0000
RDB_VEHICLE_DISPLAY_LIGHT_01 = 0x0001
RDB_VEHICLE_DISPLAY_LIGHT_02 = 0x0002
RDB_VEHICLE_DISPLAY_LIGHT_03 = 0x0004
RDB_VEHICLE_DISPLAY_LIGHT_04 = 0x0008
RDB_VEHICLE_DISPLAY_LIGHT_05 = 0x0010
RDB_VEHICLE_DISPLAY_LIGHT_06 = 0x0020
RDB_VEHICLE_DISPLAY_LIGHT_07 = 0x0040
RDB_VEHICLE_DISPLAY_LIGHT_08 = 0x0080
RDB_VEHICLE_DISPLAY_LIGHT_09 = 0x0100
RDB_VEHICLE_DISPLAY_LIGHT_10 = 0x0200
RDB_VEHICLE_DISPLAY_LIGHT_11 = 0x0400
RDB_VEHICLE_DISPLAY_LIGHT_12 = 0x0800
RDB_VEHICLE_DISPLAY_LIGHT_13 = 0x1000
RDB_VEHICLE_DISPLAY_LIGHT_14 = 0x2000
RDB_VEHICLE_DISPLAY_LIGHT_15 = 0x4000
RDB_VEHICLE_DISPLAY_LIGHT_16 = 0x8000
RDB_LANE_EXISTS_OWN = 0x01
RDB_LANE_EXISTS_LEFT = 0x02
RDB_LANE_EXISTS_RIGHT = 0x04
RDB_LANE_STATUS_NONE = 0x0000
RDB_LANE_STATUS_ROADWORKS = 0x0001
RDB_LANE_STATUS_EXIT = 0x0002
RDB_LANE_STATUS_ENTRY = 0x0004
RDB_LANE_STATUS_LINKED = 0x0008
RDB_LANE_STATUS_WET = 0x0010
RDB_LANE_STATUS_SNOW = 0x0020
RDB_DRIVER_FLAG_NONE = 0x00000000
RDB_DRIVER_FLAG_INDICATOR_L = 0x00000001
RDB_DRIVER_FLAG_INDICATOR_R = 0x00000002
RDB_DRIVER_FLAG_PARKING_BRAKE = 0x00000004
RDB_DRIVER_FLAG_LIGHT_LOW_BEAM = 0x00000008
RDB_DRIVER_FLAG_LIGHT_HIGH_BEAM = 0x00000010
RDB_DRIVER_FLAG_LIGHT_FOG_FRONT = 0x00000020
RDB_DRIVER_FLAG_LIGHT_FOG_REAR = 0x00000040
RDB_DRIVER_FLAG_LIGHT_EMERGENCY = 0x00000080
RDB_DRIVER_FLAG_LIGHT_PRIORITY = 0x00000100
RDB_DRIVER_FLAG_COLLISION = 0x00000200
RDB_MOCKUP_INPUT0_MFL_PLUS = 0x00000001
RDB_MOCKUP_INPUT0_MFL_MINUS = 0x00000002
RDB_MOCKUP_INPUT0_MFL_PHONE = 0x00000004
RDB_MOCKUP_INPUT0_MFL_VOICE = 0x00000008
RDB_MOCKUP_INPUT0_MFL_UP = 0x00000010
RDB_MOCKUP_INPUT0_MFL_DOWN = 0x00000020
RDB_MOCKUP_INPUT0_MFL_DIAMOND = 0x00000040
RDB_MOCKUP_INPUT0_MFL_STAR = 0x00000080
RDB_MOCKUP_INPUT0_TURN_UP = 0x00000100
RDB_MOCKUP_INPUT0_TURN_UP_2 = 0x00000200
RDB_MOCKUP_INPUT0_TURN_DOWN = 0x00000400
RDB_MOCKUP_INPUT0_TURN_DOWN_2 = 0x00000800
RDB_MOCKUP_INPUT0_TURN_FLASHER = 0x00001000
RDB_MOCKUP_INPUT0_TURN_HIGHBEAM = 0x00002000
RDB_MOCKUP_INPUT0_TURN_CHECK = 0x00004000
RDB_MOCKUP_INPUT0_TURN_BC = 0x00008000
RDB_MOCKUP_INPUT0_ACC_BACK = 0x00010000
RDB_MOCKUP_INPUT0_ACC_BACK_2 = 0x00020000
RDB_MOCKUP_INPUT0_ACC_FWD = 0x00040000
RDB_MOCKUP_INPUT0_ACC_FWD_2 = 0x00080000
RDB_MOCKUP_INPUT0_ACC_UP = 0x00100000
RDB_MOCKUP_INPUT0_ACC_DOWN = 0x00200000
RDB_MOCKUP_INPUT0_ACC_SET = 0x00400000
RDB_MOCKUP_INPUT0_HORN = 0x00800000
RDB_MOCKUP_INPUT0_WIPER_INTERVAL = 0x03000000
RDB_MOCKUP_INPUT0_WIPER_INTERVAL_1 = 0x01000000
RDB_MOCKUP_INPUT0_WIPER_INTERVAL_2 = 0x02000000
RDB_MOCKUP_INPUT0_WIPER_INTERVAL_3 = 0x03000000
RDB_MOCKUP_INPUT0_WIPER_AUTO = 0x04000000
RDB_MOCKUP_INPUT0_WIPER_BACK = 0x08000000
RDB_MOCKUP_INPUT0_WIPER_UP = 0x10000000
RDB_MOCKUP_INPUT0_WIPER_UP_2 = 0x20000000
RDB_MOCKUP_INPUT0_WIPER_DOWN = 0x40000000
RDB_MOCKUP_INPUT1_ZBE_COUNTER = 0x0000FFFF
RDB_MOCKUP_INPUT1_ZBE_FWD = 0x00010000
RDB_MOCKUP_INPUT1_ZBE_BACK = 0x00020000
RDB_MOCKUP_INPUT1_ZBE_LEFT = 0x00040000
RDB_MOCKUP_INPUT1_ZBE_RIGHT = 0x00080000
RDB_MOCKUP_INPUT1_ZBE_PRESS = 0x00100000
RDB_MOCKUP_INPUT1_ZBE_MENU = 0x00200000
RDB_MOCKUP_INPUT1_GWS_P = 0x00400000
RDB_MOCKUP_INPUT1_GWS_LOCK = 0x00800000
RDB_MOCKUP_INPUT1_GWS_FWD = 0x01000000
RDB_MOCKUP_INPUT1_GWS_FWD_2 = 0x02000000
RDB_MOCKUP_INPUT1_GWS_BACK = 0x04000000
RDB_MOCKUP_INPUT1_GWS_BACK_2 = 0x08000000
RDB_MOCKUP_INPUT1_GWS_AUTO_N = 0x10000000
RDB_MOCKUP_INPUT1_GWS_MAN_N = 0x20000000
RDB_MOCKUP_INPUT1_GWS_MAN_PLUS = 0x40000000
RDB_MOCKUP_INPUT1_GWS_MAN_MINUS = 0x80000000
RDB_MOCKUP_INPUT2_LSZ_POTI = 0x000000FF
RDB_MOCKUP_INPUT2_LSZ_PARKING = 0x00000100
RDB_MOCKUP_INPUT2_LSZ_DRIVING = 0x00000200
RDB_MOCKUP_INPUT2_LSZ_AUTO = 0x00000300
RDB_MOCKUP_INPUT2_LSZ_FOG_FRONT = 0x00000400
RDB_MOCKUP_INPUT2_LSZ_FOG_REAR = 0x00000800
RDB_MOCKUP_INPUT2_DB_DTC = 0x00001000
RDB_MOCKUP_INPUT2_DB_PDC = 0x00002000
RDB_MOCKUP_INPUT2_DB_SEAT_HEAT_L = 0x00004000
RDB_MOCKUP_INPUT2_DB_SEAT_HEAT_R = 0x00008000
RDB_MOCKUP_INPUT2_DB_STARTER = 0x00010000
RDB_MOCKUP_INPUT2_DB_HAZARD_LIGHTS = 0x00020000
RDB_MOCKUP_INPUT2_DB_LOCK = 0x00040000
RDB_MOCKUP_INPUT2_DB_STEER_ADJUST_FWD = 0x00100000
RDB_MOCKUP_INPUT2_DB_STEER_ADJUST_BACK = 0x00200000
RDB_MOCKUP_INPUT2_DB_STEER_ADJUST_UP = 0x00400000
RDB_MOCKUP_INPUT2_DB_STEER_ADJUST_DOWN = 0x00800000
RDB_DRIVER_PERCEPTION_FLAG_NONE = 0x00000000
RDB_DRIVER_PERCEPTION_FLAG_TURN_L = 0x00000001
RDB_DRIVER_PERCEPTION_FLAG_TURN_R = 0x00000002
RDB_DRIVER_INPUT_VALIDITY_NONE = 0x00000000
RDB_DRIVER_INPUT_VALIDITY_STEERING_WHEEL = 0x00000001
RDB_DRIVER_INPUT_VALIDITY_STEERING_SPEED = 0x00000002
RDB_DRIVER_INPUT_VALIDITY_THROTTLE = 0x00000004
RDB_DRIVER_INPUT_VALIDITY_BRAKE = 0x00000008
RDB_DRIVER_INPUT_VALIDITY_CLUTCH = 0x00000010
RDB_DRIVER_INPUT_VALIDITY_TGT_ACCEL = 0x00000020
RDB_DRIVER_INPUT_VALIDITY_TGT_STEERING = 0x00000040
RDB_DRIVER_INPUT_VALIDITY_GEAR = 0x00000080
RDB_DRIVER_INPUT_VALIDITY_CURVATURE = 0x00000100
RDB_DRIVER_INPUT_VALIDITY_STEERING_TORQUE = 0x00000200
RDB_DRIVER_INPUT_VALIDITY_ENGINE_TORQUE = 0x00000400
RDB_DRIVER_INPUT_VALIDITY_TGT_SPEED = 0x00000800
RDB_DRIVER_INPUT_VALIDITY_INFO_ONLY = 0x00001000
RDB_DRIVER_INPUT_VALIDITY_ADD_ON = 0x00002000
RDB_DRIVER_INPUT_VALIDITY_FLAGS = 0x00004000
RDB_DRIVER_INPUT_VALIDITY_MOCKUP_INPUT0 = 0x00008000
RDB_DRIVER_INPUT_VALIDITY_MOCKUP_INPUT1 = 0x00010000
RDB_DRIVER_INPUT_VALIDITY_MOCKUP_INPUT2 = 0x00020000
RDB_DRIVER_INPUT_VALIDITY_STEERING_TPOS = 0x00040000
RDB_DRIVER_INPUT_VALIDITY_MODIFIED = 0x00080000
RDB_SCORING_FLAG_NONE = 0x00000000
RDB_SCORING_FLAG_COLLISION = 0x00000001
RDB_SCORING_FLAG_OFF_ROAD = 0x00000002
RDB_COORD_FLAG_NONE = 0x00
RDB_COORD_FLAG_POINT_VALID = 0x01
RDB_COORD_FLAG_ANGLES_VALID = 0x02
RDB_LIGHT_SOURCE_FLAG_NONE = 0x0000
RDB_LIGHT_SOURCE_FLAG_USE_FRUSTUM = 0x0001
RDB_LIGHT_SOURCE_FLAG_PERSISTENT = 0x0002
RDB_LIGHT_SOURCE_FLAG_STENCIL = 0x0004
RDB_SENSOR_OBJECT_FLAG_NONE = 0x0000
RDB_SENSOR_OBJECT_FLAG_CRITICALITY_LOW = 0x0001
RDB_SENSOR_OBJECT_FLAG_CRITICALITY_MEDIUM = 0x0002
RDB_SENSOR_OBJECT_FLAG_CRITICALITY_HIGH = 0x0003
RDB_ROAD_EVENT_NONE = 0x00000000
RDB_ROAD_EVENT_POTHOLE = 0x00000001
RDB_ENV_FLAG_NONE = 0x0000
RDB_ENV_FLAG_PRECIPITATION_SNOW = 0x0001
RDB_ENV_FLAG_PRECIPITATION_HAIL = 0x0002
RDB_ENV_FLAG_ROAD_SURFACE_WET = 0x0004
RDB_ENV_FLAG_STREET_LAMPS = 0x0008
RDB_SHM_ID_IMG_GENERATOR_OUT = 0x0816a
RDB_SHM_ID_IMG_GENERATOR_IN = 0x0817a
RDB_SHM_ID_CONTROL_GENERATOR_IN = 0x0817b
RDB_SHM_ID_CUSTOM_01 = 0x0818a
RDB_SHM_ID_TC_IN = 0x08200
RDB_SHM_ID_TC_OUT = 0x08201
RDB_SHM_ID_DYN_2_STEER = 0x08210
RDB_SHM_ID_STEER_2_DYN = 0x08211
RDB_SHM_BUFFER_FLAG_NONE = 0x00000000
RDB_SHM_BUFFER_FLAG_LOCK = 0x00000001
RDB_SHM_BUFFER_FLAG_TC = 0x00000002
RDB_SHM_BUFFER_FLAG_IG = 0x00000004
RDB_OBJECT_CFG_FLAG_NONE = 0x0000
RDB_OBJECT_CFG_FLAG_CTRL_EXTERN = 0x0001
RDB_OBJECT_CFG_FLAG_MODEL_ID_VALID = 0x0002
RDB_ROAD_POS_FLAG_NONE = 0x00
RDB_ROAD_POS_FLAG_DIR_FWD = 0x01
RDB_ROAD_POS_FLAG_DIR_REAR = 0x02
RDB_ROAD_POS_FLAG_OFFROAD = 0x04
RDB_CONTACT_POINT_FLAG_NONE = 0x0000
RDB_CONTACT_POINT_FLAG_PLAYER_VALID = 0x0001
RDB_SYNC_CMD_RENDER_CONTINUOUS = 0x00000080
RDB_SYNC_CMD_RENDER_PAUSE = 0x00000100
RDB_SYNC_CMD_RENDER_SINGLE_FRAME = 0x00000200
RDB_TRAJECTORY_FLAG_NONE = 0x0000
RDB_TRAJECTORY_FLAG_TIME_DOMAIN = 0x0001
RDB_DYN_2_STEER_STATE_NONE = 0x0000
RDB_DYN_2_STEER_STATE_PAUSE = 0x0001
RDB_DYN_2_STEER_STATE_RUN = 0x0002
RDB_DYN_2_STEER_STATE_ERROR = 0x0004
RDB_DYN_2_STEER_CMD_NONE = 0x0000
RDB_DYN_2_STEER_CMD_RESET = 0x0001
RDB_DYN_2_STEER_EFFECT_NONE = 0x00000000
RDB_DYN_2_STEER_EFFECT_TIRE_MODEL = 0x00000001
RDB_DYN_2_STEER_EFFECT_VIBRATION_10HZ = 0x00000002
RDB_STEER_2_DYN_STATE_OFF = 0x00000000
RDB_STEER_2_DYN_STATE_INIT = 0x00000001
RDB_STEER_2_DYN_STATE_FAIL = 0x00000002
RDB_STEER_2_DYN_STATE_RUN = 0x00000004
RDB_STEER_2_DYN_STATE_OVER_LIMITS = 0x00000008
RDB_WHEEL_FLAG_NONE = 0x0000
RDB_WHEEL_FLAG_ON_ROADMARK = 0x0001
RDB_MOTION_SYSTEM_FLAG_NONE = 0x0000
RDB_MOTION_SYSTEM_FLAG_ACTIVE = 0x0001
RDB_MOTION_SYSTEM_FLAG_ERROR = 0x0002
RDB_CUSTOM_TRACK_CTRL_FLAG_VIS_SENSOR_A = 0x0001
RDB_CUSTOM_TRACK_CTRL_FLAG_VIS_SENSOR_B = 0x0002
RDB_CUSTOM_TRACK_CTRL_FLAG_VIS_GFX = 0x0004
RDB_CUSTOM_TRACK_CTRL_FLAG_VIS_SENSOR_C = 0x0008
RDB_CUSTOM_TRACK_CTRL_FLAG_VIS_SENSOR_D = 0x0010
RDB_CUSTOM_TRACK_CTRL_FLAG_NAME_BY_ID = 0x0100
RDB_CUSTOM_TRACK_CTRL_FLAG_PLAYER_ACTIVE = 0x0200
RDB_CUSTOM_TRACK_CTRL_VALIDITY_DEFAULT = 0x00000000
RDB_CUSTOM_TRACK_CTRL_VALIDITY_TGT_ACCEL = 0x00000001
RDB_CUSTOM_TRACK_CTRL_VALIDITY_STEERING_TPOS = 0x00000002
RDB_ROAD_QUERY_FLAG_NONE = 0x0000
RDB_ROAD_QUERY_FLAG_RELATIVE_POS = 0x0001


class RDB_POINT_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         double x;
         double y;
         double z;
         unsigned char flags;
         unsigned char type;
         unsigned short system;
    """


class RDB_COORD_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         double x;
         double y;
         double z;
         float h;
         float p;
         float r;
         unsigned char flags;
         unsigned char type;
         unsigned short system;
    """


class RDB_COORD_SYSTEM_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned short id;
         unsigned short spare;
         struct RDB_COORD_t pos;
    """


class RDB_ROAD_POS_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         unsigned short roadId;
         signed char laneId;
         unsigned char flags;
         float roadS;
         float roadT;
         float laneOffset;
         float hdgRel;
         float pitchRel;
         float rollRel;
         unsigned char roadType;
         unsigned char spare1;
         unsigned short spare2;
         float pathS;
    """


class RDB_ROADMARK_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         char id;
         char prevId;
         char nextId;
         char laneId;
         float lateralDist;
         float yawRel;
         double curvHor;
         double curvHorDot;
         float startDx;
         float previewDx;
         float width;
         float height;
         double curvVert;
         double curvVertDot;
         unsigned char type;
         unsigned char color;
         unsigned short noDataPoints;
         unsigned int roadId;
         unsigned int spare1;
    """


class RDB_LANE_INFO_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned short roadId;
         char id;
         unsigned char neighborMask;
         char leftLaneId;
         char rightLaneId;
         unsigned char borderType;
         unsigned char material;
         unsigned short status;
         unsigned short type;
         float width;
         double curvVert;
         double curvVertDot;
         double curvHor;
         double curvHorDot;
         unsigned int playerId;
         unsigned int spare1;
    """


class RDB_OBJECT_CFG_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int id;
         unsigned char category;
         unsigned char type;
         short modelId;
         char name[32];
         char modelName[32];
         char fileName[1024];
         unsigned short flags;
         unsigned short spare0;
         unsigned int spare1;
    """


class RDB_GEOMETRY_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         float dimX;
         float dimY;
         float dimZ;
         float offX;
         float offY;
         float offZ;
    """


class RDB_OBJECT_STATE_BASE_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int id;
         unsigned char category;
         unsigned char type;
         unsigned short visMask;
         char name[32];
         struct RDB_GEOMETRY_t geo;
         struct RDB_COORD_t pos;
         unsigned int parent;
         unsigned short cfgFlags;
         short cfgModelId;
    """


class RDB_OBJECT_STATE_EXT_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         struct RDB_COORD_t speed;
         struct RDB_COORD_t accel;
         float traveledDist;
         unsigned int spare[3];
    """


class RDB_OBJECT_STATE_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         struct RDB_OBJECT_STATE_BASE_t base;
         struct RDB_OBJECT_STATE_EXT_t ext;
    """


class RDB_ENGINE_BASE_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         float rps;
         float load;
         unsigned int spare1[2];
    """


class RDB_ENGINE_EXT_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         float rpsStart;
         float torque;
         float torqueInner;
         float torqueMax;
         float torqueFriction;
         float fuelCurrent;
         float fuelAverage;
         float oilTemperature;
         float temperature;
    """


class RDB_ENGINE_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         struct RDB_ENGINE_BASE_t base;
         struct RDB_ENGINE_EXT_t ext;
    """


class RDB_DRIVETRAIN_BASE_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         unsigned char gearBoxType;
         unsigned char driveTrainType;
         unsigned char gear;
         unsigned char spare0;
         unsigned int spare1[2];
    """


class RDB_DRIVETRAIN_EXT_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         float torqueGearBoxIn;
         float torqueCenterDiffOut;
         float torqueShaft;
         unsigned int spare1[2];
    """


class RDB_DRIVETRAIN_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         struct RDB_DRIVETRAIN_BASE_t base;
         struct RDB_DRIVETRAIN_EXT_t ext;
    """


class RDB_WHEEL_BASE_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         unsigned char id;
         unsigned char flags;
         unsigned char spare0[2];
         float radiusStatic;
         float springCompression;
         float rotAngle;
         float slip;
         float steeringAngle;
         unsigned int spare1[4];
    """


class RDB_WHEEL_EXT_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         float vAngular;
         float forceZ;
         float forceLat;
         float forceLong;
         float forceTireWheelXYZ[3];
         float radiusDynamic;
         float brakePressure;
         float torqueDriveShaft;
         float damperSpeed;
         unsigned int spare2[4];
    """


class RDB_WHEEL_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         struct RDB_WHEEL_BASE_t base;
         struct RDB_WHEEL_EXT_t ext;
    """


class RDB_VEHICLE_SYSTEMS_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         unsigned int lightMask;
         float steering;
         float steeringWheelTorque;
         unsigned char accMask;
         unsigned char accSpeed;
         unsigned char batteryState;
         char batteryRate;
         unsigned short displayLightMask;
         unsigned short fuelGauge;
         unsigned int spare[5];
    """


class RDB_VEHICLE_SETUP_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         float mass;
         float wheelBase;
         int spare[4];
    """


class RDB_IMAGE_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int id;
         unsigned short width;
         unsigned short height;
         unsigned char pixelSize;
         unsigned char pixelFormat;
         unsigned short cameraId;
         unsigned int imgSize;
         unsigned char color[4];
         unsigned int spare1[3];
    """


class RDB_CUSTOM_LIGHT_B_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned short lightElementId;
         unsigned short width;
         unsigned short height;
         unsigned short spare0;
         unsigned int dataSize;
         unsigned int spare1[3];
    """


class RDB_CUSTOM_LIGHT_GROUP_B_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned short lightElementId;
         unsigned short groupId;
         float intensity;
         float hOffset;
         float pOffset;
         unsigned int spare[4];
    """


class RDB_FUNCTION_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int id;
         unsigned char type;
         unsigned char dimension;
         unsigned short spare;
         unsigned int dataSize;
         unsigned int spare1[4];
    """


class RDB_SENSOR_STATE_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int id;
         unsigned char type;
         unsigned char hostCategory;
         unsigned short spare0;
         unsigned int hostId;
         char name[32];
         float fovHV[2];
         float clipNF[2];
         struct RDB_COORD_t pos;
         struct RDB_COORD_t originCoordSys;
         float fovOffHV[2];
         int spare[2];
    """


class RDB_SENSOR_OBJECT_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned char category;
         unsigned char type;
         unsigned short flags;
         unsigned int id;
         unsigned int sensorId;
         double dist;
         struct RDB_COORD_t sensorPos;
         char occlusion;
         unsigned char spare0[3];
         unsigned int spare[3];
    """


class RDB_CAMERA_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned short id;
         unsigned short width;
         unsigned short height;
         unsigned short spare0;
         float clipNear;
         float clipFar;
         float focalX;
         float focalY;
         float principalX;
         float principalY;
         struct RDB_COORD_t pos;
         unsigned int spare1[4];
    """


class RDB_LIGHT_SOURCE_BASE_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned short id;
         char templateId;
         unsigned char state;
         int playerId;
         struct RDB_COORD_t pos;
         unsigned short flags;
         unsigned short spare0;
         int spare1[2];
    """


class RDB_LIGHT_SOURCE_EXT_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         float nearFar[2];
         float frustumLRBT[4];
         float intensity[3];
         float atten[3];
         int spare1[3];
    """


class RDB_LIGHT_SOURCE_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         struct RDB_LIGHT_SOURCE_BASE_t base;
         struct RDB_LIGHT_SOURCE_EXT_t ext;
    """


class RDB_CONTACT_POINT_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned short id;
         unsigned short flags;
         struct RDB_COORD_t roadDataIn;
         float friction;
         int playerId;
         int spare1;
    """


class RDB_TRAFFIC_SIGN_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int id;
         unsigned int playerId;
         float roadDist;
         struct RDB_COORD_t pos;
         int type;
         int subType;
         float value;
         unsigned int state;
         char readability;
         char occlusion;
         unsigned short spare0;
         unsigned int addOnId;
         char minLane;
         char maxLane;
         unsigned short spare;
    """


class RDB_ROAD_STATE_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         char wheelId;
         unsigned char spare0;
         unsigned short spare1;
         unsigned int roadId;
         float defaultSpeed;
         float waterLevel;
         unsigned int eventMask;
         int spare2[12];
    """


class RDB_ENVIRONMENT_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         float visibility;
         unsigned int timeOfDay;
         float brightness;
         unsigned char precipitation;
         unsigned char cloudState;
         unsigned short flags;
         float temperature;
         unsigned int spare1[7];
    """


class RDB_PED_ANIMATION_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         struct RDB_COORD_t pos;
         unsigned int spare[4];
         unsigned int noCoords;
         unsigned int dataSize;
    """


class RDB_CUSTOM_SCORING_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         float pathS;
         float roadS;
         float fuelCurrent;
         float fuelAverage;
         unsigned int stateFlags;
         float slip;
         unsigned int spare[4];
    """


class RDB_TRIGGER_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         float deltaT;
         unsigned int frameNo;
         unsigned short features;
         short spare0;
    """


class RDB_IG_FRAME_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         float deltaT;
         unsigned int frameNo;
         unsigned int spare[2];
    """


class RDB_DRIVER_CTRL_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         float steeringWheel;
         float steeringSpeed;
         float throttlePedal;
         float brakePedal;
         float clutchPedal;
         float accelTgt;
         float steeringTgt;
         double curvatureTgt;
         float steeringTorque;
         float engineTorqueTgt;
         float speedTgt;
         unsigned char gear;
         unsigned char sourceId;
         unsigned char spare0[2];
         unsigned int validityFlags;
         unsigned int flags;
         unsigned int mockupInput0;
         unsigned int mockupInput1;
         unsigned int mockupInput2;
         unsigned int spare;
    """


class RDB_DRIVER_PERCEPTION_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         float speedFromRules;
         float distToSpeed;
         float spare0[4];
         unsigned int flags;
         unsigned int spare[4];
    """


class RDB_TRAFFIC_LIGHT_BASE_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         int id;
         float state;
         unsigned int stateMask;
    """


class RDB_TRAFFIC_LIGHT_PHASE_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         float duration;
         unsigned char type;
         unsigned char spare[3];
    """


class RDB_TRAFFIC_LIGHT_EXT_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         int ctrlId;
         float cycleTime;
         unsigned short noPhases;
         unsigned int dataSize;
    """


class RDB_TRAFFIC_LIGHT_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         struct RDB_TRAFFIC_LIGHT_BASE_t base;
         struct RDB_TRAFFIC_LIGHT_EXT_t ext;
    """


class RDB_SYNC_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int mask;
         unsigned int cmdMask;
         double systemTime;
    """


class RDB_ROAD_QUERY_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned short id;
         unsigned short flags;
         unsigned short spare[2];
         double x;
         double y;
    """


class RDB_SCP_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned short version;
         unsigned short spare;
         char sender[64];
         char receiver[64];
         unsigned int dataSize;
    """


class RDB_PROXY_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned short protocol;
         unsigned short pkgId;
         unsigned int spare[6];
         unsigned int dataSize;
    """


class RDB_TRAJECTORY_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         double spacing;
         unsigned short flags;
         unsigned short noDataPoints;
         unsigned int spare[4];
    """


class RDB_MOTION_SYSTEM_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         unsigned int flags;
         struct RDB_COORD_t pos;
         struct RDB_COORD_t speed;
         unsigned int spare[6];
    """


class RDB_CUSTOM_OBJECT_CTRL_TRACK_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         unsigned short flags;
         unsigned char posType;
         char dir;
         unsigned int roadId;
         double initialRoadDeltaS;
         float targetRoadT;
         float speedTgtS;
         float minAccelS;
         float maxAccelS;
         float accelTgt;
         unsigned int validityFlags;
         unsigned int spare[4];
    """


class RDB_FREESPACE_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         float distance;
         float angleLeft;
         float angleRight;
         float distanceLeft;
         float distanceRight;
         unsigned char stateLeft;
         unsigned char stateRight;
         unsigned char stateDistance;
         unsigned char noVisibleObjects;
         unsigned int spare1[3];
    """


class RDB_DYN_EL_SWITCH_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int objectId;
         unsigned int elementId;
         unsigned char scope;
         unsigned char spare0[3];
         unsigned int state;
         unsigned int spare1[2];
    """


class RDB_DYN_EL_DOF_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int objectId;
         unsigned int elementId;
         unsigned char scope;
         unsigned char validity;
         unsigned char nValues;
         unsigned char spare0;
         unsigned int spare1[3];
    """


class RDB_END_OF_FRAME_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """

    """


class RDB_START_OF_FRAME_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """

    """


class RDB_STEER_2_DYN_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         unsigned int state;
         float angle;
         float rev;
         float torque;
         unsigned int spare[8];
    """


class RDB_DYN_2_STEER_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int playerId;
         unsigned short state;
         unsigned short cmd;
         unsigned int effects;
         float torque;
         float friction;
         float damping;
         float stiffness;
         float velocity;
         float angle;
         float neutralPos;
         float dampingMaxTorque;
         unsigned int spare[6];
    """


class RDB_RAY_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int id;
         unsigned int emitterId;
         unsigned char type;
         unsigned char spare0;
         unsigned short spare2;
         float length;
         unsigned int spare1[3];
         struct RDB_COORD_t ray;
    """


class RDB_RT_PERFORMANCE_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int noOverruns;
         unsigned int noUnderruns;
         unsigned int noMeasurements;
         float tolerance;
         float nominalFrameTime;
         float actualFrameTime;
         unsigned int spare1[6];
    """


class RDB_MSG_HDR_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned short magicNo;
         unsigned short version;
         unsigned int headerSize;
         unsigned int dataSize;
         unsigned int frameNo;
         double simTime;
    """


class RDB_MSG_ENTRY_HDR_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int headerSize;
         unsigned int dataSize;
         unsigned int elementSize;
         unsigned short pkgId;
         unsigned short flags;
    """

# class RDB_MSG_t(cstruct.CStruct):
#     __byte_order__ = cstruct.LITTLE_ENDIAN
#     __struct__ = """
#          struct RDB_MSG_HDR_t hdr;
#          struct RDB_MSG_ENTRY_HDR_t entryHdr;
#          struct RDB_MSG_UNION_t u;
#     """


class RDB_SHM_BUFFER_INFO_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int thisSize;
         unsigned int bufferSize;
         unsigned short id;
         unsigned short spare0;
         unsigned int flags;
         unsigned int offset;
         unsigned int spare1[4];
    """


class RDB_SHM_HDR_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
         unsigned int headerSize;
         unsigned int dataSize;
         unsigned char noBuffers;
    """


lookup_dict = {1: 'RDB_PKG_ID_START_OF_FRAME',
               2: 'RDB_PKG_ID_END_OF_FRAME',
               3: 'RDB_PKG_ID_COORD_SYSTEM',
               4: 'RDB_PKG_ID_COORD',
               5: 'RDB_PKG_ID_ROAD_POS',
               6: 'RDB_PKG_ID_LANE_INFO',
               7: 'RDB_PKG_ID_ROADMARK',
               8: 'RDB_PKG_ID_OBJECT_CFG',
               9: 'RDB_PKG_ID_OBJECT_STATE',
               10: 'RDB_PKG_ID_VEHICLE_SYSTEMS',
               11: 'RDB_PKG_ID_VEHICLE_SETUP',
               12: 'RDB_PKG_ID_ENGINE',
               13: 'RDB_PKG_ID_DRIVETRAIN',
               14: 'RDB_PKG_ID_WHEEL',
               15: 'RDB_PKG_ID_PED_ANIMATION',
               16: 'RDB_PKG_ID_SENSOR_STATE',
               17: 'RDB_PKG_ID_SENSOR_OBJECT',
               18: 'RDB_PKG_ID_CAMERA',
               19: 'RDB_PKG_ID_CONTACT_POINT',
               20: 'RDB_PKG_ID_TRAFFIC_SIGN',
               21: 'RDB_PKG_ID_ROAD_STATE',
               22: 'RDB_PKG_ID_IMAGE',
               23: 'RDB_PKG_ID_LIGHT_SOURCE',
               24: 'RDB_PKG_ID_ENVIRONMENT',
               25: 'RDB_PKG_ID_TRIGGER',
               26: 'RDB_PKG_ID_DRIVER_CTRL',
               27: 'RDB_PKG_ID_TRAFFIC_LIGHT',
               28: 'RDB_PKG_ID_SYNC',
               29: 'RDB_PKG_ID_DRIVER_PERCEPTION',
               30: 'RDB_PKG_ID_LIGHT_MAP',
               31: 'RDB_PKG_ID_TONE_MAPPING',
               32: 'RDB_PKG_ID_ROAD_QUERY',
               33: 'RDB_PKG_ID_SCP',
               34: 'RDB_PKG_ID_TRAJECTORY',
               35: 'RDB_PKG_ID_DYN_2_STEER',
               36: 'RDB_PKG_ID_STEER_2_DYN',
               37: 'RDB_PKG_ID_PROXY',
               38: 'RDB_PKG_ID_MOTION_SYSTEM',
               39: 'RDB_PKG_ID_OCCLUSION_MATRIX',
               40: 'RDB_PKG_ID_FREESPACE',
               41: 'RDB_PKG_ID_DYN_EL_SWITCH',
               42: 'RDB_PKG_ID_DYN_EL_DOF',
               43: 'RDB_PKG_ID_IG_FRAME',
               44: 'RDB_PKG_ID_RAY',
               45: 'RDB_PKG_ID_RT_PERFORMANCE',
               10000: 'RDB_PKG_ID_CUSTOM_SCORING',
               10001: 'RDB_PKG_ID_CUSTOM_OBJECT_CTRL_TRACK',
               10002: 'RDB_PKG_ID_CUSTOM_LIGHT_B',
               10003: 'RDB_PKG_ID_CUSTOM_LIGHT_A',
               10004: 'RDB_PKG_ID_CUSTOM_LIGHT_GROUP_B',
               12000: 'RDB_PKG_ID_CUSTOM_AUDI_FORUM',
               12100: 'RDB_PKG_ID_CUSTOM_OPTIX_START',
               12101: 'RDB_PKG_ID_OPTIX_BUFFER',
               12149: 'RDB_PKG_ID_CUSTOM_OPTIX_END',
               12150: 'RDB_PKG_ID_CUSTOM_USER_A_START',
               12174: 'RDB_PKG_ID_CUSTOM_USER_A_END',
               12175: 'RDB_PKG_ID_CUSTOM_USER_B_START',
               12200: 'RDB_PKG_ID_CUSTOM_USER_B_END'}

type_dict = {1: RDB_START_OF_FRAME_t,
             2: RDB_END_OF_FRAME_t,
             3: RDB_COORD_SYSTEM_t,
             4: RDB_COORD_t,
             5: RDB_ROAD_POS_t,
             6: RDB_LANE_INFO_t,
             7: RDB_ROADMARK_t,
             8: RDB_OBJECT_CFG_t,
             9: RDB_OBJECT_STATE_t,
             10: RDB_VEHICLE_SYSTEMS_t,
             11: RDB_VEHICLE_SETUP_t,
             12: RDB_ENGINE_t,
             13: RDB_DRIVETRAIN_t,
             # 12174: RDB_CUSTOM_USER_A_END_t,
             15: RDB_PED_ANIMATION_t,
             10000: RDB_CUSTOM_SCORING_t,
             17: RDB_SENSOR_OBJECT_t,
             18: RDB_CAMERA_t,
             19: RDB_CONTACT_POINT_t,
             10004: RDB_CUSTOM_LIGHT_GROUP_B_t,
             21: RDB_ROAD_STATE_t,
             22: RDB_IMAGE_t,
             23: RDB_LIGHT_SOURCE_t,
             24: RDB_ENVIRONMENT_t,
             25: RDB_TRIGGER_t,
             26: RDB_DRIVER_CTRL_t,
             27: RDB_TRAFFIC_LIGHT_t,
             28: RDB_SYNC_t,
             29: RDB_DRIVER_PERCEPTION_t,
             # 30: RDB_LIGHT_MAP_t,
             # 31: RDB_TONE_MAPPING_t,
             32: RDB_ROAD_QUERY_t,
             33: RDB_SCP_t,
             34: RDB_TRAJECTORY_t,
             35: RDB_DYN_2_STEER_t,
             36: RDB_STEER_2_DYN_t,
             37: RDB_PROXY_t,
             38: RDB_MOTION_SYSTEM_t,
             # 39: RDB_OCCLUSION_MATRIX_t,
             # 12200: RDB_CUSTOM_USER_B_END_t,
             41: RDB_DYN_EL_SWITCH_t,
             42: RDB_DYN_EL_DOF_t,
             43: RDB_IG_FRAME_t,
             44: RDB_RAY_t,
             45: RDB_RT_PERFORMANCE_t,
             # 12100: RDB_CUSTOM_OPTIX_START_t,
             # 12101: RDB_OPTIX_BUFFER_t,
             14: RDB_WHEEL_t,
             # 12175: RDB_CUSTOM_USER_B_START_t,
             # 12000: RDB_CUSTOM_AUDI_FORUM_t,
             16: RDB_SENSOR_STATE_t,
             10001: RDB_CUSTOM_OBJECT_CTRL_TRACK_t,
             10002: RDB_CUSTOM_LIGHT_B_t,
             40: RDB_FREESPACE_t,
             # 10003: RDB_CUSTOM_LIGHT_A_t,
             # 12149: RDB_CUSTOM_OPTIX_END_t,
             # 12150: RDB_CUSTOM_USER_A_START_t,
             20: RDB_TRAFFIC_SIGN_t,
             }
