import hashlib
import urllib.request
from xml.etree import ElementTree as ET
import requests

_secret = "ILcrZOAJaesnC7hKzY2nfi7HGDx5IPFAH65BSFxEqE"
_url_path = "https://call.bendidi.me"

def _create_checksum(query_call):
    call = query_call + _secret
    hash_object = hashlib.sha1(call.encode('utf-8'))
    pbHash = hash_object.hexdigest()
    return pbHash





def _create_query(query_call,parameter_string):
    checksum = _create_checksum(query_call)
    final_query = parameter_string + "&checksum=" + checksum
    return final_query



def _create_api_url(call,final_query):
    api_url = _url_path + "/bigbluebutton/api/" + call + "?" + final_query
    return api_url



def _create_parameter_string(args):
    parameter_string = ""
    for key, value in args.items():
        value = value.replace(" ","+")
        parameter_string += key + "=" + value + "&"
    parameter_string = parameter_string[:-1]
    return parameter_string

def _get_url(call,args):
    parameter_string = _create_parameter_string(args)
    final_query = _create_query(call + parameter_string, parameter_string)
    api_url = _create_api_url(call,final_query)
    return api_url

def create_meeting(args):
    call = "create"
    api_url = _get_url(call,args)
    print(api_url + "\n\n")
    r = requests.get(api_url)
    root = ElementTree.fromstring(r.content)



#  "createname=Test+Meeting&meetingID=abc123&attendeePW=111222&moderatorPW=333444"
create_meeting({"name":"Test Meeting","meetingID":"abc123","attendeePW":"111222","moderatorPW":"333444"})
