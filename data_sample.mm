************************************************************************
file with basedata            : mm2_.bas
initial value random generator: 1010900321
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  12
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     10      0       15        7       15
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2           6  10
   3        3          3           7  10  11
   4        3          2           5   9
   5        3          1           8
   6        3          2           7  11
   7        3          1           9
   8        3          1          11
   9        3          1          12
  10        3          1          12
  11        3          1          12
  12        1          0
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  S 1  S 2  S 3  S 4
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     2       0    4    3    0
  3      1     7       0    4    0    7
  4      1     5       3    0    0    7
  5      1     4       7    0    8    0
  6      1     2       0    4    6    0
  7      1     4       0    5    0    4
  8      1     2       5    0    0    8
  9      1     1       6    0    0    6
 10      1     8       0    4    6    0
 11      1     4       4    0    0    7
 12      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  S 1  S 2  S3    S4
    9    8   35   31
************************************************************************
