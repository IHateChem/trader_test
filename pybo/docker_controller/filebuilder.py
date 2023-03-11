import os
import subprocess
from datetime import datetime
import docker
def get_args(args: dict) -> list[str]:
    arg_list = ['--id', args['id'], '--cpu', str(args['cpu']), '--memory', str(args['memory']), '--gpu', str(args['gpu']), '--mode', args['mode'], '--tickers', args['ticker'], '--net', args['net'], '--backend', args['backend'], '--start_date', args['start_date'], '--end_date', args['end_date'], '--lr', str(args['lr']), '--balance', str(args['balance'])]
    if args['model']:
        arg_list += ['--model', args['model']]
    return arg_list

def dockerfile_builder(args: dict):
    user_id = args.get(id)
    BASE = 'C:/users/이석우/proejcts' #BASE = '/home/fmsoft/project/trader_test'
    src = BASE +'/app/trader_test/file/basefile'
    BASEDIR = BASE + f'/app/trader_test/'
    if not os.path.exists(BASEDIR):
        os.makedirs(BASEDIR)
    dst = BASEDIR + '/Dockerfile'
    f = open(src, "r")
    lines = "\n".join(f.readlines())
    lines = lines.replace("<netname>", f"{args.get('net')}.py", 2)
    if args["model"]:
        lines = lines.replace("##", "")
        lines = lines.replace("<modelname>", f"{args.get('model')}", 2)
    args["args"] = get_args(args)
    lines = lines.replace("<args>", '", "'.join(get_args(args)))
    f.close()
    f = open(dst, "w")
    f.write(lines)
    f.close()


    
def container_builder(args: dict):
    today = datetime.today().strftime("%Y%m%d")
    BASE = 'C:/users/이석우/proejcts'#BASE = '/home/fmsoft/project/trader_test'
    os.chdir(BASE+"/app/trader_test/")
    try:
        client = docker.from_env()
    except docker.errors.DockerException:
        print("Docker daemmon is not running.")
        raise(docker.errors.DockerException)
    # 이미지 목록 가져오기
    images = client.images.list()
    # 이미지 이름 출력
    for image in images:
        if image.tags and f"{args['id']}_image_{today}" in image.tags[0]:
            for container in client.containers.list(all= True):
                if args["id"]+"_"+"container" in container.name:
                    container.stop()
                    container.remove()
                    break
            client.images.remove(f"{args['id']}_image_{today}:latest")
            break
    subprocess.run(f"docker build -t {args['id']}_image_{today} .", shell=True)
    subprocess.run(f"docker run -it --rm -p 80:8000 --memory {args['memory']}m --cpus {args['cpu']} --name {args['id']}_container_{today} {args['id']}_image_{today}", shell=True)



