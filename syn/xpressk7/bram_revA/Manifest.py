# To list file
# ls -1 | xargs -I % echo \"%\",

modules = {
"local" : ["../../../rtl","../../../ip-cores"],
}


files = [
"top_level.vhd",
"xpressk7.xdc",
]

library = "work"


target = "xilinx" 
action = "synthesis" 

syn_device = "xc7k160" 
syn_grade = "-2" 
syn_package = "tfbg676" 
syn_top = "top_level" 
syn_project = "yarr"
syn_tool = "vivado"
