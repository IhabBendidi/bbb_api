## Requirements :
The current API only supports Python 3. It does not currently support Python 2

## Python API Calls :


### Create a meeting :

`create_meeting` function helps to create a meeting.

The create call is idempotent: you can call it multiple times with the same parameters without side effects. This simplifies the logic for joining a user into a session as your application can always call create before returning the join URL to the user. This way, regardless of the order in which users join, the meeting will always exist when the user tries to join (the first create call actually creates the meeting; subsequent calls to create simply return SUCCESS).

The BigBlueButton server will automatically remove empty meetings that were created but have never had any users after a number of minutes specified by meetingExpireIfNoUserJoinedInMinutes defined in bigbluebutton.properties.

##### Input :

A dictionary

```
import bbb-api as b
b.create_meeting({"name":"Test Meeting","meetingID":"abc123","attendeePW":"111222","moderatorPW":"333444"})
```
