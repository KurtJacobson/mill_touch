def gcode_titles():

    titles = {'G0':'Coordinated Motion at Rapid Rate',
        'G1':'Coordinated Motion at Feed Rate',
        'G2':'Coordinated Clockwise Helical Motion at Feed Rate',
        'G3':'Coordinated Counterclockwise Helical Motion at Feed Rate',
        'G4':'Dwell',
        'G5':'Cubic Spline',
        'G5.1':'Quadratic B-Spline',
        'G5.2':'NURBS, add control point',
        'G7':'Diameter Mode (lathe)',
        'G8':'Radius Mode (lathe)',
        'G10L1':'Set Tool Table Entry',
        'G10L2':'Set Tool Table, Calculated, Workpiece',
        'G10L10':'Set Tool Table, Calculated, Fixture',
        'G10L11':'Coordinate System Origin Setting',
        'G10L20':'Coordinate System Origin Setting Calculated',
        'G17':'Plane Select XY',
        'G18':'Plane Select XZ',
        'G19':'Plane Select YZ',
        'G17.1':'Plane Select UV',
        'G17.2':'Plane Select WU',
        'G17.3':'Plane Select VW',
        'G20':'Set Units to Inch',
        'G21':'Set Units to Millimeters',
        'G28':'Go to Predefined Position',
        'G28.1':'Set Predefined Position',
        'G30':'Go to Predefined Position',
        'G30.1':'Set Predefined Position',
        'G33':'Spindle Synchronized Motion',
        'G33.1':'Rigid Tapping',
        'G38.2':'Probing Toward Workpiece, Signal Error',
        'G38.3':'Probing Toward Workpiece',
        'G38.4':'Probing Away Workpiece, Signal Error',
        'G38.5':'Probing Away Workpiece',
        'G40':'Cancel Cutter Compensation',
        'G41':'Cutter Compensation, Left of Programmed Path',
        'G41.1':'Dynamic Cutter Compensation, Left of Programmed Path',
        'G42':'Cutter Compensation, Right of Programmed Path',
        'G42.1':'Dynamic Cutter Compensation, Right of Programmed Path',
        'G43':'Use Tool Length Offset from Tool Table',
        'G43.1':'Dynamic Tool Length Offset',
        'G43.2':'Apply additional Tool Length Offset',
        'G49':'Cancel Tool Length Offset',
        'G52':'Local Coordinate System Offset',
        'G53':'Move in Machine Coordinates',
        'G54':'Select Coordinate System 1',
        'G55':'Select Coordinate System 2',
        'G56':'Select Coordinate System 3',
        'G57':'Select Coordinate System 4',
        'G58':'Select Coordinate System 5',
        'G59':'Select Coordinate System 6',
        'G59.1':'Select Coordinate System 7',
        'G59.2':'Select Coordinate System 8',
        'G59.3':'Select Coordinate System 9',
        'G61':'Exact Path Mode',
        'G61.1':'Exact Stop Mode',
        'G64':'Path Control Mode with Tolerance',
        'G73':'Drilling Cycle with Chip Breaking',
        'G74':'Left-hand Tapping Cycle with Dwell',
        'G76':'Multi-pass Threading Cycle (Lathe)',
        'G80':'Cancel Motion Modes',
        'G81':'Drilling Cycle',
        'G82':'Drilling Cycle with Dwell',
        'G83':'Drilling Cycle with Peck',
        'G84':'Right-hand Tapping Cycle with Dwell',
        'G85':'Boring Cycle, No Dwell, Feed Out',
        'G86':'Boring Cycle, Stop, Rapid Out',
        'G89':'Boring Cycle, Dwell, Feed Out',
        'G90':'Absolute Distance Mode',
        'G90.1':'Absolute Distance Mode IJK Arc Offsets',
        'G91':'Incremental Distance Mode',
        'G91.1':'Incremental Distance Mode IJK Arc Offsets',
        'G92':'Coordinate System Offset',
        'G92.1':'Reset G92 Offsets, Reset Parameters',
        'G92.2':'Reset G92 Offsets, Keep Parameters ',
        'G92.3':'Restore G92 Offsets',
        'G93':'Feed Rate Inverse Time Mode',
        'G94':'Feed Rate Units per Minute Mode',
        'G95':'Feed Rate Units per Revolution Mode',
        'G96':'Spindle Control Constant Surface Speed Mode',
        'G97':'Spindle Control RPM Mode',
        'G98':'Canned Cycle Return Level',
        'G99':'Canned Cycle Return Level',}

    return titles


def gcode_words():

    words = {'G0':['X', 'Y', 'Z'],
        'G1':['X', 'Y', 'Z'],
        'G2':['X', 'Y', 'Z', 'I', 'J', 'K', 'R', 'P'],
        'G3':['X', 'Y', 'Z', 'I', 'J', 'K', 'R', 'P'],
        'G4':['P'],
        'G5':['I', 'J', 'P', 'Q'],
        'G5.1':['I', 'J'],
        'G5.2':['P', 'L'],
        'G10':['L'],
        'G10L1':['R', 'I', 'J', 'Q'],
        'G10L2':['P', 'X', 'Y', 'Z', 'R'],
        'G10L10':['P', 'R', 'I', 'J', 'Q'],
        'G10L11':['P', 'R', 'I', 'J', 'Q'],
        'G10L20':['P', 'X', 'Y', 'Z'],
        'G33':['X', 'Y', 'Z', 'K', '$'],
        'G33.1':['X', 'Y', 'Z', 'K', '$'],
        'G38.2':['X', 'Y', 'Z'],
        'G38.3':['X', 'Y', 'Z'],
        'G38.4':['X', 'Y', 'Z'],
        'G38.5':['X', 'Y', 'Z'],
        'G41':['D'],
        'G41.1':['D', 'L'],
        'G42':['D'],
        'G42.1':['D', 'L'],
        'G43':['H'],
        'G43.1':['X', 'Y', 'Z'],
        'G43.2':['H'],
        'G52':['X', 'Y', 'Z'],
        'G53':['X', 'Y', 'Z'],
        'G64':['P', 'Q'],
        'G73':['X', 'Y', 'Z', 'R', 'Q', 'L'],
        'G74':['X', 'Y', 'Z', 'R', 'L', 'P', '$'],
        'G76':['P', 'Z', 'I', 'J', 'K', 'Q', 'H', 'E', 'L', '$'],
        'G81':['X', 'Y', 'Z', 'R', 'L'],
        'G82':['X', 'Y', 'Z', 'R', 'L', 'P'],
        'G83':['X', 'Y', 'Z', 'R', 'L', 'Q'],
        'G84':['X', 'Y', 'Z', 'R', 'L', 'P', '$'],
        'G85':['X', 'Y', 'Z', 'R', 'L'],
        'G86':['X', 'Y', 'Z', 'R', 'L', 'P', '$'],
        'G89':['X', 'Y', 'Z', 'R', 'L', 'P'],
        'G92':['X', 'Y', 'Z'],
        'G96':['D', 'S', '$'],
        'G97':['S', '$'],}

    return words

def gcode_descriptions(gcode):

    gcodeTitle = {'G0':G0,
        'G1':G1,
        'G2':G2,
        'G3':G3,
        'G4':G4,
        'G5':G5,
        'G5.1':G5_1,
        'G5.2':'NURBS, add control point',
        'G7':G7,
        'G8':G8,
        'G10L1':G10L1,
        'G10L2':G10L2,
        'G10L10':G10L10,
        'G10L11':G10L11,
        'G10L20':G10L20,
        'G17':'Plane Select XY',
        'G18':'Plane Select XZ',
        'G19':'Plane Select YZ',
        'G17.1':'Plane Select UV',
        'G17.2':'Plane Select WU',
        'G17.3':'Plane Select VW',
        'G20':'Set Units to Inch',
        'G21':'Set Units to Millimeters',
        'G28':'Go to Predefined Position',
        'G28.1':'Set Predefined Position',
        'G30':'Go to Predefined Position',
        'G30.1':'Set Predefined Position',
        'G33':'Spindle Synchronized Motion',
        'G33.1':'Rigid Tapping',
        'G38.2':'Probing Toward Workpiece, Signal Error',
        'G38.3':'Probing Toward Workpiece',
        'G38.4':'Probing Away Workpiece, Signal Error',
        'G38.5':'Probing Away Workpiece',
        'G40':'Cancel Cutter Compensation',
        'G41':'Cutter Compensation, Left of Programmed Path',
        'G41.1':'Dynamic Cutter Compensation, Left of Programmed Path',
        'G42':'Cutter Compensation, Right of Programmed Path',
        'G42.1':'Dynamic Cutter Compensation, Right of Programmed Path',
        'G43':'Use Tool Length Offset from Tool Table',
        'G43.1':'Dynamic Tool Length Offset',
        'G43.2':'Apply additional Tool Length Offset',
        'G49':'Cancel Tool Length Offset',
        'G52':'Local Coordinate System Offset',
        'G53':'Move in Machine Coordinates',
        'G54':'Select Coordinate System 1',
        'G55':'Select Coordinate System 2',
        'G56':'Select Coordinate System 3',
        'G57':'Select Coordinate System 4',
        'G58':'Select Coordinate System 5',
        'G59':'Select Coordinate System 6',
        'G59.1':'Select Coordinate System 7',
        'G59.2':'Select Coordinate System 8',
        'G59.3':'Select Coordinate System 9',
        'G61':'Exact Path Mode',
        'G61.1':'Exact Stop Mode',
        'G64':'Path Control Mode with Tolerance',
        'G73':'Drilling Cycle with Chip Breaking',
        'G74':'Left-hand Tapping Cycle with Dwell',
        'G76':'Multi-pass Threading Cycle (Lathe)',
        'G80':'Cancel Motion Modes',
        'G81':'Drilling Cycle',
        'G82':'Drilling Cycle with Dwell',
        'G83':'Drilling Cycle with Peck',
        'G84':'Right-hand Tapping Cycle with Dwell',
        'G85':'Boring Cycle, No Dwell, Feed Out',
        'G86':'Boring Cycle, Stop, Rapid Out',
        'G89':'Boring Cycle, Dwell, Feed Out',
        'G90':'Absolute Distance Mode',
        'G90.1':'Absolute Distance Mode IJK Arc Offsets',
        'G91':'Incremental Distance Mode',
        'G91.1':'Incremental Distance Mode IJK Arc Offsets',
        'G92':'Coordinate System Offset',
        'G92.1':'Reset G92 Offsets, Reset Parameters',
        'G92.2':'Reset G92 Offsets, Keep Parameters ',
        'G92.3':'Restore G92 Offsets',
        'G93':'Feed Rate Inverse Time Mode',
        'G94':'Feed Rate Units per Minute Mode',
        'G95':'Feed Rate Units per Revolution Mode',
        'G96':'Spindle Control Constant Surface Speed Mode',
        'G97':'Spindle Control RPM Mode',
        'G98':'Canned Cycle Return Level',
        'G99':'Canned Cycle Return Level',}

    print(gcode)
    if gcode in gcodeTitle:
        return gcodeTitle[gcode]
    else:
        return ''

G0 = """G0 axes
Coordinated motion at maximum speed
"""

G1 = """G1 axes
Coordinated motion at feed speed
"""

G2 = """G2 Coordinated Clockwise Helical Motion at Feed Rate
Center Format G2 axes offsets <P>
XY plane (G17)\nZ = helix\nI = X offset\nJ = Y offset\n
XZ plane (G18)\nY = helix\nI = X offset\nK = Z offset\n
YZ plane (G19)\nX = helix\nJ = Y offset\nK = Z offset\n
P = Number of Turns\n
Radius Format G2 axes R <P>
R = Radius from Current Position
"""

G3 = """G3 Coordinated Counterclockwise Helical Motion at Feed Rate
Center Format G3 axes offsets <P>
XY plane (G17)\nZ = helix\nI = X offset\nJ = Y offset\n
XZ plane (G18)\nY = helix\nI = X offset\nK = Z offset\n
YZ plane (G19)\nX = helix\nJ = Y offset\nK = Z offset\n
P = Number of Turns\n
Radius Format G3 axes R <P>
R = Radius from Current Position
"""

G4 = """G4 P
Dwell program for P seconds, floating point.
"""

G5 = """G5 X Y <I J> P Q
Cubic Spline
I = X incremental offset from start point to first control point
J = Y incremental offset from start point to first control point
P = X incremental offset from end point to second control point
Q = Y incremental offset from end point to second control point

G5 creates a cubic B-spline in the XY plane with the X and Y axes only.
P and Q must both be specified for every G5 command.
"""

G5_1 = """G5.1 X Y I J
Quadratic Spline
I - X incremental offset from start point to control point
J - Y incremental offset from start point to control point
G5.1 creates a quadratic B-spline in the XY plane with the X and Y axis only.
Not specifying I or J gives zero offset for the unspecified axis, so one or
both must be given.
"""

G7 = """G7 Lathe Diameter Mode
"""

G8 = """G8 Lathe Radius Mode
"""

G10L1 = """G10 L1 P axes <R I J Q>
Set Tool Table
P = tool number
R = radius of tool
I = front angle (lathe)
J = back angle (lathe)
Q = orientation (lathe)
G10 L1 sets the tool table for the P tool number to the values of the words.
"""

G10L2 = """G10 L2 P <axes R>
P = coordinate system (0-9)
R = rotation about the Z axis
G10 L2 offsets the origin of the axes in the coordinate system specified
to the value of the axis word.
"""

G10L10 = """G10 L10 P axes <R I J Q>
P =- tool number
R = radius of tool
I = front angle (lathe)
J = back angle (lathe)
Q = orientation (lathe)
G10 L10 changes the tool table entry for tool P so that if the tool offset is
reloaded, with the machine in its current position and with the current G5x and
G52/G92 offsets active, the current coordinates for the given axes will become
the given values.
"""

G10L11 = """G10 L11 P axes <R I J Q>
P = tool number
R = radius of tool
I = front angle (lathe)
J = back angle (lathe)
Q = orientation (lathe)
G10 L11 is just like G10 L10 except that instead of setting the entry according
to the current offsets, it is set so that the current coordinates would become
the given value if the new tool offset is reloaded and the machine is placed in
the G59.3 coordinate system without any G52/G92 offset active.
"""

G10L20 = """
"""

G17 = """
"""

G18 = """
"""
