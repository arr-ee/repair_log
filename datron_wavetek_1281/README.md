# General notes

Debug pathways: DCV 1V range, adjust resolution etc, STATUS => CONFIG => +-

## Other repair logs/resources

- <https://xdevs.com/fix/d1281/>
  - Early-ish Datron models (S/N 19620 & 19608)
  - [FRAM replacement info](https://xdevs.com/fix/d1281/#adapters)
- <https://www.eevblog.com/forum/metrology/datron-1281-repairmaintenance/>
  - Extended thread by `leighcorrigall`
  - S/N 20206
  - [Modernised caldump script](https://www.eevblog.com/forum/metrology/datron-1281-repairmaintenance/msg3876473/#msg3876473) (see also [version using pyvisa](fw/dumper))
  - [Alternative FRAM replacement](https://www.eevblog.com/forum/metrology/datron-1281-repairmaintenance/msg3888764/#msg3888764)
  - Good info on replacement fixtures
- <https://www.eevblog.com/forum/repair/datron-1271-repair/>
  - earlier thread by `rigrunner` on 1271

## Voltage checks

| Board   | Rail        | TP+            | TP-               |
| :------ | :---------- | :------------- | :---------------- |
| DC      | 15          | TP901          | TP101/102 (Mecca) |
| DC      | -15         | TP902          | TP101/102 (Mecca) |
| DC      | 35          | TP903          | TP101/102 (Mecca) |
| DC      | -35         | TP904          | TP101/102 (Mecca) |
| DC      | 5           | TP905          | TP101/102 (Mecca) |
| Digital | 5           | any ic really? | TP503             |
| Digital | 45          | TP502          | TP503             |
| Digital | 11V unreg   |                |                   |
| Digital | -14 unreg   | TP501          | TP503             |
| Digital | -14_2 unreg | TP504          | TP503             |
| Digital | 2.5         | TP201          | TP503             |

## Revision differences

Compared to information available

## Misc

**Outdated** Both meters seem to be severely off on 100mV range (measured at 7dg fast):

| Signal    | Meter | Range | Reading                 |
| :-------- | :---- | :---- | :---------------------- |
| 0 (short) | 35239 | 100mV | -6,28020                |
| 0 (short) | 35239 | 1V    | -0,0000146              |
| 0 (short) | 35239 | 10V   | 00,000036               |
| 0 (short) | 35239 | 100V  | -000,00166              |
| 0 (short) | 35239 | 1kV   | -0000,0007              |
| 100mV     | 35239 | 100mV | 93,78[2-3] + noise      |
| 100mV     | 35239 | 1V    | 0,1000548               |
| 100mV     | 35239 | 10V   | 00,100075               |
| 100mV     | 35239 | 100V  | 000,09945               |
| 100mV     | 35239 | 1kV   | 0000,0975               |
| 110mV     | 35239 | 100mV | 103,783 + noise         |
| 110mV     | 35239 | 1V    | 0,1100546               |
| 110mV     | 35239 | 10V   | 00,110073               |
| 110mV     | 35239 | 100V  | 000,10945               |
| 110mV     | 35239 | 1kV   | 0000,107,6              |
| 100mV     | 43268 | 100mV | 98,[1-4], very noisy    |
| 100mV     | 43268 | 1V    | 0,1000[0-4], very noisy |
| 100mV     | 43268 | 10V   |                         |
| 100mV     | 43268 | 100V  |                         |
| 100mV     | 43268 | 1kV   |                         |
| 110mV     | 43268 | 100mV | 106,[4-8], very noisy   |
| 110mV     | 43268 | 1V    |                         |
| 110mV     | 43268 | 10V   |                         |
| 110mV     | 43268 | 100V  |                         |
| 110mV     | 43268 | 1kV   |                         |
