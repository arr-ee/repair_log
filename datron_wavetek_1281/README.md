# General notes

Debug pathways: DCV 1V range, adjust resolution etc, STATUS => CONFIG => +-

## Current status

- [SN 35239](sn35239_log.md): WIP, bad current board, intsource characterisation fail
- [SN 43268](sn43268_log.md): WIP, vref mismatch

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

[Digital testpoints](photos/testpoints_digital.png), [DC testpoints](photos/testpoints_dc.png)

## Revision differences (SN 35239 and up)

- Plastic fasteners appear to be in decent condition, latches can be reused
- Binding posts are fixed and not retractable

### DC assy v3.4

- No major botches on the bottom of the board.
- No components attached to legs of electrolytics.
- Capacitor values are different to what's in service manual:

  | Designator       | Value per manual | Value as found |
  | :--------------- | :--------------- | :------------- |
  | C307,308,312,313 | 100uF @ 25V      | 100uF @ 50V    |
  | C901,904,905     | 1000uF @ 40V     | 1000uF @ 50V   |
  | C807             | 470uF @ 25V      | no change      |
  | C907,910         | 33uF @ 63V       | *220uF* @ 63V  |
  | C909,912,913,914 | 1uF @ 63V        | 1uF @ 100V     |

  All capacitors were United ChemiCon KME

### Digital assy v1.12

- Capacitor values are different to what's in service manual:

  | Designator | Value per manual | Value as found |
  | :--------- | :--------------- | :------------- |
  | C501       | 1000uF @ 40V     | 1000uF @ 50V   |
  | C502       | 470uF @ 63V      | no change      |
  | C510       | 220uF @ 40V      | 220uF @ 50V    |
  | C513,514   | 2200uF @ 16V     | 2200uF @ 25V   |
  | C515       | 470uF @ 25V      | no change      |
  | C520       | 330uF @ 100V     | 220uF @ 100V   |

## Misc

- `-35V` in-guard PSU appears to not be used. It only goes to the Current board, where it never leaves the header.

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
