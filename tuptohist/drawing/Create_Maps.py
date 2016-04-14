"""
Here is defined correspondance between number of a readout sectors in STTrackTuple algorithm and their names.
"""

import pickle

def IT_Map():
    IT_Map = {
    308:"IT3CSideX2Sector1",
    309:"IT3CSideX2Sector2",
    310:"IT3CSideX2Sector3",
    311:"IT3CSideX2Sector4",
    312:"IT3CSideX2Sector5",
    313:"IT3CSideX2Sector6",
    314:"IT3CSideX2Sector7",
    280:"IT3CSideVSector1",
    281:"IT3CSideVSector2",
    282:"IT3CSideVSector3",
    283:"IT3CSideVSector4",
    284:"IT3CSideVSector5",
    285:"IT3CSideVSector6",
    286:"IT3CSideVSector7",
    252:"IT3CSideUSector1",
    253:"IT3CSideUSector2",
    254:"IT3CSideUSector3",
    255:"IT3CSideUSector4",
    256:"IT3CSideUSector5",
    257:"IT3CSideUSector6",
    258:"IT3CSideUSector7",
    224:"IT3CSideX1Sector1",
    225:"IT3CSideX1Sector2",
    226:"IT3CSideX1Sector3",
    227:"IT3CSideX1Sector4",
    228:"IT3CSideX1Sector5",
    229:"IT3CSideX1Sector6",
    230:"IT3CSideX1Sector7",
    315:"IT3ASideX2Sector1",
    316:"IT3ASideX2Sector2",
    317:"IT3ASideX2Sector3",
    318:"IT3ASideX2Sector4",
    319:"IT3ASideX2Sector5",
    320:"IT3ASideX2Sector6",
    321:"IT3ASideX2Sector7",
    287:"IT3ASideVSector1",
    288:"IT3ASideVSector2",
    289:"IT3ASideVSector3",
    290:"IT3ASideVSector4",
    291:"IT3ASideVSector5",
    292:"IT3ASideVSector6",
    293:"IT3ASideVSector7",
    259:"IT3ASideUSector1",
    260:"IT3ASideUSector2",
    261:"IT3ASideUSector3",
    262:"IT3ASideUSector4",
    263:"IT3ASideUSector5",
    264:"IT3ASideUSector6",
    265:"IT3ASideUSector7",
    231:"IT3ASideX1Sector1",
    232:"IT3ASideX1Sector2",
    233:"IT3ASideX1Sector3",
    234:"IT3ASideX1Sector4",
    235:"IT3ASideX1Sector5",
    236:"IT3ASideX1Sector6",
    237:"IT3ASideX1Sector7",
    322:"IT3BottomX2Sector1",
    323:"IT3BottomX2Sector2",
    324:"IT3BottomX2Sector3",
    325:"IT3BottomX2Sector4",
    326:"IT3BottomX2Sector5",
    327:"IT3BottomX2Sector6",
    328:"IT3BottomX2Sector7",
    294:"IT3BottomVSector1",
    295:"IT3BottomVSector2",
    296:"IT3BottomVSector3",
    297:"IT3BottomVSector4",
    298:"IT3BottomVSector5",
    299:"IT3BottomVSector6",
    300:"IT3BottomVSector7",
    266:"IT3BottomUSector1",
    267:"IT3BottomUSector2",
    268:"IT3BottomUSector3",
    269:"IT3BottomUSector4",
    270:"IT3BottomUSector5",
    271:"IT3BottomUSector6",
    272:"IT3BottomUSector7",
    238:"IT3BottomX1Sector1",
    239:"IT3BottomX1Sector2",
    240:"IT3BottomX1Sector3",
    241:"IT3BottomX1Sector4",
    242:"IT3BottomX1Sector5",
    243:"IT3BottomX1Sector6",
    244:"IT3BottomX1Sector7",
    329:"IT3TopX2Sector1",
    330:"IT3TopX2Sector2",
    331:"IT3TopX2Sector3",
    332:"IT3TopX2Sector4",
    333:"IT3TopX2Sector5",
    334:"IT3TopX2Sector6",
    335:"IT3TopX2Sector7",
    301:"IT3TopVSector1",
    302:"IT3TopVSector2",
    303:"IT3TopVSector3",
    304:"IT3TopVSector4",
    305:"IT3TopVSector5",
    306:"IT3TopVSector6",
    307:"IT3TopVSector7",
    273:"IT3TopUSector1",
    274:"IT3TopUSector2",
    275:"IT3TopUSector3",
    276:"IT3TopUSector4",
    277:"IT3TopUSector5",
    278:"IT3TopUSector6",
    279:"IT3TopUSector7",
    245:"IT3TopX1Sector1",
    246:"IT3TopX1Sector2",
    247:"IT3TopX1Sector3",
    248:"IT3TopX1Sector4",
    249:"IT3TopX1Sector5",
    250:"IT3TopX1Sector6",
    251:"IT3TopX1Sector7",
    196:"IT2CSideX2Sector1",
    197:"IT2CSideX2Sector2",
    198:"IT2CSideX2Sector3",
    199:"IT2CSideX2Sector4",
    200:"IT2CSideX2Sector5",
    201:"IT2CSideX2Sector6",
    202:"IT2CSideX2Sector7",
    168:"IT2CSideVSector1",
    169:"IT2CSideVSector2",
    170:"IT2CSideVSector3",
    171:"IT2CSideVSector4",
    172:"IT2CSideVSector5",
    173:"IT2CSideVSector6",
    174:"IT2CSideVSector7",
    140:"IT2CSideUSector1",
    141:"IT2CSideUSector2",
    142:"IT2CSideUSector3",
    143:"IT2CSideUSector4",
    144:"IT2CSideUSector5",
    145:"IT2CSideUSector6",
    146:"IT2CSideUSector7",
    112:"IT2CSideX1Sector1",
    113:"IT2CSideX1Sector2",
    114:"IT2CSideX1Sector3",
    115:"IT2CSideX1Sector4",
    116:"IT2CSideX1Sector5",
    117:"IT2CSideX1Sector6",
    118:"IT2CSideX1Sector7",
    203:"IT2ASideX2Sector1",
    204:"IT2ASideX2Sector2",
    205:"IT2ASideX2Sector3",
    206:"IT2ASideX2Sector4",
    207:"IT2ASideX2Sector5",
    208:"IT2ASideX2Sector6",
    209:"IT2ASideX2Sector7",
    175:"IT2ASideVSector1",
    176:"IT2ASideVSector2",
    177:"IT2ASideVSector3",
    178:"IT2ASideVSector4",
    179:"IT2ASideVSector5",
    180:"IT2ASideVSector6",
    181:"IT2ASideVSector7",
    147:"IT2ASideUSector1",
    148:"IT2ASideUSector2",
    149:"IT2ASideUSector3",
    150:"IT2ASideUSector4",
    151:"IT2ASideUSector5",
    152:"IT2ASideUSector6",
    153:"IT2ASideUSector7",
    119:"IT2ASideX1Sector1",
    120:"IT2ASideX1Sector2",
    121:"IT2ASideX1Sector3",
    122:"IT2ASideX1Sector4",
    123:"IT2ASideX1Sector5",
    124:"IT2ASideX1Sector6",
    125:"IT2ASideX1Sector7",
    210:"IT2BottomX2Sector1",
    211:"IT2BottomX2Sector2",
    212:"IT2BottomX2Sector3",
    213:"IT2BottomX2Sector4",
    214:"IT2BottomX2Sector5",
    215:"IT2BottomX2Sector6",
    216:"IT2BottomX2Sector7",
    182:"IT2BottomVSector1",
    183:"IT2BottomVSector2",
    184:"IT2BottomVSector3",
    185:"IT2BottomVSector4",
    186:"IT2BottomVSector5",
    187:"IT2BottomVSector6",
    188:"IT2BottomVSector7",
    154:"IT2BottomUSector1",
    155:"IT2BottomUSector2",
    156:"IT2BottomUSector3",
    157:"IT2BottomUSector4",
    158:"IT2BottomUSector5",
    159:"IT2BottomUSector6",
    160:"IT2BottomUSector7",
    126:"IT2BottomX1Sector1",
    127:"IT2BottomX1Sector2",
    128:"IT2BottomX1Sector3",
    129:"IT2BottomX1Sector4",
    130:"IT2BottomX1Sector5",
    131:"IT2BottomX1Sector6",
    132:"IT2BottomX1Sector7",
    217:"IT2TopX2Sector1",
    218:"IT2TopX2Sector2",
    219:"IT2TopX2Sector3",
    220:"IT2TopX2Sector4",
    221:"IT2TopX2Sector5",
    222:"IT2TopX2Sector6",
    223:"IT2TopX2Sector7",
    189:"IT2TopVSector1",
    190:"IT2TopVSector2",
    191:"IT2TopVSector3",
    192:"IT2TopVSector4",
    193:"IT2TopVSector5",
    194:"IT2TopVSector6",
    195:"IT2TopVSector7",
    161:"IT2TopUSector1",
    162:"IT2TopUSector2",
    163:"IT2TopUSector3",
    164:"IT2TopUSector4",
    165:"IT2TopUSector5",
    166:"IT2TopUSector6",
    167:"IT2TopUSector7",
    133:"IT2TopX1Sector1",
    134:"IT2TopX1Sector2",
    135:"IT2TopX1Sector3",
    136:"IT2TopX1Sector4",
    137:"IT2TopX1Sector5",
    138:"IT2TopX1Sector6",
    139:"IT2TopX1Sector7",
    84:"IT1CSideX2Sector1",
    85:"IT1CSideX2Sector2",
    86:"IT1CSideX2Sector3",
    87:"IT1CSideX2Sector4",
    88:"IT1CSideX2Sector5",
    89:"IT1CSideX2Sector6",
    90:"IT1CSideX2Sector7",
    56:"IT1CSideVSector1",
    57:"IT1CSideVSector2",
    58:"IT1CSideVSector3",
    59:"IT1CSideVSector4",
    60:"IT1CSideVSector5",
    61:"IT1CSideVSector6",
    62:"IT1CSideVSector7",
    28:"IT1CSideUSector1",
    29:"IT1CSideUSector2",
    30:"IT1CSideUSector3",
    31:"IT1CSideUSector4",
    32:"IT1CSideUSector5",
    33:"IT1CSideUSector6",
    34:"IT1CSideUSector7",
    0:"IT1CSideX1Sector1",
    1:"IT1CSideX1Sector2",
    2:"IT1CSideX1Sector3",
    3:"IT1CSideX1Sector4",
    4:"IT1CSideX1Sector5",
    5:"IT1CSideX1Sector6",
    6:"IT1CSideX1Sector7",
    91:"IT1ASideX2Sector1",
    92:"IT1ASideX2Sector2",
    93:"IT1ASideX2Sector3",
    94:"IT1ASideX2Sector4",
    95:"IT1ASideX2Sector5",
    96:"IT1ASideX2Sector6",
    97:"IT1ASideX2Sector7",
    63:"IT1ASideVSector1",
    64:"IT1ASideVSector2",
    65:"IT1ASideVSector3",
    66:"IT1ASideVSector4",
    67:"IT1ASideVSector5",
    68:"IT1ASideVSector6",
    69:"IT1ASideVSector7",
    35:"IT1ASideUSector1",
    36:"IT1ASideUSector2",
    37:"IT1ASideUSector3",
    38:"IT1ASideUSector4",
    39:"IT1ASideUSector5",
    40:"IT1ASideUSector6",
    41:"IT1ASideUSector7",
    7:"IT1ASideX1Sector1",
    8:"IT1ASideX1Sector2",
    9:"IT1ASideX1Sector3",
    10:"IT1ASideX1Sector4",
    11:"IT1ASideX1Sector5",
    12:"IT1ASideX1Sector6",
    13:"IT1ASideX1Sector7",
    98:"IT1BottomX2Sector1",
    99:"IT1BottomX2Sector2",
    100:"IT1BottomX2Sector3",
    101:"IT1BottomX2Sector4",
    102:"IT1BottomX2Sector5",
    103:"IT1BottomX2Sector6",
    104:"IT1BottomX2Sector7",
    70:"IT1BottomVSector1",
    71:"IT1BottomVSector2",
    72:"IT1BottomVSector3",
    73:"IT1BottomVSector4",
    74:"IT1BottomVSector5",
    75:"IT1BottomVSector6",
    76:"IT1BottomVSector7",
    42:"IT1BottomUSector1",
    43:"IT1BottomUSector2",
    44:"IT1BottomUSector3",
    45:"IT1BottomUSector4",
    46:"IT1BottomUSector5",
    47:"IT1BottomUSector6",
    48:"IT1BottomUSector7",
    14:"IT1BottomX1Sector1",
    15:"IT1BottomX1Sector2",
    16:"IT1BottomX1Sector3",
    17:"IT1BottomX1Sector4",
    18:"IT1BottomX1Sector5",
    19:"IT1BottomX1Sector6",
    20:"IT1BottomX1Sector7",
    105:"IT1TopX2Sector1",
    106:"IT1TopX2Sector2",
    107:"IT1TopX2Sector3",
    108:"IT1TopX2Sector4",
    109:"IT1TopX2Sector5",
    110:"IT1TopX2Sector6",
    111:"IT1TopX2Sector7",
    77:"IT1TopVSector1",
    78:"IT1TopVSector2",
    79:"IT1TopVSector3",
    80:"IT1TopVSector4",
    81:"IT1TopVSector5",
    82:"IT1TopVSector6",
    83:"IT1TopVSector7",
    49:"IT1TopUSector1",
    50:"IT1TopUSector2",
    51:"IT1TopUSector3",
    52:"IT1TopUSector4",
    53:"IT1TopUSector5",
    54:"IT1TopUSector6",
    55:"IT1TopUSector7",
    21:"IT1TopX1Sector1",
    22:"IT1TopX1Sector2",
    23:"IT1TopX1Sector3",
    24:"IT1TopX1Sector4",
    25:"IT1TopX1Sector5",
    26:"IT1TopX1Sector6",
    27:"IT1TopX1Sector7"
    }
    return IT_Map
    
def TT_Map():
    TT_Map = {
    159 : "TTbVRegionCSector4", 
    158 : "TTbVRegionCSector3",
    156 : "TTbVRegionCSector1",
    157 : "TTbVRegionCSector2",
    163 : "TTbVRegionCSector8",
    162 : "TTbVRegionCSector7",
    160 : "TTbVRegionCSector5",
    161 : "TTbVRegionCSector6",
    167 : "TTbVRegionCSector12",
    166 : "TTbVRegionCSector11",
    164 : "TTbVRegionCSector9",
    165 : "TTbVRegionCSector10",
    171 : "TTbVRegionCSector16",
    170 : "TTbVRegionCSector15",
    168 : "TTbVRegionCSector13",
    169 : "TTbVRegionCSector14",
    175 : "TTbVRegionCSector20",
    174 : "TTbVRegionCSector19",
    172 : "TTbVRegionCSector17",
    173 : "TTbVRegionCSector18",
    179 : "TTbVRegionCSector24",
    178 : "TTbVRegionCSector23",
    176 : "TTbVRegionCSector21",
    177 : "TTbVRegionCSector22",
    191 : "TTbVRegionBSector10",
    190 : "TTbVRegionBSector9",
    189 : "TTbVRegionBSector8",
    186 : "TTbVRegionBSector5",
    187 : "TTbVRegionBSector6",
    188 : "TTbVRegionBSector7",
    197 : "TTbVRegionBSector16",
    196 : "TTbVRegionBSector15",
    195 : "TTbVRegionBSector14",
    192 : "TTbVRegionBSector11",
    193 : "TTbVRegionBSector12",
    194 : "TTbVRegionBSector13",
    203 : "TTbVRegionBSector22",
    202 : "TTbVRegionBSector21",
    201 : "TTbVRegionBSector20",
    198 : "TTbVRegionBSector17",
    199 : "TTbVRegionBSector18",
    200 : "TTbVRegionBSector19",
    185 : "TTbVRegionBSector4",
    184 : "TTbVRegionBSector3",
    182 : "TTbVRegionBSector1",
    183 : "TTbVRegionBSector2",
    207 : "TTbVRegionBSector26",
    206 : "TTbVRegionBSector25",
    204 : "TTbVRegionBSector23",
    205 : "TTbVRegionBSector24",
    211 : "TTbVRegionASector4",
    210 : "TTbVRegionASector3",
    208 : "TTbVRegionASector1",
    209 : "TTbVRegionASector2",
    215 : "TTbVRegionASector8",
    214 : "TTbVRegionASector7",
    212 : "TTbVRegionASector5",
    213 : "TTbVRegionASector6",
    219 : "TTbVRegionASector12",
    218 : "TTbVRegionASector11",
    216 : "TTbVRegionASector9",
    217 : "TTbVRegionASector10",
    223 : "TTbVRegionASector16",
    222 : "TTbVRegionASector15",
    220 : "TTbVRegionASector13",
    221 : "TTbVRegionASector14",
    227 : "TTbVRegionASector20",
    226 : "TTbVRegionASector19",
    224 : "TTbVRegionASector17",
    225 : "TTbVRegionASector18",
    231 : "TTbVRegionASector24",
    230 : "TTbVRegionASector23",
    228 : "TTbVRegionASector21",
    229 : "TTbVRegionASector22",
    237 : "TTbXRegionCSector4",
    236 : "TTbXRegionCSector3",
    234 : "TTbXRegionCSector1",
    235 : "TTbXRegionCSector2",
    241 : "TTbXRegionCSector8",
    240 : "TTbXRegionCSector7",
    238 : "TTbXRegionCSector5",
    239 : "TTbXRegionCSector6",
    245 : "TTbXRegionCSector12",
    244 : "TTbXRegionCSector11",
    242 : "TTbXRegionCSector9",
    243 : "TTbXRegionCSector10",
    249 : "TTbXRegionCSector16",
    248 : "TTbXRegionCSector15",
    246 : "TTbXRegionCSector13",
    247 : "TTbXRegionCSector14",
    253 : "TTbXRegionCSector20",
    252 : "TTbXRegionCSector19",
    250 : "TTbXRegionCSector17",
    251 : "TTbXRegionCSector18",
    257 : "TTbXRegionCSector24",
    256 : "TTbXRegionCSector23",
    254 : "TTbXRegionCSector21",
    255 : "TTbXRegionCSector22",
    269 : "TTbXRegionBSector10",
    268 : "TTbXRegionBSector9",
    267 : "TTbXRegionBSector8",
    264 : "TTbXRegionBSector5",
    265 : "TTbXRegionBSector6",
    266 : "TTbXRegionBSector7",
    275 : "TTbXRegionBSector16",
    274 : "TTbXRegionBSector15",
    273 : "TTbXRegionBSector14",
    270 : "TTbXRegionBSector11",
    271 : "TTbXRegionBSector12",
    272 : "TTbXRegionBSector13",
    281 : "TTbXRegionBSector22",
    280 : "TTbXRegionBSector21",
    279 : "TTbXRegionBSector20",
    276 : "TTbXRegionBSector17",
    277 : "TTbXRegionBSector18",
    278 : "TTbXRegionBSector19",
    263 : "TTbXRegionBSector4",
    262 : "TTbXRegionBSector3",
    260 : "TTbXRegionBSector1",
    261 : "TTbXRegionBSector2",
    285 : "TTbXRegionBSector26",
    284 : "TTbXRegionBSector25",
    282 : "TTbXRegionBSector23",
    283 : "TTbXRegionBSector24",
    289 : "TTbXRegionASector4",
    288 : "TTbXRegionASector3",
    286 : "TTbXRegionASector1",
    287 : "TTbXRegionASector2",
    293 : "TTbXRegionASector8",
    292 : "TTbXRegionASector7",
    290 : "TTbXRegionASector5",
    291 : "TTbXRegionASector6",
    297 : "TTbXRegionASector12",
    296 : "TTbXRegionASector11",
    294 : "TTbXRegionASector9",
    295 : "TTbXRegionASector10",
    301 : "TTbXRegionASector16",
    300 : "TTbXRegionASector15",
    298 : "TTbXRegionASector13",
    299 : "TTbXRegionASector14",
    305 : "TTbXRegionASector20",
    304 : "TTbXRegionASector19",
    302 : "TTbXRegionASector17",
    303 : "TTbXRegionASector18",
    309 : "TTbXRegionASector24",
    308 : "TTbXRegionASector23",
    306 : "TTbXRegionASector21",
    307 : "TTbXRegionASector22",
    81 : "TTaURegionCSector4",
    80 : "TTaURegionCSector3",
    78 : "TTaURegionCSector1",
    79 : "TTaURegionCSector2",
    85 : "TTaURegionCSector8",
    84 : "TTaURegionCSector7",
    82 : "TTaURegionCSector5",
    83 : "TTaURegionCSector6",
    89 : "TTaURegionCSector12",
    88 : "TTaURegionCSector11",
    86 : "TTaURegionCSector9",
    87 : "TTaURegionCSector10",
    93 : "TTaURegionCSector16",
    92 : "TTaURegionCSector15",
    90 : "TTaURegionCSector13",
    91 : "TTaURegionCSector14",
    97 : "TTaURegionCSector20",
    96 : "TTaURegionCSector19",
    94 : "TTaURegionCSector17",
    95 : "TTaURegionCSector18",
    101 : "TTaURegionCSector24",
    100 : "TTaURegionCSector23",
    98 : "TTaURegionCSector21",
    99 : "TTaURegionCSector22",
    109 : "TTaURegionBSector6",
    108 : "TTaURegionBSector5",
    107 : "TTaURegionBSector4",
    104 : "TTaURegionBSector1",
    105 : "TTaURegionBSector2",
    106 : "TTaURegionBSector3",
    115 : "TTaURegionBSector12",
    114 : "TTaURegionBSector11",
    113 : "TTaURegionBSector10",
    110 : "TTaURegionBSector7",
    111 : "TTaURegionBSector8",
    112 : "TTaURegionBSector9",
    121 : "TTaURegionBSector18",
    120 : "TTaURegionBSector17",
    119 : "TTaURegionBSector16",
    116 : "TTaURegionBSector13",
    117 : "TTaURegionBSector14",
    118 : "TTaURegionBSector15",
    133 : "TTaURegionASector4",
    132 : "TTaURegionASector3",
    130 : "TTaURegionASector1",
    131 : "TTaURegionASector2",
    137 : "TTaURegionASector8",
    136 : "TTaURegionASector7",
    134 : "TTaURegionASector5",
    135 : "TTaURegionASector6",
    141 : "TTaURegionASector12",
    140 : "TTaURegionASector11",
    138 : "TTaURegionASector9",
    139 : "TTaURegionASector10",
    145 : "TTaURegionASector16",
    144 : "TTaURegionASector15",
    142 : "TTaURegionASector13",
    143 : "TTaURegionASector14",
    149 : "TTaURegionASector20",
    148 : "TTaURegionASector19",
    146 : "TTaURegionASector17",
    147 : "TTaURegionASector18",
    153 : "TTaURegionASector24",
    152 : "TTaURegionASector23",
    150 : "TTaURegionASector21",
    151 : "TTaURegionASector22",
    3 : "TTaXRegionCSector4",
    2 : "TTaXRegionCSector3",
    0 : "TTaXRegionCSector1",
    1 : "TTaXRegionCSector2",
    7 : "TTaXRegionCSector8",
    6 : "TTaXRegionCSector7",
    4 : "TTaXRegionCSector5",
    5 : "TTaXRegionCSector6",
    11 : "TTaXRegionCSector12",
    10 : "TTaXRegionCSector11",
    8 : "TTaXRegionCSector9",
    9 : "TTaXRegionCSector10",
    15 : "TTaXRegionCSector16",
    14 : "TTaXRegionCSector15",
    12 : "TTaXRegionCSector13",
    13 : "TTaXRegionCSector14",
    19 : "TTaXRegionCSector20",
    18 : "TTaXRegionCSector19",
    16 : "TTaXRegionCSector17",
    17 : "TTaXRegionCSector18",
    23 : "TTaXRegionCSector24",
    22 : "TTaXRegionCSector23",
    20 : "TTaXRegionCSector21",
    21 : "TTaXRegionCSector22",
    31 : "TTaXRegionBSector6",
    30 : "TTaXRegionBSector5",
    29 : "TTaXRegionBSector4",
    26 : "TTaXRegionBSector1",
    27 : "TTaXRegionBSector2",
    28 : "TTaXRegionBSector3",
    37 : "TTaXRegionBSector12",
    36 : "TTaXRegionBSector11",
    35 : "TTaXRegionBSector10",
    32 : "TTaXRegionBSector7",
    33 : "TTaXRegionBSector8",
    34 : "TTaXRegionBSector9",
    43 : "TTaXRegionBSector18",
    42 : "TTaXRegionBSector17",
    41 : "TTaXRegionBSector16",
    38 : "TTaXRegionBSector13",
    39 : "TTaXRegionBSector14",
    40 : "TTaXRegionBSector15",
    55 : "TTaXRegionASector4",
    54 : "TTaXRegionASector3",
    52 : "TTaXRegionASector1",
    53 : "TTaXRegionASector2",
    59 : "TTaXRegionASector8",
    58 : "TTaXRegionASector7",
    56 : "TTaXRegionASector5",
    57 : "TTaXRegionASector6",
    63 : "TTaXRegionASector12",
    62 : "TTaXRegionASector11",
    60 : "TTaXRegionASector9",
    61 : "TTaXRegionASector10",
    67 : "TTaXRegionASector16",
    66 : "TTaXRegionASector15",
    64 : "TTaXRegionASector13",
    65 : "TTaXRegionASector14",
    71 : "TTaXRegionASector20",
    70 : "TTaXRegionASector19",
    68 : "TTaXRegionASector17",
    69 : "TTaXRegionASector18",
    75 : "TTaXRegionASector24",
    74 : "TTaXRegionASector23",
    72 : "TTaXRegionASector21",
    73 : "TTaXRegionASector22"
    }
    return TT_Map

def IT_ids_Map():
    #internal bin numeber : uniqueSectorID
    IT_ids_Map = {
    308    :7201,
    309    :7202,
    310    :7203,
    311    :7204,
    312    :7205,
    313    :7206,
    314    :7207,
    280    :6945,
    281    :6946,
    282    :6947,
    283    :6948,
    284    :6949,
    285    :6950,
    286    :6951,
    252    :6689,
    253    :6690,
    254    :6691,
    255    :6692,
    256    :6693,
    257    :6694,
    258    :6695,
    224    :6433,
    225    :6434,
    226    :6435,
    227    :6436,
    228    :6437,
    229    :6438,
    230    :6439,
    315    :7233,
    316    :7234,
    317    :7235,
    318    :7236,
    319    :7237,
    320    :7238,
    321    :7239,
    287    :6977,
    288    :6978,
    289    :6979,
    290    :6980,
    291    :6981,
    292    :6982,
    293    :6983,
    259    :6721,
    260    :6722,
    261    :6723,
    262    :6724,
    263    :6725,
    264    :6726,
    265    :6727,
    231    :6465,
    232    :6466,
    233    :6467,
    234    :6468,
    235    :6469,
    236    :6470,
    237    :6471,
    322    :7265,
    323    :7266,
    324    :7267,
    325    :7268,
    326    :7269,
    327    :7270,
    328    :7271,
    294    :7009,
    295    :7010,
    296    :7011,
    297    :7012,
    298    :7013,
    299    :7014,
    300    :7015,
    266    :6753,
    267    :6754,
    268    :6755,
    269    :6756,
    270    :6757,
    271    :6758,
    272    :6759,
    238    :6497,
    239    :6498,
    240    :6499,
    241    :6500,
    242    :6501,
    243    :6502,
    244    :6503,
    329    :7297,
    330    :7298,
    331    :7299,
    332    :7300,
    333    :7301,
    334    :7302,
    335    :7303,
    301    :7041,
    302    :7042,
    303    :7043,
    304    :7044,
    305    :7045,
    306    :7046,
    307    :7047,
    273    :6785,
    274    :6786,
    275    :6787,
    276    :6788,
    277    :6789,
    278    :6790,
    279    :6791,
    245    :6529,
    246    :6530,
    247    :6531,
    248    :6532,
    249    :6533,
    250    :6534,
    251    :6535,
    196    :5153,
    197    :5154,
    198    :5155,
    199    :5156,
    200    :5157,
    201    :5158,
    202    :5159,
    168    :4897,
    169    :4898,
    170    :4899,
    171    :4900,
    172    :4901,
    173    :4902,
    174    :4903,
    140    :4641,
    141    :4642,
    142    :4643,
    143    :4644,
    144    :4645,
    145    :4646,
    146    :4647,
    112    :4385,
    113    :4386,
    114    :4387,
    115    :4388,
    116    :4389,
    117    :4390,
    118    :4391,
    203    :5185,
    204    :5186,
    205    :5187,
    206    :5188,
    207    :5189,
    208    :5190,
    209    :5191,
    175    :4929,
    176    :4930,
    177    :4931,
    178    :4932,
    179    :4933,
    180    :4934,
    181    :4935,
    147    :4673,
    148    :4674,
    149    :4675,
    150    :4676,
    151    :4677,
    152    :4678,
    153    :4679,
    119    :4417,
    120    :4418,
    121    :4419,
    122    :4420,
    123    :4421,
    124    :4422,
    125    :4423,
    210    :5217,
    211    :5218,
    212    :5219,
    213    :5220,
    214    :5221,
    215    :5222,
    216    :5223,
    182    :4961,
    183    :4962,
    184    :4963,
    185    :4964,
    186    :4965,
    187    :4966,
    188    :4967,
    154    :4705,
    155    :4706,
    156    :4707,
    157    :4708,
    158    :4709,
    159    :4710,
    160    :4711,
    126    :4449,
    127    :4450,
    128    :4451,
    129    :4452,
    130    :4453,
    131    :4454,
    132    :4455,
    217    :5249,
    218    :5250,
    219    :5251,
    220    :5252,
    221    :5253,
    222    :5254,
    223    :5255,
    189    :4993,
    190    :4994,
    191    :4995,
    192    :4996,
    193    :4997,
    194    :4998,
    195    :4999,
    161    :4737,
    162    :4738,
    163    :4739,
    164    :4740,
    165    :4741,
    166    :4742,
    167    :4743,
    133    :4481,
    134    :4482,
    135    :4483,
    136    :4484,
    137    :4485,
    138    :4486,
    139    :4487,
    84 :3105,
    85 :3106,
    86 :3107,
    87 :3108,
    88 :3109,
    89 :3110,
    90 :3111,
    56 :2849,
    57 :2850,
    58 :2851,
    59 :2852,
    60 :2853,
    61 :2854,
    62 :2855,
    28 :2593,
    29 :2594,
    30 :2595,
    31 :2596,
    32 :2597,
    33 :2598,
    34 :2599,
    0  :2337,
    1  :2338,
    2  :2339,
    3  :2340,
    4  :2341,
    5  :2342,
    6  :2343,
    91 :3137,
    92 :3138,
    93 :3139,
    94 :3140,
    95 :3141,
    96 :3142,
    97 :3143,
    63 :2881,
    64 :2882,
    65 :2883,
    66 :2884,
    67 :2885,
    68 :2886,
    69 :2887,
    35 :2625,
    36 :2626,
    37 :2627,
    38 :2628,
    39 :2629,
    40 :2630,
    41 :2631,
    7  :2369,
    8  :2370,
    9  :2371,
    10 :2372,
    11 :2373,
    12 :2374,
    13 :2375,
    98 :3169,
    99 :3170,
    100    :3171,
    101    :3172,
    102    :3173,
    103    :3174,
    104    :3175,
    70 :2913,
    71 :2914,
    72 :2915,
    73 :2916,
    74 :2917,
    75 :2918,
    76 :2919,
    42 :2657,
    43 :2658,
    44 :2659,
    45 :2660,
    46 :2661,
    47 :2662,
    48 :2663,
    14 :2401,
    15 :2402,
    16 :2403,
    17 :2404,
    18 :2405,
    19 :2406,
    20 :2407,
    105    :3201,
    106    :3202,
    107    :3203,
    108    :3204,
    109    :3205,
    110    :3206,
    111    :3207,
    77 :2945,
    78 :2946,
    79 :2947,
    80 :2948,
    81 :2949,
    82 :2950,
    83 :2951,
    49 :2689,
    50 :2690,
    51 :2691,
    52 :2692,
    53 :2693,
    54 :2694,
    55 :2695,
    21 :2433,
    22 :2434,
    23 :2435,
    24 :2436,
    25 :2437,
    26 :2438,
    27 :2439,
    }
    return IT_ids_Map

def TT_ids_Map():
    TT_ids_Map={
    159 :4388,
    158 :4387,
    156 :4385,
    157 :4386,
    163 :4392,
    162 :4391,
    160 :4389,
    161 :4390,
    167 :4396,
    166 :4395,
    164 :4393,
    165 :4394,
    171 :4400,
    170 :4399,
    168 :4397,
    169 :4398,
    175 :4404,
    174 :4403,
    172 :4401,
    173 :4402,
    179 :4408,
    178 :4407,
    176 :4405,
    177 :4406,
    191 :4426,
    190 :4425,
    189 :4424,
    186 :4421,
    187 :4422,
    188 :4423,
    197 :4432,
    196 :4431,
    195 :4430,
    192 :4427,
    193 :4428,
    194 :4429,
    203 :4438,
    202 :4437,
    201 :4436,
    198 :4433,
    199 :4434,
    200 :4435,
    185 :4420,
    184 :4419,
    182 :4417,
    183 :4418,
    207 :4442,
    206 :4441,
    204 :4439,
    205 :4440,
    211 :4452,
    210 :4451,
    208 :4449,
    209 :4450,
    215 :4456,
    214 :4455,
    212 :4453,
    213 :4454,
    219 :4460,
    218 :4459,
    216 :4457,
    217 :4458,
    223 :4464,
    222 :4463,
    220 :4461,
    221 :4462,
    227 :4468,
    226 :4467,
    224 :4465,
    225 :4466,
    231 :4472,
    230 :4471,
    228 :4469,
    229 :4470,
    237 :4644,
    236 :4643,
    234 :4641,
    235 :4642,
    241 :4648,
    240 :4647,
    238 :4645,
    239 :4646,
    245 :4652,
    244 :4651,
    242 :4649,
    243 :4650,
    249 :4656,
    248 :4655,
    246 :4653,
    247 :4654,
    253 :4660,
    252 :4659,
    250 :4657,
    251 :4658,
    257 :4664,
    256 :4663,
    254 :4661,
    255 :4662,
    269 :4682,
    268 :4681,
    267 :4680,
    264 :4677,
    265 :4678,
    266 :4679,
    275 :4688,
    274 :4687,
    273 :4686,
    270 :4683,
    271 :4684,
    272 :4685,
    281 :4694,
    280 :4693,
    279 :4692,
    276 :4689,
    277 :4690,
    278 :4691,
    263 :4676,
    262 :4675,
    260 :4673,
    261 :4674,
    285 :4698,
    284 :4697,
    282 :4695,
    283 :4696,
    289 :4708,
    288 :4707,
    286 :4705,
    287 :4706,
    293 :4712,
    292 :4711,
    290 :4709,
    291 :4710,
    297 :4716,
    296 :4715,
    294 :4713,
    295 :4714,
    301 :4720,
    300 :4719,
    298 :4717,
    299 :4718,
    305 :4724,
    304 :4723,
    302 :4721,
    303 :4722,
    309 :4728,
    308 :4727,
    306 :4725,
    307 :4726,
    81 :2596,
    80 :2595,
    78 :2593,
    79 :2594,
    85 :2600,
    84 :2599,
    82 :2597,
    83 :2598,
    89 :2604,
    88 :2603,
    86 :2601,
    87 :2602,
    93 :2608,
    92 :2607,
    90 :2605,
    91 :2606,
    97 :2612,
    96 :2611,
    94 :2609,
    95 :2610,
    101 :2616,
    100 :2615,
    98 :2613,
    99 :2614,
    109 :2630,
    108 :2629,
    107 :2628,
    104 :2625,
    105 :2626,
    106 :2627,
    115 :2636,
    114 :2635,
    113 :2634,
    110 :2631,
    111 :2632,
    112 :2633,
    121 :2642,
    120 :2641,
    119 :2640,
    116 :2637,
    117 :2638,
    118 :2639,
    133 :2660,
    132 :2659,
    130 :2657,
    131 :2658,
    137 :2664,
    136 :2663,
    134 :2661,
    135 :2662,
    141 :2668,
    140 :2667,
    138 :2665,
    139 :2666,
    145 :2672,
    144 :2671,
    142 :2669,
    143 :2670,
    149 :2676,
    148 :2675,
    146 :2673,
    147 :2674,
    153 :2680,
    152 :2679,
    150 :2677,
    151 :2678,
    3 :2340,
    2 :2339,
    0 :2337,
    1 :2338,
    7 :2344,
    6 :2343,
    4 :2341,
    5 :2342,
    11 :2348,
    10 :2347,
    8 :2345,
    9 :2346,
    15 :2352,
    14 :2351,
    12 :2349,
    13 :2350,
    19 :2356,
    18 :2355,
    16 :2353,
    17 :2354,
    23 :2360,
    22 :2359,
    20 :2357,
    21 :2358,
    31 :2374,
    30 :2373,
    29 :2372,
    26 :2369,
    27 :2370,
    28 :2371,
    37 :2380,
    36 :2379,
    35 :2378,
    32 :2375,
    33 :2376,
    34 :2377,
    43 :2386,
    42 :2385,
    41 :2384,
    38 :2381,
    39 :2382,
    40 :2383,
    55 :2404,
    54 :2403,
    52 :2401,
    53 :2402,
    59 :2408,
    58 :2407,
    56 :2405,
    57 :2406,
    63 :2412,
    62 :2411,
    60 :2409,
    61 :2410,
    67 :2416,
    66 :2415,
    64 :2413,
    65 :2414,
    71 :2420,
    70 :2419,
    68 :2417,
    69 :2418,
    75 :2424,
    74 :2423,
    72 :2421,
    73 :2422,
    }
    return TT_ids_Map

if __name__ == "__main__":
    with open('IT_Map.pkl', 'wb') as basket:
        pickle.dump(IT_Map(), basket)
    with open('TT_Map.pkl', 'wb') as basket:
        pickle.dump(TT_Map(), basket)
