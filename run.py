import output_csv as o, navigate_url as n, read_arguments as r                 

args=r.read_arguments()
data=n.navigate_url(args[0],args[1],args[2])
o.output_csv(data[0],data[1])
