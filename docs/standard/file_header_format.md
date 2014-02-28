### Header Section Information

The header section is composed of information related to the test that does not
change or is held constant during a particular test.  For instance, the
refrigerant charge level may be measured before the test begins and is not
changed during the test itself. Additionally information about the equipment
tested, such as model numbers, can be recorded in this section.

All this information collected in one place would be confusing and hard to
negotiate. To bring more order to the file header, information can be
grouped within individual sections. Attributes can be defined within each
section in the following way:

    attribute name = value

If physical quantities need to be defined in the header (refrigerant charge
amount, control set point, etc.), they can be defined by adding an optional
unit identifier:

    attribute name = value [unit]

When using this convention, all the information recorded within the header can
be parsed and stored conveniently in the data object.

Recommended sections and information recorded therein is summarized as follows.

#### Test Information

This is a general section that records general information about the test.
Information that could be recorded within this section is:

* experimenter's name
* experimenter's contact information
* project name
* test date

Information recorded in this section is not limited to the above suggestions.
Additional information can be added if its deemed important.

#### Testing Conditions

Information pertaining to the psychrometric chamber operating set points and
configuration should be recorded here.

* psychrometric chambers used
* operating set points
* nozzle box configuration

#### Equipment Information

Information pertaining the equipment can be recorded in this section. Useful
information that is invaluable to future researchers includes:

* component model numbers and manufacturers
* component types
* rated performance
* nominal charge, airflow, etc.

#### Sensor Information

Much like the equipment information section, information about the sensors used
during the test is important for researchers quantifying uncertainty.

* sensor model numbers and manufacturers
* sensor types
* sensor configuration

#### Fault Test Information

Fault testing is often performed in order to characterize a system's response
to faulty operation. Information pertaining to the implementation of faults
and their intensities should be recorded.

* charge amount (actual/relative to normal)
* fouling area
* flow rate reduction
* bypass levels
* damper positions
