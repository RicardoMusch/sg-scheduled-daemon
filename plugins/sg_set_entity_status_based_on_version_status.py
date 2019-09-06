app_version = "v0.1"


def log(msg):
    try:
        logger.debug(str(msg))
    except:
        print msg


####################################################################
"Get a Shotgun Connection"
try:
    import sgtk

    ## SHOTGUN CONTEXT
    current_engine = sgtk.platform.current_engine()
    current_context = current_engine.context
    logger = sgtk.platform.get_logger(__name__)

    try:
        log(" ")
        shotgun = self.parent.shotgun
    except:
        shotgun = shotgun
except:
    import os
    import sys

    log("Importing Shotgun API3")
    log(" ")
    shotgun_api3 = os.environ["SHOTGUN_API3"]
    sys.path.insert(0, shotgun_api3)
    import shotgun_api3

    SERVER_PATH = os.environ["SERVER_PATH"]
    SCRIPT_NAME = os.environ["SCRIPT_NAME"]
    SCRIPT_KEY = os.environ["SCRIPT_KEY"]

    shotgun = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)


log(" ")
log("########################### Shotgun Status Checker "+app_version+" ###############################")
log(" ")



#############################################################
## Set Entity Status to Final when Version is set to Final
#############################################################
log("Getting versions with 'fin' as status and setting the entity status to 'fin' if not already done")
versions = []
columns = [ "sg_status_list", "code", "entity" ]
filters = [ 
#['project', 'name_contains', "pipeline" ],
['sg_status_list', 'is', "fin" ],
]
versions = shotgun.find( 'Version', filters, columns )
#log(versions)

if versions != []:
    log(" ")
    log("Found 'fin' Versions:")
    for version in versions:
        log("- "+str(version.get("project"))+" - "+version.get("code"))

        columns = [ "sg_status_list" ]
        filters = [ 
        ['sg_status_list', 'is_not', "fin" ],
        ['id', 'is', version.get("entity").get("id") ],
        #['entity.Entity.sg_status_list', 'is not', "fin"] ## Not working?
        ]
        result = shotgun.find_one( version.get("entity").get("type") , filters, columns )
        
        if result != None:
            version_name = version.get("code")
            entity = version.get("entity")
            entity_type = version.get("entity").get("type")
            entity_name = version.get("entity").get("name")
        
            data = { 'sg_status_list': 'fin' }
            shotgun.update(version.get("entity").get("type"), version.get("entity").get("id"), data)
            msg = "Set Status of "+entity_type+" "+entity_name+" to Final because a version with Final Status was found"
            msg = str(msg)
            log(msg)

