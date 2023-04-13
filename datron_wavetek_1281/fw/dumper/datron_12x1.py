"""Datron 1271/1281 calram dumping utility

By leighcorrigall based on earlier work by rigrunner and TheSteve
https://www.eevblog.com/forum/metrology/datron-1281-repairmaintenance/msg3876473/#msg3876473

Modified to use pyvisa by @arr-ee"""

import sys
import os
import pprint

from collections import OrderedDict

import pyvisa


def get_lower_bytes(data: bytes) -> bytes:
    """
    NVRAM IC is on the low 8 bits of the 16 bit bus so we need
    to strip the low bytes from the returned words and discard the high bits
    """
    buffer = []
    words = data.split(b" ")

    for i in range(1, 9):  # ignore the first word
        word = words[i]
        lower_byte = word[2:]
        lower = int(lower_byte, 16)
        buffer.append(lower)

    # print(''.join([chr(x) for x in buffer]))

    return bytes(buffer)


region_to_size_dict = {
    "IPZ": 4096,
    "SECN": 8192,
    "PRIM": 4096,
}


def dump(region, filename):
    if region not in region_to_size_dict:
        raise Exception("unsupported region name {}".format(region))

    size = region_to_size_dict[region]

    print("dumping to file {}".format(filename))

    with open(filename, "wb") as file:
        for i in range(0, size, 16):  # 16 bit
            datron.write("DUMP? " + region + "," + str(i))

            # progress
            sys.stdout.write(
                "\r{percent}% complete".format(percent=str(round((i * 100) / size)))
            )
            sys.stdout.flush()

            data = datron.read_raw()
            lower_bytes = get_lower_bytes(data)
            file.write(lower_bytes)

    sys.stdout.write("\t{} done.\n".format(region))
    sys.stdout.flush()


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=2)

    rm = pyvisa.ResourceManager()
    print(rm.list_resources())
    datron_visastr = "ASRL/dev/cu.usbmodem101::INSTR"

    data = b"0000 7410 7403 74CF 74F1 74EF 74FF 74DF 74DC"
    pp.pprint(
        OrderedDict(
            data=data,
            observed=get_lower_bytes(data),
            expected=b"\x10\x03\xcf\xf1\xef\xff\xdf\xdc",
            expected_str="\x10\x03ÏñïÿßÜ",
        )
    )

    datron: pyvisa.resources.MessageBasedResource = rm.open_resource(datron_visastr)

    datron.write("*RST")  # reset the meter
    datron.write("*IDN?")  # identify

    info = datron.read()
    id, model, serial, firmware = [x.strip() for x in info.split(",")]

    pp.pprint(OrderedDict(id=id, model=model, serial=serial, firmware=firmware))

    ipz_filename = "{serial}.ipz.nvram".format(serial=serial)
    dump("IPZ", ipz_filename)

    secn_filename = "{serial}.secn.nvram".format(serial=serial)
    dump("SECN", secn_filename)

    prim_filename = "{serial}.prim.nvram".format(serial=serial)
    dump("PRIM", prim_filename)

    nvram_filename = "{serial}.nvram.bin".format(serial=serial)

    os.system(
        "cat {input_filenames} > {output_filename}".format(
            input_filenames=" ".join([ipz_filename, secn_filename, prim_filename]),
            output_filename=nvram_filename,
        )
    )

    print("finished!")
