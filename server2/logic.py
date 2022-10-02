from flask import make_response
import sys
sys.path.insert(1, '/server2')
import text_response

def logic_response(json_file):
    if (json_file['serial'].isdecimal()):
        response=  make_response(text_response.Bad_Serial(), 200)

    elif(json_file['serial'].startswith("24-X")):
        response=  make_response(text_response.Upgrade(), 200)

    elif(json_file['serial'].startswith("36-X") or json_file['serial'].startswith("51-B")):
        if(json_file['indicator1']=="off" and json_file['indicator2']=="off" and json_file['indicator3']=="off"):
            response=  make_response(text_response.Turn_ON(), 200)
        elif(json_file['indicator1']=="on" and json_file['indicator2']=="on" and json_file['indicator3']=="on"):
            response=  make_response(text_response.OK(), 200)
        elif(json_file['indicator1']=="blinking"):
            if (json_file['serial'].startswith("51-B") or json_file['indicator3']=="blinking" or json_file['indicator2']=="blinking"):
                response=  make_response(text_response.Wait(), 200)
        elif(json_file['indicator3']=="blinking" and json_file['indicator2']=="blinking"):
            response=  make_response(text_response.Wait(), 200)
        elif(json_file['serial'].startswith("51-B")):
            if(json_file['indicator3']=="blinking" or json_file['indicator2']=="blinking"):
                response=  make_response(text_response.Wait(), 200)
            elif(json_file['indicator1']=="on" or json_file['indicator2']=="on" or json_file['indicator3']=="on"):
                response=  make_response(text_response.OK(), 200)
    else:
        response=  make_response(text_response.Unknown(), 200)
    return response