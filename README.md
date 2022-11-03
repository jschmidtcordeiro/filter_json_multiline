# Filter Json Multiline
This is a program to help filter a file that has many lines of json messages

---

## Quick Start
With the repository downloaded or cloned to your machine you may go to the root folder.

In the root folder, first you add a file to input_files folder to be parsed. A example of the content in the input file is in the Examples topic of this document.

After added the input file run the app.

    python3 app.py input_files/<file.txt> output_files/<file.csv>
    
After running the code successfully you will have a .csv file in the output files ready to be read in the Google Sheets or Excel

## Examples

### Command example

    python3 app.py example_input.txt example_output.csv

### Input files syntax
    
    [{"bn": "AAAAAAA254AF", "bt": 1666792197, "n": "model", "vs": "test"}, {"n": "rssi", "u": "dBW", "v": -107}, {"n": "mac", "vs": "AAAAAAA254AF"}]
    [{"bn": "AAAAAAA254AF", "bt": 1666792197}, {"n": "connection_interface", "vs": "Ethernet"}]
    [{"bn": "AAAAAAA254AF", "bt": 1666792258, "n": "model", "vs": "test"}, {"n": "rssi", "u": "dBW", "v": -105}, {"n": "mac", "vs": "AAAAAAA254AF"}]
    [{"bn": "AAAAAAA254AF", "bt": 1666792258}, {"n": "connection_interface", "vs": "Ethernet"}]
    [{"bn": "AAAAAAA254AF", "bt": 1666792319, "n": "model", "vs": "test"}, {"n": "rssi", "u": "dBW", "v": -107}, {"n": "mac", "vs": "AAAAAAA254AF"}]
    [{"bn": "AAAAAAA254AF", "bt": 1666792319}, {"n": "connection_interface", "vs": "Ethernet"}]
    [{"bn": "AAAAAAA254AF", "bt": 1666792379, "n": "model", "vs": "test"}, {"n": "rssi", "u": "dBW", "v": -105}, {"n": "mac", "vs": "AAAAAAA254AF"}]
    [{"bn": "AAAAAAA254AF", "bt": 1666792379}, {"n": "connection_interface", "vs": "Ethernet"}]
    [{"bn": "AAAAAAA254AF", "bt": 1666792440, "n": "model", "vs": "test"}, {"n": "rssi", "u": "dBW", "v": -113}, {"n": "mac", "vs": "AAAAAAA254AF"}]
    [{"bn": "AAAAAAA254AF", "bt": 1666792440}, {"n": "connection_interface", "vs": "Ethernet"}]
