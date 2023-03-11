from docker_controller.argv_parser import first_parser
from docker_controller.filebuilder import dockerfile_builder
args = first_parser()
print(args.model)
dockerfile_builder(args)