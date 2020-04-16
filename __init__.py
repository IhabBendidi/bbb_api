import bbb_api.bbb as b

def create_meeting(args):
    return b.create_meeting(args)

def join_meeting(args):
    return b.join_meeting(args)

def is_meeting_running(args):
    return b.is_meeting_running(args)

def end_meeting(args):
    return b.end_meeting(args)

def get_meeting_info(args):
    return b.get_meeting_info(args)

def get_meetings(args):
    return b.get_meetings(args)
