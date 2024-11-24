import os
import argparse
import shutil

OUTPUT_DIR_NAME = 'output'
DOCKER_OUTPUT_DIR_NAME = os.path.join(OUTPUT_DIR_NAME, 'docker_output')
DOCKER_COMPOSE_DIR = os.path.join(DOCKER_OUTPUT_DIR_NAME, 'docker-compose')
GRID_TRACFIN_PYTHON_DIR = os.path.join(DOCKER_COMPOSE_DIR, 'dockerfile', 'grid_tracfin_python')
POSTGRES_DIR = os.path.join(DOCKER_COMPOSE_DIR, 'dockerfile', 'postgres')
DOCKER_COMPOSE_CONF_FILE = os.path.join(DOCKER_COMPOSE_DIR, 'docker-compose.yml')

def stop_containers():
    print('Stop docker compose')
    os.system('docker-compose -f ' + DOCKER_COMPOSE_CONF_FILE + ' down')
# END def stop_containers()

def start_containers():
    print('Execute docker compose')
    os.system('docker-compose -f ' + DOCKER_COMPOSE_CONF_FILE + ' up')
# END def start_containers()

def copy_deployment_directory_to_output():
    docker_deployment_dir_src = 'deployment'

    # If Docker output directory exist, remove it.
    if os.path.exists(DOCKER_OUTPUT_DIR_NAME):
        shutil.rmtree(DOCKER_OUTPUT_DIR_NAME)

    # Create docker output directory which will contains the image, Dockerfile, source code, we need to build the app and deploy it on Docker
    os.makedirs(DOCKER_OUTPUT_DIR_NAME, exist_ok=True)

    # Copy the docker configuration (Image, docker-compose etc)
    shutil.copytree(docker_deployment_dir_src, DOCKER_OUTPUT_DIR_NAME, dirs_exist_ok=True)
# END def copy_deployment_directory_to_output()

def copy_app_config_to_output():
    app_config_dir_path_src =  os.path.join('server', 'config')
    app_config_dir_path_dest =  os.path.join(GRID_TRACFIN_PYTHON_DIR, 'config') 

    # Copy config directory to output directory
    shutil.copytree(app_config_dir_path_src, app_config_dir_path_dest, dirs_exist_ok=True)
# END def copy_app_config_to_output()

def prepare_python_part():
    python_dir_src = os.path.join('server', 'app')    
    python_dir_dest = os.path.join(GRID_TRACFIN_PYTHON_DIR, 'app')

    # Copy the Python Source code
    shutil.copytree(python_dir_src, python_dir_dest, dirs_exist_ok=True)

    # Remove existing Python image to rebuild a new one each time (KEEP for the moment but must be refactor in the future)
    docker_python_image = 'grid_tracfin_project-python-server'
    print('Remove existing python image: ' + docker_python_image)
    os.system('docker rmi ' + docker_python_image)
# END def prepare_python_part()

def prepare_database_part():
    database_init_path_src = os.path.join('server', 'db')    
    database_init_path_dest = os.path.join(POSTGRES_DIR, 'db')

    # Copy the Python Source code
    os.makedirs(database_init_path_dest, exist_ok=True)
    shutil.copytree(database_init_path_src, database_init_path_dest, dirs_exist_ok=True)

    # Remove existing Python image to rebuild a new one each time (KEEP for the moment but must be refactor in the future)
    docker_database_image = 'grid_tracfin_project-postgres'
    print('Remove existing python image: ' + docker_database_image)
    os.system('docker rmi ' + docker_database_image)
# END def prepare_database_part()

####################
 ## MAIN SCRIPTS ##
####################

def install_dev_env():
    # Python requirements
    os.system('pip install pipreqs')
# END def def install_dev_env()

def generate_python_requirements():
    os.system('pipreqs ' + os.path.join('server', 'app'))
# END def generate_python_requirements()

def build_app():
    print('Check if Docker is Started')
    cmd_result = os.system('docker ps')
    if cmd_result != 0:
        print('Docker is Not Running: Stop the task => Start Docker application before running this task.')
        exit()

    stop_containers()

    print('Build GridTracfin App and deploy into Docker...')
    # Create output directory if not exist
    if not os.path.exists(OUTPUT_DIR_NAME):
        os.makedirs(OUTPUT_DIR_NAME)
 
    copy_deployment_directory_to_output()
    copy_app_config_to_output()
    prepare_database_part()
    prepare_python_part()

    start_containers()
### End def build_app()

FUNCTIONS_MAP = { 'build_and_deploy' : build_app, 'gpr': generate_python_requirements, 'install_dev_env': install_dev_env }

parser = argparse.ArgumentParser(description="Grid Tracfin Builder",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('command', choices=FUNCTIONS_MAP.keys())
args = parser.parse_args()

## DEBUG purpose
#config = vars(args)
#print(config)

func = FUNCTIONS_MAP[args.command]
func()

