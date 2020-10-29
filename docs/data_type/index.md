# Data Type

## Basic data type

Basic data type used in Jupiter macro/API.

\*All Python data types can be used when using the Python API.

| Jupiter Macro/API data type | Abbreviation | Description                                                                                                                                             |
| --------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Integer                     | `int`        | Represents a positive or negative value with no decimal point.<br>2147483647 means the default value `(blank=no input)` in the integer value field      |
| Boolean                     | `bool`       | Represents the boolean values `False(0)` and `True(1)`                                                                                                  |
| Float                       | `float`      | Represents a computer level double precision floating point number.<br>1.79769e+308 means the default value `(Blank=no input)` in the real number field |
| String                      | `str`        | Represents a string. Enclose with `""`                                                                                                                  |
| Cursor                      | `cursor`     | **TypeID:** Represents an entity in the form of ID.<br>**Example:**<br>`3:1`<br>`[3:1,3:2]`                                                             |

## Item Type

An enumeration that represents the type of item.

The `typeID` variable used primarily in `int` notation.

TypeID is used in the form of `JPT.DItemType.DItemType`.

| Int notation | Item type                             | Description                                                          |
| ------------ | ------------------------------------- | -------------------------------------------------------------------- |
| 3            | `BODY`                                | Parts                                                                |
| 4            | `VERTEX`                              | Vertex                                                               |
| 5            | `EDGE`                                | Edge                                                                 |
| 6            | `FACE`                                | Face                                                                 |
| 7            | `SOLID`                               | Solid shape<br>※Not an element                                       |
| 10           | `NODE`                                | Node                                                                 |
| 11           | `ELEM`                                | Element                                                              |
| 12           | `REF_BODY`                            | Reference parts                                                      |
| 13           | `REF_VERTEX`                          | Reference part composition vertex                                    |
| 14           | `REF_EDGE`                            | Reference part composition edge                                      |
| 15           | `REF_FACE`                            | Reference part composition face                                      |
| 16           | `REF_SOLID`                           | Reference part composition solid                                     |
| 19           | `REF_NODE`                            | Reference part composition node                                      |
| 20           | `REF_ELEM`                            | Reference part component                                             |
| 21           | `LOCAL_SETTING`                       | Local settings                                                       |
| 22           | `MATERIAL`                            | Material                                                             |
| 23           | `ENTITY_ATTR_CAD_INFO`                | CAD attribute information                                            |
| 24           | `FEM_FIELD_SCALAR`                    | For LBC-FIELD (Scalar)                                               |
| 25           | `FEM_FIELD_VECTOR`                    | For LBC-FIELD (Vector)                                               |
| 26           | `FEM_FIELD_TENSOR`                    | For LBC-FIELD (Tensor)                                               |
| 27           | `COORD`                               | Coordinate system                                                    |
| 28           | `LOADCASE`                            | Load case                                                            |
| 29           | `LBC_FORCE`                           | Boundary condition: Force                                            |
| 30           | `LBC_FORCE_ND`                        | Boundary condition: Force (Normal direction)                         |
| 31           | `LBC_FORCE_QUADRATIC`                 | Boundary condition: Force (Cylindrical surface load (Secondary))     |
| 32           | `LBC_FORCE_SINE`                      | Boundary condition: Force (Cylindrical surface load (Sine))          |
| 33           | `LBC_FORCE_VECTOR`                    | Boundary condition: Force (Cylindrical surface load (Vector))        |
| 34           | `LBC_NOLIN1`                          | Boundary condition: Force (Non-linear force (NOLIN1))                |
| 35           | `LBC_NOLIN3`                          | Boundary condition: Force (Non-linear force (NOLIN3))                |
| 36           | `LBC_NOLIN4`                          | Boundary condition: Force (Non-linear force (NOLIN4))                |
| 37           | `LBC_CONSTRAINT`                      | Boundary condition: Constraint                                       |
| 38           | `LBC_ENFORCED_DISP`                   | Boundary condition: Forced displacement                              |
| 39           | `LBC_GRAVITY`                         | Boundary condition: Gravity                                          |
| 40           | `LBC_G_PRESSURE`                      | Boundary condition: Pressure (general)                               |
| 41           | `LBC_H_PRESSURE`                      | Boundary condition: Pressure (Hydrostatic pressure)                  |
| 42           | `LBC_T_PRESSURE`                      | Boundary condition: Pressure (2 points designation)                  |
| 43           | `LBC_PRESSURE_QUADRATIC`              | Boundary condition: Pressure (Cylindrical surface load (Secondary))  |
| 44           | `LBC_PRESSURE_SINE`                   | Boundary condition: Pressure (Cylindrical load (Sine))               |
| 45           | `LBC_T_CENTRIFUGAL_FORCE`             | Boundary condition: Centrifugal force (2 points designation)         |
| 46           | `LBC_CS_CENTRIFUGAL_FORCE`            | Boundary condition: Centrifugal force (Coordinate system)            |
| 47           | `LBC_TEMP_INI`                        | Boundary condition: Initial temperature                              |
| 49           | `LBC_TEMP_LOAD_GENERAL`               | Boundary condition: Temperature load (Constant)                      |
| 50           | `LBC_TEMP_LOAD_ADVC_FILE`             | Boundary condition: Temperature load (ADVC file)                     |
| 51           | `LBC_TEMP_LOAD_NASTRAN`               | Boundary condition: Temperature load (Nastran Punch)                 |
| 52           | `LBC_TEMP_LOAD_ADVC_RESULT_REFERENCE` | Boundary condition: Temperature load (Overall mapping)               |
| 53           | `LBC_TEMP_BOUNDARY`                   | Boundary condition: Boundary temperature                             |
| 54           | `LBC_CONCENTRATE_FLUX`                | Boundary condition: Concentrated heat flux                           |
| 55           | `LBC_SURFACE_FLUX`                    | Boundary condition: Surface heat flux                                |
| 56           | `LBC_THERMAL_CONVECTION`              | Boundary condition: Surface convection                               |
| 57           | `LBC_ENFORCED_VELOCITY`               | Boundary condition: Forced speed                                     |
| 58           | `LBC_ENFORCED_ACCELERATION`           | Boundary condition: Forced acceleration                              |
| 60           | `LBC_CONTACT_CLEARANCE`               | Boundary connection: Contact (Contact surface gap amount)            |
| 61           | `LBC_MAPPING_PRESSURE`                | Boundary condition: Pressure (surface mapping)                       |
| 64           | `LBC_MAPPING_TEMP_BOUNDARY`           | Boundary condition: Boundary temperature (Surface mapping)           |
| 65           | `LBC_MAPPING_THERMAL_CONVECTION`      | Boundary condition: Surface convection (surface mapping)             |
| 66           | `LBC_INITSTRESS_GENERAL`              | Boundary condition: Initial stress                                   |
| 68           | `LBC_PRETENSION`                      | Connection: Pretension (general)                                     |
| 69           | `LBC_PRETENSION_ABAQUS`               | Connection: Pretension (Abaqus)                                      |
| 70           | `LBC_SURFACE_LOADS`                   | Boundary condition: Pressure (ADVC)                                  |
| 71           | `LBC_SUBMODEL_FORCED_DISP`            | Boundary condition: Sub-model forced displacement                    |
| 72           | `LBC_SUBMODEL_FORCED_TEMP`            | Boundary condition: Sub-model forced temperature                     |
| 73           | `LBC_SUBMODEL_FORCED_FLUX`            | Boundary condition: Sub-model forced heat flux                       |
| 74           | `LBC_INSIDE_HEAT_GENERATION`          | Boundary condition: Internal heat flux                               |
| 75           | `LBC_RIGIDWALL`                       | Connection: Rigid wall                                               |
| 76           | `LBC_INIT_ANGULAR_VEL_ABAQUS`         | Boundary condition: Initial angular velocity (Abaqus)                |
| 78           | `SUP_GROUP`                           | Parent group (For tree display)                                      |
| 79           | `GROUP`                               | Group                                                                |
| 80           | `ELEMEDGE_GROUP`                      | Element edge group                                                   |
| 81           | `FIELD_DATA`                          | Field data                                                           |
| 82           | `PROPERTY_0D_MASS`                    | Connection: Mass element                                             |
| 83           | `PROPERTY_1D_BAR`                     | Property: 1D (Bar element)                                           |
| 84           | `PROPERTY_1D_BEAM`                    | Property: 1D (Beam element)                                          |
| 85           | `PROPERTY_1D_ROD`                     | Property: 1D (Rod)                                                   |
| 86           | `PROPERTY_1D_PLOT`                    | Connection: Plot                                                     |
| 87           | `PROPERTY_2D_SHELL`                   | Property: 2D (Shell)                                                 |
| 88           | `PROPERTY_2D_COMPOSITE_SHELL`         | Property: 2D (Laminated material)                                    |
| 89           | `PROPERTY_3D_SOLID`                   | Property: 3D (Solid)                                                 |
| 90           | `PROPERTY_3D_GASKET`                  | Property: 3D (Gasket)                                                |
| 91           | `PROPERTY_3D_COHESIVE`                | Property: 3D (Adhesive element)                                      |
| 93           | `SECTION_GENERAL`                     | Property: 1D (Section (General))                                     |
| 94           | `SECTION_LIBRARY`                     | Property: 1D (Section (Library))                                     |
| 96           | `CONNECT_MPC`                         | Connection: MPC                                                      |
| 97           | `CONNECT_SPRING`                      | Connection: Spring element                                           |
| 98           | `CONNECT_RBE2`                        | Connection: RBE2                                                     |
| 99           | `CONNECT_CONM`                        | Connection: Mass element                                             |
| 101          | `CONNECT_RBAR`                        | Connection: Bar element                                              |
| 102          | `CONNECT_RBE3`                        | Connection: RBE3                                                     |
| 103          | `CONNECT_BUSH`                        | Connection: Bush                                                     |
| 106          | `CONNECT_DAMPER`                      | Connection: Damper                                                   |
| 107          | `CONNECT_CONNECTOR`                   | Connection: Connector                                                |
| 108          | `CONTACT_ADVC`                        | Connection: Contact (ADVC)                                           |
| 109          | `CONTACT_NXNASTRAN`                   | Connection: Contact (NX Nastran)                                     |
| 110          | `CONTACT_MSCNASTRAN`                  | Connection: Contact (MSC Nastran)                                    |
| 111          | `CONTACT_ABAQUS`                      | Connection: Contact (Abaqus)                                         |
| 112          | `CONTACT_ANSYS`                       | Connection: Contact (Ansys)                                          |
| 117          | `DCS`                                 | Displacement coordinate system                                       |
| 118          | `ADVCPROCESS`                         | ADVC process                                                         |
| 119          | `ADVCPROCESS_STATIC`                  | ADVC process (Static)                                                |
| 120          | `ADVCPROCESS_DYNAMIC`                 | ADVC process (Dynamic)                                               |
| 121          | `ADVCPROCESS_EIGEN`                   | ADVC process (Eigen value)                                           |
| 122          | `ADVCPROCESS_CREEP`                   | ADVC process (Creep)                                                 |
| 123          | `ADVCPROCESS_DYNAMIC_EXPLICIT`        | ADVC process (Dynamic explicit)                                      |
| 124          | `ADVCPROCESS_FATIGUE`                 | ADVC process (Fatigue)                                               |
| 125          | `ADVCPROCESS_MODAL_FREQ_RESP`         | ADVC process (Modal frequency response)                              |
| 126          | `ADVCPROCESS_RESP_SPEC`               | ADVC process (Response spectrum)                                     |
| 127          | `ADVCPROCESS_RAND_RESP`               | ADVC process (Random response)                                       |
| 130          | `ADVCJOB`                             | ADVC job                                                             |
| 131          | `ABAQSTEPS`                           | Abaqus step                                                          |
| 132          | `ABAQSTEPS_STRUCT`                    | Abaqus Step: Structure                                               |
| 133          | `ABAQSTEPS_THERMAL`                   | Abaqus step: Heat transfer                                           |
| 134          | `ABAQSTEPS_STRUCT_STATIC`             | Abaqus Step: Structure (Static General)                              |
| 135          | `ABAQSTEPS_STRUCT_FREQUENCY`          | Abaqus Step: Structure (Natural Frequency)                           |
| 136          | `ABAQSTEPS_STRUCT_COUPLEDTD`          | Abaqus Step: Structure(Coupled-Temp-Displacement)                    |
| 137          | `ABAQSTEPS_STRUCT_DYNAMIC`            | Abaqus Step: Structure (Dynamic Implicit)                            |
| 138          | `ABAQSTEPS_STRUCT_DYNAMIC_COUPLEDTD`  | Abaqus Step: Structure (Dynamic Coupled-Temp-Displacement, Explicit) |
| 139          | `ABAQSTEPS_STRUCT_DYNAMIC_EXPLICIT`   | Abaqus Step: Structure (Dynamic Explicit)                            |
| 140          | `ABAQSTEPS_STRUCT_STATICRISK`         | Abaqus Step: Structure (Static Riks)                                 |
| 141          | `ABAQSTEPS_THERMAL_SS`                | Abaqus Step: Heat transfer (Steady State)                            |
| 142          | `ABAQSTEPS_THERMAL_TRANSIENT`         | Abaqus Step: Heat (Transient)                                        |
| 143          | `ABAQUSJOB`                           | Abaqus job                                                           |
| 144          | `LBC_MAPPING_HEATFLUX`                | Boundary condition: Heat flux (Surface mapping)                      |
| 145          | `CONNECT_GAP`                         | Connection: Gap                                                      |
| 146          | `ANSYSJOB`                            | Ansys job                                                            |
| 147          | `NASTRANJOB`                          | Nastran job                                                          |
| 148          | `DYANAMISJOB`                         | TS-Solver job                                                        |
| 151          | `ACTRANJOB`                           | Actran job                                                           |
| 152          | `LSDYNAJOB`                           | LS-Dyna job                                                          |
| 153          | `NCS`                                 | Nodal coordinate system                                              |
| 155          | `LBC_DOFSET`                          | Boundary condition: Definition of degrees of freedom                 |
| 156          | `BEAM_PROP_ATTR`                      | Property: Beam element attribute 1                                   |
| 157          | `BEAM_PROP_ATTR2`                     | Property: Beam element attribute 2                                   |
| 158          | `SHELL_PROP_ATTR`                     | Property: Shell attribute                                            |
| 159          | `CONN_PROP_ATTR`                      | Property: Join attribute                                             |
| 163          | `CONNECTION_ELEMENT`                  | Connection: Connection element                                       |
| 164          | `CONTACT_TSSS`                        | Connection: Contact (SunShine)                                       |

## Element types

ElemKind is an enumeration of element types.

| ElemKind      | Description                     | ElemType             | Description                       |
| ------------- | ------------------------------- | -------------------- | --------------------------------- |
| `ELEMKIND_0D` | An element prepared for a node. | `ELEMTYPE_POINT`     | Vertex element.                   |
| `ELEMKIND_1D` | 1D element (bar element).       | `ELEMTYPE_LINE2`     | 1D element (First order element)  |
|               |                                 | `ELEMTYPE_LINE3`     | 1D element (Second order element) |
| `ELEMKIND_2D` | 2D element (Shell element)      | `ELEMTYPE_TRI3`      | Triangular primary element        |
|               |                                 | `ELEMTYPE_TRI6`      | Triangular quadratic element      |
|               |                                 | `ELEMTYPE_QUAD4`     | Quadratic first order element     |
|               |                                 | `ELEMTYPE_QUAD8`     | Quadratic second order element    |
| `ELEMKIND_3D` | 3D element (Solid element)      | `ELEMTYPE_TET4`      | Tetra first order element         |
|               |                                 | `ELEMTYPE_TET10`     | Tetra second order element        |
|               |                                 | `ELEMTYPE_HEX8`      | Hex first order element           |
|               |                                 | `ELEMTYPE_HEX20`     | Hex second order element          |
|               |                                 | `ELEMTYPE_PRISM6`    | Penta first order element         |
|               |                                 | `ELEMTYPE_PRISM15`   | Penta second order element        |
|               |                                 | `ELEMTYPE_PYRAMID5`  | Pyramid first order element       |
|               |                                 | `ELEMTYPE_PYRAMID13` | Pyramid second order element      |

## Unit types

An enumeration type that represents units.

Function used:

- [ConvertFromDocUnit](./../../psj_utility/PSJ-Utility_ConvertFromDocUnit.md)

- [ConvertFromMacroUnit](./../../psj_utility/PSJ-Utility_ConvertFromMacroUnit.md)

- [ConvertValueToDocUnit](./../../psj_utility/PSJ-Utility_ConvertValueToDocUnit.md)

- [ConvertValueToMacroUnit](./../../psj_utility/PSJ-Utility_ConvertValueToMacroUnit.md)

| Unit Type                       | Description                     | String Unit                                                                                |
| ------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------ |
| `Unit_Length`                   | Length                          | $mm\\m\\ft\\in\\cm$                                                                        |
| `Unit_Time`                     | Time                            | $s\\min\\h$                                                                                |
| `Unit_Mass`                     | Mass                            | $t\\kg\\kgf*s^2/mm\\slug\\lbf*s^2/in\\lb\\g$                                               |
| `Unit_Force`                    | Force                           | $N\\mN\\kgf\\lbf\\tf$                                                                      |
| `Unit_Angle`                    | Angle                           | $deg\\rad$                                                                                 |
| `Unit_Temperature`              | Temperature                     | $K\\deg C\\deg F$                                                                          |
| `Unit_Area`                     | Area                            | $mm^2\\m^2\\ft^2\\in^2\\cm^2$                                                              |
| `Unit_Volume`                   | Volume                          | $mm^3\\m^3\\ft^3\\in^3\\cm^3$                                                              |
| `Unit_Velocity`                 | Velocity                        | $mm/s\\m/s\\ft/s\\in/s$                                                                    |
| `Unit_Acceleration`             | Acceleration                    | $mm/s^2\\m/s^2\\ft/s^2\\in/s^2\\g\\Gal$                                                    |
| `Unit_RotateVelo`               | Rotational velocity             | $rad/s\\deg/s\\rpm$                                                                        |
| `Unit_RotateAcc`                | Rotational acceleration         | $rad/s^2\\deg/s^2$                                                                         |
| `Unit_Moment`                   | Moment                          | $N*mm\\N*m\\mN*mm\\kgf*mm\\lbf*ft\\lbf*in\\tf*m$                                           |
| `Unit_Pressure`                 | Pressure                        | $MPa\\Pa\\kPa\\kgf/mm^2\\lbf/ft^2\\lbf/in^2\\tf/m^2\\GPa$                                  |
| `Unit_Density`                  | Density                         | $t/mm^3\\kg/m^3\\kg/mm^3\\kgf*s^2/mm^4\\slug/ft^3\\lbf*s^2/in^4$                           |
| `Unit_Stiffness`                | Stiffness                       | $N/mm\\N/m\\mN/mm\\kgf/mm\\lbf/ft\\lbf/in$                                                 |
| `Unit_RotateStiff`              | Rotational stiffness            | $N*mm/rad\\N*m/rad\\mN*mm/rad\\kgf*mm/rad\\lbf*ft/rad\\lbf*in/rad\\N*mm/deg$               |
| `Unit_DampingCoef`              | Damping coefficient             | $N*s/mm\\N*s/m\\mN*s/mm\\kgf*s/mm\\lbf*s/ft\\lbf*s/in$                                     |
| `Unit_RotateDampingCoef`        | Rotational damping coefficient  | $N*mm*s/rad\\N*m*s/rad\\mN*mm*s/rad\\kgf*mm*s/rad\\lbf*ft*s/rad\\lbf*in*s/rad\\N*mm*s/deg$ |
| `Unit_Modulus`                  | Elastic modulus                 | $N/mm^2\\N/m^2\\mN/mm^2\\kgf/mm^2\\lbf/ft^2\\lbf/in^2$                                     |
| `Unit_Energy`                   | Energy                          | $mJ\\J\\miuJ\\kcal\\ft*lbf\\in*lbf\\kJ\\cal$                                               |
| `Unit_Power`                    | Power                           | $mW\\W\\miuW\\kcal/s\\ft*lbf/s\\in*lbf/s$                                                  |
| `Unit_ThermalExCoef`            | Coefficient of linear expansion | $/K$                                                                                       |
| `Unit_ThermalConductivity`      | Thermal conductivity            | $mW/mm*K\\W/m*K\\miuW/mm*K\\kcal/mm*h*K\\lbf/s*K$                                          |
| `Unit_ConvectionCoef`           | Convection coefficient          | $mW/mm^2*K\\W/m^2*K\\miuW/mm^2*K\\kcal/mm^2*h*K\\lbf/ft*s*K\\lbf/in*s*K$                   |
| `Unit_SpecificHeat`             | Specific heat                   | $mJ/t*K\\J/kg*K\\miuJ/kg*K\\kcal/kg*K\\ft*lbf/slug*K\\in^2/s^2*K$                          |
| `Unit_HeatFlux`                 | Heat flux                       | $mW/mm^2\\W/m^2\\miuW/mm^2\\kcal/mm^2*h\\lbf/ft*s\\lbf/in*s$                               |
| `Unit_HeatGeneration`           | Heat generation                 | $mW/mm^3\\W/m^3\\miuW/mm^3\\kcal//mm^3*h\\lbf/ft^2*s\\lbf/in^2*s$                          |
| `Unit_MomentInertia`            | Inertia (Area) moment           | None                                                                                       |
| `Unit_TorsionalConst`           | Torsional rigidity              | None                                                                                       |
| `Unit_WarpCoef`                 | Warping factor                  | $mm^6\\m^6\\ft^6\\in^6\\cm^6$                                                              |
| `Unit_LinearMassMomentIntertia` | Mass moment of inertia          | None                                                                                       |
| `Unit_Stress`                   | Stress                          | $N/mm^2\\N/m^2\\mN/mm^2$                                                                   |
| `Unit_Strain`                   | Strain                          | None                                                                                       |
| `Unit_ThermalEnergy`            | Thermal energy                  | $J\\mJ\\cal$                                                                               |
| `Unit_Frequency`                | Frequency                       | $Hz$                                                                                       |
| `Unit_VolumeEnergyDensity`      | Volume energy density           | $J/mm^3\\J/m^3\\mJ/mm^3$                                                                   |

```{toctree}
:hidden:
item_class/Class_BodyVector
item_class/Class_VersionInfo
item_class/Class_DBody
item_class/Class_DEdge
item_class/Class_DElem
item_class/Class_DFace
item_class/Class_DGroup
item_class/Class_DItem
item_class/Class_DItemVector
item_class/Class_DNode
item_class/Class_DoubleVector
item_class/Class_EdgeVector
item_class/Class_ElemVector
item_class/Class_FaceVector
item_class/Class_GroupVector
item_class/Class_NodeVector
item_class/Class_StringVector
item_class/Class_TVector3d
item_class/Class_VersionInfo
```
