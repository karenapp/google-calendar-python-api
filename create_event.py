from datetime import datetime, timedelta
from cal_setup import get_calendar_service


def main():
    # creates one hour event tomorrow 10 AM IST
    service = get_calendar_service()

    d = datetime.now().date()
    tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
    start = tomorrow.isoformat()
    end = (tomorrow + timedelta(hours=1)).isoformat()

    event_result = service.events().insert(calendarId='primary',
        body={ 
            "summary": 'Automating calendar', 
            "description": 'This is a tutorial example of automating google calendar with python',
            "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'}, 
            "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
        }
    ).execute()

    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
    main()
