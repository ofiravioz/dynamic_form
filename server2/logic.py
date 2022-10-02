from flask import make_response
import sys
sys.path.insert(1, '/server2')
import re
import text_response

def logic_response(json_file):
    reObj = re.compile('indicator')
    off=0
    on=0
    blinking=0
    count=0
    for key in json_file.keys():
        if(reObj.match(key)):
            if(json_file[key]=='off'):
                off+=1
            elif(json_file[key]=='on'):
                on+=1
            elif(json_file[key]=='blinking'):
                blinking+=1
            count+=1

    if (json_file['serial'].isdecimal()):
        response=  make_response(text_response.Bad_Serial(), 200)

    elif(json_file['serial'].startswith("24-X")):
        response=  make_response(text_response.Upgrade(), 200)

    elif(json_file['serial'].startswith("36-X")):
        if(off==count):
            response=  make_response(text_response.Turn_ON(), 200)
        elif(on==count):
            response=  make_response(text_response.OK(), 200)
        elif(blinking>=2):
            response=  make_response(text_response.Wait(), 200)
    elif(json_file['serial'].startswith("51-B")):
        if(off==count):
            response=  make_response(text_response.Turn_ON(), 200)
        elif(blinking>=1):
            response=  make_response(text_response.Wait(), 200)
        elif(on<=1):
            response=  make_response(text_response.OK(), 200)
    else:
        response=  make_response(text_response.Unknown(), 200)
    return response