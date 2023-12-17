from fastapi import FastAPI
from core.docker import docker_list as gdck_list, docker_get as gdck_get, docker_stop as gdck_stop

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/docker/containers/")
async def docker_list():
    ret_list = []
    
    for container in gdck_list(""):
        ret_list.append({"id":container.attrs["Id"], 
                                "name": container.name,
                                "status": container.attrs["State"]["Status"]})
    return ret_list    


@app.get("/docker/containers/{name}")
async def docker_list(docker_name: str):
    ret_list = []
    
    for container in gdck_list(docker_name):
        ret_list.append({"id":container.attrs["Id"], 
                                "name": container.name,
                                "status": container.attrs["State"]["Status"]})
    return ret_list




@app.get("/docker/container/{id}")
async def docker_get(docker_id: str):
    attrs = gdck_get(docker_id)
    return attrs


@app.get("/docker/container/stop/{id}")
async def docker_stop(docker_id: str):
    gdck_stop(docker_id)
    return {"message": "OK"}    
