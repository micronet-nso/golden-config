**Zero Touch Provisioning**.

this develop will help us to automate the configuration of day 0, without any human config access.


**Use Case Description**. 

For this particular use case, referring to the configuration of network services, when finishing adding the configuration of the equipment that is being managed in the web portal, this data must be sent to the orchestrator's methods so that it fulfills its function. , the data sent by the web part to the orchestrator, are necessary to carry out its activities until the team is enabled.

**Installation**.

+ before to run this python code, the NSO application must be installed.
+ then, you need to install all python dependecies

**Usage**

into the file "NSO_Services.py" in the method "get_platform" this have only one parameters that you need to pass it,
* platform   - device platform 

this method help us to identify what kind of plataform the device have.

into the file "NSO_Services.py" in the method "add_device" there are four parameters that you need to pass it,
* nso_socket - is the url where nso live
* hostname   - device hostname
* ipaddr     - device ip address 
* platform   - device platform 

into the file "NSO_Services.py" in the method "device_ssh_keys" there are two parameters that you need to pass it,
* nso_socket - is the url where nso live
* hostname   - device hostname

into the file "NSO_Services.py" in the method "device_sync_from" there are two parameters that you need to pass it,
* nso_socket - is the url where nso live
* hostname   - device hostname

into the file "NSO_Services.py" in the method "create_golden_config_service" there are six parameters that you need to pass it,
 
* nso_socket - is the url where nso live
* hostname   - device hostname
* ipaddr     - device ip address 
* platform   - device platform 
* service_name - device service name
* region       - region   which region does the device belong to 


Known issues

this only work with XE device platform.


https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/micronet-nso/golden-config


