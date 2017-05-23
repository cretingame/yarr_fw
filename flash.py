import os
import subprocess

project_path = os.getcwd()

file_list = os.listdir(project_path)

# TDO create the file if doesn't exist
script_file = open('flash.tcl', 'r+')

			

script_file.write(
"######################################################\n" +
"# Generated file to flash the program RAM\n" +
"######################################################\n" +
"\n\n" + 
"#Run flash.py to generate this file\n\n")

bit_file_exist = False

for file in file_list:
	if (file.endswith(".bit")):
		bit_file =  os.path.join(project_path + "/", file)
		bit_file_exist = True

if (bit_file_exist):
	cmd0 = "open_hw\n"
	cmd1 = "connect_hw_server -url localhost:3121\n"
	cmd2 = "current_hw_target [get_hw_targets */xilinx_tcf/Xilinx/000013b363cb01]\n"
	cmd3 = "set_property PARAM.FREQUENCY 6000000 [get_hw_targets */xilinx_tcf/Xilinx/000013b363cb01]\n"
	cmd4 = "open_hw_target\n"
	cmd5 = "set_property PROGRAM.FILE {" + bit_file + "} [lindex [get_hw_devices] 1]\n"
	cmd6 = "program_hw_devices [lindex [get_hw_devices] 1]"
	print cmd0 + cmd1 + cmd2 + cmd3 + cmd4 + cmd5 + cmd6 + "\n"
	script_file.write(cmd0 + cmd1 + cmd2 + cmd3 + cmd4 + cmd5 + cmd6 + "\n")
	#subprocess.call(["vivado", "-mode batch -source " + "flash.tcl"])
	os.system("vivado -mode batch -source " + "flash.tcl")
else:
	print "No bit file found !\n"
