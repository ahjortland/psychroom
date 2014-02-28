## Test Output File Format

The following sections describes the structure of the output data file
produced using this standard. Using this standard provides the following
benefits:

* test data is clear and understandable even when a person was not involved
in the actual experiment/data collection
* test information usually not recorded (i.e. refrigerant charging amount,
fault conditions, component model numbers/types) are identified clearly
* using the _PsychRoom Toolkit_, data can be easily and quickly imported into
a Python working environment.

The output file standard specifies a structure for saving experimental data as
well as what kinds of items should be saved in each section. Experimental data
is saved as raw text in the following way:

    [section 1]   ------------------------------------
    item_1 = val_1                                    |
    item_2 = val_2                                    |
    .                                                 |H
    .                                                 |E
    .                                                 |A
    [section 2]                                       |D
    item_45 = val_45 [unit]                           |E
    .                                                 |R
    [section N]                                       |
    .                                                 |
    .            -------------------------------------
    [Raw Data]   -------------------------------------
    ,meas_1,meas_2,...,meas_N                         |
    yyyy-mm-dd HH:MM:SS,unit_1,unit_2,...,unit_N      |D
    2014-02-15 08:02:32,0.230,0.435,...,23.99         |A
    2014-02-15 08:02:42,0.330,0.434,...,24.42         |T
    .                                                 |A
    .                                                 |
    .                                                 |
    .                                                 |
    .                                                 |
    .                                                 |
    .                                                 |
    .                                                 |
    .                                                 |
    .                                                 |

In essence, the experimental data file is a configuration with a
comma-separated file appended to it. To identify this type of file, the
default convention used will be to save the file with a `.htf` extension. A
further explanation how each section recorded in the output file should be
formatted can be found:

* [Header Format](https://github.com/ahjortland/psychroom/tree/master/docs/standard/file_header_format.md)
* [Data Output Format](https://github.com/ahjortland/psychroom/tree/master/docs/standard/file_data_format.md)
