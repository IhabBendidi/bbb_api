## Requirements :
The current API only supports Python 3. It does not currently support Python 2

## Python API Calls :


### Create a meeting :

`create_meeting` function helps to create a meeting.

The create call is idempotent: you can call it multiple times with the same parameters without side effects. This simplifies the logic for joining a user into a session as your application can always call create before returning the join URL to the user. This way, regardless of the order in which users join, the meeting will always exist when the user tries to join (the first create call actually creates the meeting; subsequent calls to create simply return SUCCESS).

The BigBlueButton server will automatically remove empty meetings that were created but have never had any users after a number of minutes specified by meetingExpireIfNoUserJoinedInMinutes defined in bigbluebutton.properties.

##### Input :

A dictionary variable containing all necessary values or optional values needed for the api call. A more comprehensive list of those needed variables can be found [here](https://docs.bigbluebutton.org/dev/api.html#create).

##### Example :

```
import bbb_api as b
b.create_meeting({"name":"Test Meeting","meetingID":"abc123","attendeePW":"111222","moderatorPW":"333444"})
```


##### Output :

A dictionary with a response key of SUCCESS or Failure, as well as information about the created meeting. If the meeting is already created, it is still a success, but it does not create a new one.

```
{'response': {'returncode': 'SUCCESS', 'meetingID': 'abc123', 'internalMeetingID': '6367c48dd193d56ea7b0baad25b19455e529f5ee-1586581110019', 'parentMeetingID': 'bbb-none', 'attendeePW': '111222', 'moderatorPW': '333444', 'createTime': '1586581110019', 'voiceBridge': '15938', 'dialNumber': '613-555-1234', 'createDate': 'Sat Apr 11 04:58:30 UTC 2020', 'hasUserJoined': 'false', 'duration': '0', 'hasBeenForciblyEnded': 'false', 'messageKey': 'duplicateWarning', 'message': 'This conference was already in existence and may currently be in progress.'}}

```


### Join a meeting :

`join_meeting` function helps to join an existing meeting.


##### Input :

A dictionary variable containing all necessary values or optional values needed for the api call. A more comprehensive list of those needed variables can be found [here](https://docs.bigbluebutton.org/dev/api.html#join).

##### Example :

```
import bbb_api as b
b.join_meeting({"fullName":"Test Meeting","meetingID":"abc123","password":"333444","clientURL":"ihabURL"})
```


##### Output :

A url that redirects into the room of the meeting.

```
https://call.bendidi.me/bigbluebutton/api/join?fullName=Test+Meeting&meetingID=abc1234&password=333444&clientURL=ihabURL&checksum=fa78afd0c6e592c931159c7ca310c1aabc2bd85f

```

### Check if a meeting is running :

`is_meeting_running` function helps to check whether there is an already running meeting. A meeting is only considered running if it has at least one user already joined.


##### Input :

A dictionary variable containing the meeting id.

##### Example :

```
import bbb_api as b
b.is_meeting_running({"meetingID":"abc123"})
```


##### Output :

A response telling if the meeting is running or not. A meeting is only considered running if it has at least one user already joined.

```
{'response': {'returncode': 'SUCCESS', 'running': 'true'}}

```
