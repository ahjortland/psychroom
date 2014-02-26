## Standard Measurement Labeling Convention

The goal of the measurement label is to describe the physical quantities
recorded during the experiment. The aim of the label is to record
_meta-information_ about the measurement. In other words, storing the:

* who,
* what,
* where,
* and how

of the measurement.  This is accomplished using a standard labeling convention
by the standards committee.  The standard labeling convention is described
below and its parts are described in individual sections henceforth.

    {COMPONENT}{#?}_{FLUID}{#?}_{LOCATION}{#?}_{TYPE}{#?}

The label stores information about the component, fluid, location, and type of
measurement being recorded.  Additionally, an optional numeric identifier can be
assigned to distinguish between multiple occurrences of components or locations.
For example in a dual compressor systems, the compressors could be identified as
compressor 0 and compressor 1.

### Differential Measurements

Differential measurements are handled in a similar way to normal single point measurements.

However, each part of the name string can now be composed of two parts - the distinction between 
first and second part is made by using a capital letter. Before the type, add "Delta" to specify
that a difference measurement is used. Naming scheme:

    {component1}{Component2?}{#?}_{fluid1}{Fluid2?}{#?}_{location1}{Location2}{#?}_Delta{type1}{Type2?}

#### Examples:
Difference between compressor refrigerant inlet temperature and indoor heat exchanger (evaporator) refrigerant 
outlet temperature:

    idhxComp_ref_outIn_DeltaT
 
 Difference between air inlet temperature of evaporator and refrigerant inlet temperature:
    
    idhx_airRef_inIn_DeltaT

### Component Label Identifier

The component label identifier is used to describe which component in the
overall system the measurement is taken.  A list of acceptable component
identifiers is shown below.

<TABLE>
<CAPTION><EM>Acceptable component identifiers and descriptions.</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR>
        <TH>Identifier</TH>
        <TH>Description</TH>
        <TH>Example</TH>
    </TR>
<TBODY>
    <TR>
        <TD>absr
        <TD>absorber
        <TD>
    </TR>
    <TR>
        <TD>accm
        <TD>accumulator
        <TD>
    </TR>
    <TR>
        <TD>ahu
        <TD>air handling unit
        <TD>
    </TR>
    <TR>
        <TD>amb
        <TD>ambient
        <TD>
    </TR>
    <TR>
        <TD>comp
        <TD>compressor
        <TD>
    </TR>
    <TR>
        <TD>damp
        <TD>damper
        <TD>
    </TR>
    <TR>
        <TD>desr
        <TD>desorber
        <TD>
    </TR>
    <TR>
        <TD>eng
        <TD>engine
        <TD>
    </TR>
    <TR>
        <TD>ehr
        <TD>electric heater
        <TD>
    </TR>
    <TR>
        <TD>ejr
        <TD>ejector/injector
        <TD>
    </TR>
    <TR>
        <TD>fan
        <TD>fan
        <TD>
    </TR>
    <TR>
        <TD>filt
        <TD>filter
        <TD>
    </TR>
    <TR>
        <TD>idhx
        <TD>indoor heat exchanger
        <TD>
    </TR>
    <TR>
        <TD>ithx
        <TD>internal heat exchanger
        <TD>
    </TR>
    <TR>
        <TD>liql
        <TD>Liquid line
        <TD>
    </TR>
    <TR>
        <TD>mflr
        <TD>muffler
        <TD>
    </TR>
    <TR>
        <TD>mot
        <TD>motor
        <TD>
    </TR>
    <TR>
        <TD>noz
        <TD>nozzle box
        <TD>
    </TR>
    <TR>
        <TD>odhx
        <TD>outdoor heat exchanger
        <TD>
    </TR>
    <TR>
        <TD>pump
        <TD>pump
        <TD>
    </TR>
    <TR>
        <TD>rect
        <TD>rectifier
        <TD>
    </TR>
    <TR>
        <TD>recv
        <TD>receiver
        <TD>
    </TR>
    <TR>
        <TD>sep
        <TD>separator
        <TD>
    </TR>
    <TR>
        <TD>od
        <TD>outdoor
        <TD>
    </TR>
    <TR>
        <TD>odu
        <TD>outdoor unit
        <TD>outdoor unit
    </TR>
    <TR>
        <TD>valv
        <TD>valve
        <TD>
    </TR>
    <TR>
        <TD>rvalv
        <TD>reversing valve
        <TD>
    </TR>
    <TR>
        <TD>vsd
        <TD>variable speed/frequency drive
        <TD>
    </TR>
    <TR>
        <TD>vapl
        <TD>vapor line
        <TD>
    </TR>
    <TR>
        <TD>xd
        <TD>expansion device
        <TD>
    </TR>
</TABLE>


### Fluid Label Identifier

The fluid label identifier is used to describe the "fluid" being measured by the
measurement device.  A list of acceptable fluid identifiers is shown below.

<TABLE>
<CAPTION><EM>Acceptable fluid identifiers and descriptions.</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR>
        <TH>Identifier</TH>
        <TH>Description</TH>
        <TH>Example</TH>
    </TR>
<TBODY>
    <TR>
        <TD>air
        <TD>air
        <TD>ahu_air_mix_T is the air handling unit mixed-air temperature
    </TR>
    <TR>
        <TD>elec
        <TD>electric
        <TD>comp_elec_ctrl_pwr is the compressor controller electric power
    </TR>
        <TR>
        <TD>ngas
        <TD>natural gas
        <TD>htr_ngas_in_mdot is the heater natural gas inlet mass flow rate
    </TR>
    <TR>
        <TD>gwm
        <TD>glycol water mixture
        <TD>mixtures of glycol and water. mixture ratio to be defined in file header
    </TR>
    <TR>
        <TD>brn
        <TD>brine
        <TD>ithx_brn_out_T is the internal heat exchanger brine outlet
        temperature
    </TR>
    <TR>
        <TD>h2o
        <TD>water
        <TD>ithx_h2o_in_mdot is the internal heat exchanger water inlet mass
        flow rate
    </TR>
    <TR>
        <TD>oil
        <TD>oil
        <TD>sep_oil_out_T is the oil outlet temperature of the separator
    </TR>
    <TR>
        <TD>ref
        <TD>refrigerant
        <TD>odhx_ref_out_pg is the outdoor heat exchanger refrigerant outlet
        gauge pressure
    </TR>
    <TR>
        <TD>rich
        <TD>rich solution
        <TD>absr_rich_out_T is the outlet temperature of the rich solution in
        the absorber
    </TR>
    <TR>
        <TD>weak
        <TD>weak solution
        <TD>rect_weak_out_mdot is the outlet mass flow rate of the weak solution
        in the rectifier
    </TR>
    <TR>
        <TD>mech
        <TD>mechanical, e.g. shaft or belt; what exactly needs to be
        clear from schematic
        <TD>
    </TR>
</TABLE>


### Location Label Identifier

The location label identifier is used to describe where on the component the
measurement is taken.  A list of acceptable location identifiers is shown below.

<TABLE>
<CAPTION><EM>Acceptable location identifiers and descriptions.</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR>
        <TH>Identifier</TH>
        <TH>Description</TH>
        <TH>Explanation</TH>
        <TH>Example</TH>
    </TR>
<TBODY>
    <TR>
        <TD>crct
        <TD>circuit
        <TD>Anywhere between the main inlet and outlet of heat exchangers
        <TD>odhx_ref_crct1_T is the temperature at a location marked as #1 
        within the refrigerant circuit of the outdoor heat exchanger
    </TR>
    <TR>
        <TD>ctrl
        <TD>controller
        <TD>Controller of a component
        <TD>fan_elec_ctrl_pwr is the power consumption of the fan controller
    </TR>
    <TR>
        <TD>dmp
        <TD>damper
        <TD>Damper of a component
        <TD>ahu_air_damp_pos is the opening position of the damper in 
        the air handling unit
    </TR>
    <TR>
        <TD>exh
        <TD>exhaust
        <TD>Exhaust from a component
        <TD> ahu_air_exh_T is the temperature at the exhaust of the air handling
        unit
    </TR>
    <TR>
        <TD>gasl
        <TD>gas line
        <TD>Gas line along the refrigerant circuit of a component
        <TD>odhx_ref_gasl_pg is the gauge pressure at the exit towards the gas
        line of the system at the outdoor heat exchanger
    </TR>
    <TR>
        <TD>in
        <TD>inlet
        <TD>Inlet of a component
        <TD>ithx_brn_in_T is the inlet brine temperature of an internal heat
        exchanger
    </TR>
    <TR>
        <TD>int
        <TD>internal, interior
        <TD>Internal part of a component
        <TD> comp_ref_int1_pg is the gauge pressure of the internal location #1
        inside the compressor
    </TR>
    <TR>
        <TD>idr
        <TD>indoor
        <TD>A location in the indoor room around a component
        <TD> ahu_air_indr_B is the indoor room wet-bulb temperature around the
        air handling unit
    </TR>
    <TR>
        <TD>lvl
        <TD>level
        <TD>
        <TD>
    </TR>
    <TR>
        <TD>liql
        <TD>liquid line
        <TD>Liquid line along the refrigerant circuit of a component
        <TD> odhx_ref_liql_pg is the gauge pressure at the exit towards 
        the liquid line at the outdoor heat exchanger
    </TR>
    <TR>
        <TD>mix
        <TD>mixed
        <TD>Mixing chamber inside a component
        <TD> ahu_air_mix_D is the dew point at the mixing chamber inside the air
        handling unit
    </TR>
    <TR>
        <TD>odr
        <TD>outdoor
        <TD>A location around the outdoor room at a component
        <TD> comp_air_odr_T is the temperature around the compressor in the
        outdoor room
    </TR>
    <TR>
        <TD>out
        <TD>outlet
        <TD>Outlet of a component
        <TD>xd2_ref_out_pg is the gauge pressure at the refrigerant outlet of
        expansion valve #2
    </TR>
    <TR>
        <TD>phas
        <TD>phase
        <TD>Phase of power supply to a component
        <TD>comp_elec_phas2_I is the current at the second phase of the
        electrical power supply to the compressor
    </TR>
    <TR>
        <TD>plnm
        <TD>plenum
        <TD>Plenum of a component
        <TD>idhx_air_plenum_D is the dew point at the plenum of the indoor unit
        heat exchanger
    </TR>
    <TR>
        <TD>ret
        <TD>return
        <TD>Return air duct of a component
        <TD>ahu_air_ret_B is the air wet-bulb temperature at the return air pipe
        of the air handling unit
    </TR>
    <TR>
        <TD>sply
        <TD>supply
        <TD>Supply air duct of a component
        <TD>ahu_air_sply_RH is the air relative humidity at the supply air pipe
        of the air handling unit
    </TR>
    <TR>
        <TD>srnd
        <TD>surroundings
        <TD>Surroundings of the psychrometric chamber
        <TD> noz_air_srndInt_DeltaP is the air pressure difference between the
        atmosphere and the interior of the nozzle box
    </TR>
    <TR>
        <TD>surf
        <TD>surface
        <TD>Surface of a component
        <TD>comp_air_surf_T is the air-side compressor surface temperature
    </TR>
</TABLE>


### Measurement Type Label Identifier

The measurement type label identifier is used to describe the actual type of
measurement being recorded.  A list of acceptable measurement types is shown
below.
<TABLE>
<CAPTION><EM>Acceptable measurement type identifiers and
             descriptions.</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR>
        <TH>Identifier</TH>
        <TH>Description</TH>
        <TH>Explanation</TH>
        <TH>Example</TH>
    </TR>
<TBODY>
    <TR>
        <TD>B
        <TD>wet bulb
        <TD>Wet bulb for humid air.
        <TD>idhx_air_in_B is indoor air heat exchanger inlet wet bulb 
	    temperature.
    </TR>
    <TR>
        <TD>D
        <TD>dew point
        <TD>Dew point for humid air/
        <TD>idhx_air_in_D is indoor air heat exchanger inlet dew point 
	    temperature.
    </TR>
    <TR>
        <TD>duty
        <TD>PWM duty cycle
        <TD>Duty cycle for PWM (pulse-width-modulation) type signals.
        <TD>xd_ref_liql_PWM is the duty cycle of a pulse width modulated 
	    electronic expansion valve.
    </TR>
    <TR>
        <TD>freq
        <TD>frequency
        <TD>Frequency of a component.
        <TD>vsd_elec_out_freq is the output frequency of a variable speed drive.
    </TR>
    <TR>
        <TD>I
        <TD>current
        <TD>Electrical current.
        <TD>vsd_elec_out_I is the output current of a variable speed drive 
        and typically equivalent to comp_elec_in_I. 
    </TR>
    <TR>
        <TD>T
        <TD>temperature
        <TD>Temperature.
        <TD>comp_ref_out_T is the refrigerant temperature at the outlet of the 
	    compressor.
    </TR>
    <TR>
        <TD>mdot
        <TD>mass flow rate
        <TD>Mass flow rate.
        <TD>comp_ref_out_mdot is the refrigerant outlet flow rate and is 
	    different from comp_ref_in_mdot if vapor injected compression is used.
    </TR>
    <TR>
        <TD>pa
        <TD>absolute pressure
        <TD>Absolute pressure measurement.
        <TD>comp_ref_out_pa is the absolute refrigerant outlet pressure of the 
	    compressor if an absolute pressure transducer was used. 
    </TR>
    <TR>
        <TD>pag
        <TD>absolute pressure, based on gauge pressure measurement
        <TD>Gauge pressure measurement converted to absolute 
	    pressure at the time of measurement.
        <TD>comp_ref_out_pag is the absolute refrigerant outlet pressure of the 
	    compressor if a gauge pressure transducer was used and the value is 
	    already containing the compensation for the ambient pressure.
    </TR>
    <TR>
        <TD>pg
        <TD>gauge pressure
        <TD>Gauge pressure measurement.
        <TD> comp_ref_out_pg is the gauge refrigerant outlet pressure of the 
	    compressor if a gauge pressure transducer was used. 
    </TR>
    <TR>
        <TD>pos
        <TD>position
        <TD>Position of an adjustable component.
        <TD> ahu_air_damp_pos is the opening position of the damper in the air 
	    handling unit.
    </TR>
    <TR>
        <TD>pwr
        <TD>power
        <TD>Electrical power.
        <TD>Comp_elec_in_power is the input power of the compressor. Note: do 
	    not use power for mechanical measurements, rather report RPM and torque.
    </TR>
    <TR>
        <TD>RH
        <TD>relative humidity
        <TD>Relative humidity of air.
        <TD>idhx_air_out_RH is the relative humidity of the air leaving the 
	    evaporator.
    </TR>
    <TR>
        <TD>spd
        <TD>rotational speed
        <TD>Rotational speed of a component.
        <TD> comp_mech_int_speed is the rotational speed of the compressor and 
	    typically different from comp_elec_in_freq.
    </TR>
    <TR>
        <TD>sw
        <TD>switch
        <TD>State of a switch.
        <TD>sep_oil_lvl_sw is the state of the liquid level switch in the oil 
	    separator.
    </TR>
    <TR>
        <TD>u
        <TD>flow velocity
        <TD>Flow velocity of a fluid.
        <TD>idhx_air_in_u is the indoor heat exchanger inlet flow velocity.
    </TR>
    <TR>
        <TD>V
        <TD>voltage
        <TD>Electrical voltage.
        <TD>fan_elec_in_V is the electrical voltage of the indoor fan power.
    </TR>
    <TR>
        <TD>Vdot
        <TD>volumetric flow rate
        <TD>Volumetric flow rate of a fluid
        <TD>noz_air_in_Vdot is the flow rate measured by the flow measurement
	    nozzle box.
    </TR>
</TABLE>

### Example Systems

* [Refrigerant circuit of a ductless, split system heat pump](https://github.com/ahjortland/psychroom/tree/master/docs/dhp_example_labels.md)
* [Air-side measurements of a rooftop air conditioner](https://github.com/ahjortland/psychroom/tree/master/docs/rtu_example_labels.md)
