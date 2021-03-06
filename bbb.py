import hashlib
import urllib.request
from xml.etree import ElementTree
import requests
from collections import defaultdict


_secret = "tyQFjQsvU32tJtzMw8iWU7dqh5a2djzChi7WEDBGs"
_url_path = "https://live.bendidi.me"

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

def join_meeting(args):
    call = "join"
    api_url = _get_url(call,args)
    return api_url


def is_meeting_running(args):
    call = "isMeetingRunning"
    api_url = _get_url(call,args)
    r = requests.get(api_url)
    root = ElementTree.fromstring(r.content)
    response = _etree_to_dict(root)
    return response

def end_meeting(args):
    call = "end"
    api_url = _get_url(call,args)
    r = requests.get(api_url)
    root = ElementTree.fromstring(r.content)
    response = _etree_to_dict(root)
    return response

def get_meeting_info(args):
    call = "getMeetingInfo"
    api_url = _get_url(call,args)
    r = requests.get(api_url)
    root = ElementTree.fromstring(r.content)
    response = _etree_to_dict(root)
    return response

def get_meetings(args):
    call = "getMeetings"
    api_url = _get_url(call,args)
    r = requests.get(api_url)
    root = ElementTree.fromstring(r.content)
    response = _etree_to_dict(root)
    return response

def get_recordings(args):
    call = "getRecordings"
    api_url = _get_url(call,args)
    r = requests.get(api_url)
    root = ElementTree.fromstring(r.content)
    response = _etree_to_dict(root)
    return response

def publish_recordings(args):
    call = "publishRecordings"
    api_url = _get_url(call,args)
    r = requests.get(api_url)
    root = ElementTree.fromstring(r.content)
    response = _etree_to_dict(root)
    return response

def delete_recordings(args):
    call = "deleteRecordings"
    api_url = _get_url(call,args)
    r = requests.get(api_url)
    root = ElementTree.fromstring(r.content)
    response = _etree_to_dict(root)
    return response

def update_recordings(args):
    call = "updateRecordings"
    api_url = _get_url(call,args)
    r = requests.get(api_url)
    root = ElementTree.fromstring(r.content)
    response = _etree_to_dict(root)
    return response
