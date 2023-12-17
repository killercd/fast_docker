import docker

def docker_list(filter):
    client = docker.from_env()
    docker_list = []
    for container in  client.containers.list():
        if container.name.find(filter)>=0:
            docker_list.append(container)
    return docker_list


def docker_get(docker_id):
    client = docker.from_env()
    return client.containers.get(docker_id).attrs

def docker_stop(docker_id):
    client = docker.from_env()
    client.containers.get(docker_id).stop()
