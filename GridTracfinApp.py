import os
import argparse
import shutil

def build_app():
    print('Build GridTracfin App and deploy into Docker...')
    output_dir_name = 'output'
    docker_output_dir_name = os.path.join(output_dir_name, 'docker_output')
    docker_compose_dir = os.path.join(docker_output_dir_name, 'docker-compose')
    docker_deployment_dir_src = 'deployment'
    python_dir_src = os.path.join('server', 'app')
    python_dir_dest = os.path.join(docker_compose_dir, 'dockerfile', 'grid_tracfin_python', 'app')
    docker_compose_conf_file = os.path.join(docker_compose_dir, 'docker-compose.yml')
    
    # Create output directory if not exist
    if not os.path.exists(output_dir_name):
        os.makedirs(output_dir_name)

    # If Docker output directory exist, remove it.
    if os.path.exists(docker_output_dir_name):
        shutil.rmtree(docker_output_dir_name, )

    # Create docker output directory which will contains the image, Dockerfile, source code, we need to build the app and deploy it on Docker
    os.makedirs(docker_output_dir_name, exist_ok=True)

    # Copy the docker configuration (Image, docker-compose etc)
    shutil.copytree(docker_deployment_dir_src, docker_output_dir_name, dirs_exist_ok=True)

    # Copy the Python Source code
    shutil.copytree(python_dir_src, python_dir_dest, dirs_exist_ok=True)

    print('Stop docker compose')
    os.system('docker-compose -f ' + docker_compose_conf_file + ' down')

    # Remove existing Python container to rebuild a new one each time (KEEP for the moment but must be refactor in the future)
    docker_python_container_name = 'python-server'
    print('Remove existing python container: ' + docker_python_container_name)
    os.system('docker container rm ' + docker_python_container_name)

    # Remove existing Python image to rebuild a new one each time (KEEP for the moment but must be refactor in the future)
    docker_python_image = 'docker-compose-python-server'
    print('Remove existing python image: ' + docker_python_image)
    os.system('docker rmi ' + docker_python_image)

    print('Execute docker compose')
    os.system('docker-compose -f ' + docker_compose_conf_file + ' up')
### End def build_app()

FUNCTIONS_MAP = { 'build' : build_app }

parser = argparse.ArgumentParser(description="Grid Tracfin Builder",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("command", choices=FUNCTIONS_MAP.keys())
args = parser.parse_args()

## DEBUG purpose
#config = vars(args)
#print(config)

func = FUNCTIONS_MAP[args.command]
func()

