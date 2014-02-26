### Data Section Information

Data measured is stored in the output test file under the reserved section
name `[Raw Data]`. This identifies where the file header ends and the
measured data begins. Measurements recorded take the following form:

    LINE 1: ,label_1,label_2,...,label_N
    LINE 2: yyyy-mm-dd HH:MM:SS,unit_1,unit_2,...,unit_N
    LINE 3: timestamp_i,value_1,value_2,...,value_N

#### `LINE 1` - Measurement Labels

Each measurements label should be recorded here as comma-separated list. The
labels should be recorded using the labeling convention described
[here](https://github.com/ahjortland/psychroom/blob/master/docs/label_convention.md).

It should also be noted that a label for the timestamps is not required and a
blank space should be recorded in its place.

#### `LINE 2` - Measurement Units

The unit of each measurement should be recorded on the second line using the
proper unit identifier for the type of measurement. Time stamps should be
recorded in the following format:

    yyyy-mm-dd HH:MM:SS (e.g. 2014-02-21 15:48:43)

#### `LINE 3-EOF` - Measurement Values

The remain values recorded for each measurement at each time stamp should be
recorded on separate rows in a comma-separated format. The first column should
always correspond to the timestamp.
