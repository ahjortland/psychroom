#### Refrigerant circuit of a ductless split heat pump system

Ductless split heat pump system is a split system which can provide heating or
cooling to a building zone. It operates with a compressor, a reversing valve, an
indoor heat exchanger, an electronic expansion valve, an outdoor heat exchanger
and an accumulator. The indoor heat exchanger is housed inside the indoor unit
while the other components are housed in the outdoor unit. The reversing valve
controls the refrigerant flow to provide either heating or cooling to the
building zone.

In this example, an experiment was designed to measure the states of refrigerant
between components and the refrigerant mass flow rate of the system. The
schematic of the sensor location is given as follows.

<img src="https://raw.github.com/ahjortland/psychroom/master/docs/standard/pictures/DHP.png" alt="DHP_ref_fig" title="DHP_ref_fig" style="width: 500px;"/>

In the schematic, the indoor unit is named as ahu1 and the outdoor unit is named
as ahu2. M stands for refrigerant mass flowmeter, T stands for immersion
thermocouples, P stands for gage pressure transducers and W stands for a power 
transducer. The heat exchangers in the system are not labeled as condenser and
evaporator because both heat exchangers can serve as a condenser or an
evaporator. The power transducers are positioned next to the indoor unit and
outdoor unit labels as they are measuring power consumption of the indoor units
and outdoor units but not the power consumption of the individual components.
The refrigerant on the right-handed side of the heat exchangers are always in
vapor form and the pipes on that side are the gas line while other pipes are
called the liquid line. The location of liquid line and gas line and the
refrigerant flow direction are indicated in the legend in the diagram.

The labeling of the sensors is listed as follows.

<TABLE>
<CAPTION><EM>Name and labels of sensors in the ductless split heat pump
    system</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR>
        <TH>Sensor</TH>
        <TH>Label</TH>
        <TH>Explanation</TH>
    </TR>
<TBODY>
    <TR>
        <TD>T at the compressor discharge
        <TD>comp_ref_out_T
        <TD>
    </TR>
    <TR>
        <TD>T at the indoor heat exchanger gas line exit
        <TD>idhx_ref_gasl_T
        <TD>
    </TR>
    <TR>
        <TD>T at the indoor heat exchanger liquid line exit
        <TD>idhx_ref_liql_T
        <TD>
    </TR>
    <TR>
        <TD>T at the expansion valve liquid line exit
        <TD>xd_ref_liql_T
        <TD>Only one location refers to the expansion valve so no number is needed
    </TR>
    <TR>
        <TD>T at the outdoor heat exchanger liquid line exit
        <TD>odhx_ref_liql_T
        <TD>
    </TR>
    <TR>
        <TD>T at the outdoor heat exchanger gas line exit
        <TD>odhx_ref_gasl_T
        <TD>
    </TR>
    <TR>
        <TD>T at the accumulator inlet
        <TD>accm_ref_in_T
        <TD>
    </TR>
    <TR>
        <TD>T at the compressor suction
        <TD>comp_ref_in_T
        <TD>
    </TR>
    <TR>
        <TD>P at the compressor discharge
        <TD>comp_ref_out_pg
        <TD>
    </TR>
    <TR>
        <TD>P at the indoor heat exchanger gas line exit
        <TD>idhx_ref_gasl_pg
        <TD>
    </TR>
    <TR>
        <TD>P at the indoor heat exchanger liquid line exit
        <TD>idhx_ref_liql_pg
        <TD>
    </TR>
    <TR>
        <TD>P at the expansion valve liquid line exit
        <TD>xd_ref_liql_pg
        <TD>Only one location refers to the expansion valve so no number is
        needed
    </TR>
    <TR>
        <TD>P at the outdoor heat exchanger liquid line exit
        <TD>odhx_ref_liql_pg
        <TD>
    </TR>
    <TR>
        <TD>P at the outdoor heat exchanger gas line exit
        <TD>odhx_ref_gasl_pg
        <TD>
    </TR>
    <TR>
        <TD>P at the accumulator inlet
        <TD>accm_ref_in_pg
        <TD>
    </TR>
    <TR>
        <TD>P at the compressor suction
        <TD>comp_ref_in_pg
        <TD>
    </TR>
    <TR>
        <TD>M at the indoor unit heat exchanger liquid line exit
        <TD>idhx_ref_liql_mdot
        <TD>
    </TR>
    <TR>
        <TD>W at the indoor unit
        <TD>ahu1_elec_idr_pwr
        <TD>The indoor unit is labeled as ahu1 and idr means that the power
        transducer is positioned in the indoor room.
    </TR>
    <TR>
        <TD>W at the outdoor unit
        <TD>ahu2_elec_idr_pwr
        <TD>The outdoor unit is labeled as ahu2 and odr means that the power
        transducer is positioned in the indoor room.
    </TR>
</TABLE>
