quality-assessment-script
=========================

This script is used to compare the output files from [Crossbow](http://bowtie-bio.sourceforge.net/crossbow/) to see how consistent the results are after many attempts. It accepts any number of files as inputs and compares them all against each other.

By default, all columns of the files are compared against each other, however this can be modified by changing the columns in the `COLUMNS_TO_CHECK` list. 
Please note: These values at these indexes are described [here](http://bowtie-bio.sourceforge.net/crossbow/manual.shtml#crossbow-output), however they range from 0 to 17 instead of 1 to 18.

Usage
=====
`python quality-assessment-script.py files...` 
