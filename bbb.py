import hashlib
import urllib.request
from xml.etree import ElementTree
import requests
from collections import defaultdict


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


def _etree_to_dict(t):
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(_etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v
                     for k, v in dd.items()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v)
                        for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
              d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d

def create_meeting(args):
    call = "create"
    api_url = _get_url(call,args)
    r = requests.get(api_url)
    root = ElementTree.fromstring(r.content)
    response = _etree_to_dict(root)
    return response



#  "createname=Test+Meeting&meetingID=abc123&attendeePW=111222&moderatorPW=333444"
#create_meeting({"name":"Test Meeting","meetingID":"abc123","attendeePW":"111222","moderatorPW":"333444"})
