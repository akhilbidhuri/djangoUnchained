import re
import json
import requests
from datetime import datetime
from userActivity.models import Users, ActivityPeriod
from django.core.management.base import BaseCommand, CommandError

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def get_datetime(datetime_str):
    old_format = '%b %d %Y %I:%M%p'
    new_format = '%Y-%m-%d %H:%M'
    new_datetime_str = datetime.strptime(datetime_str, old_format).strftime(new_format)
    return new_datetime_str

def populate_using_json(data):
    if 'ok' in data and 'members' in data:
        if type(data['members'])==list:
            for member in data['members']:
                try:
                    db_user, _ = Users.objects.get_or_create(id=member['id'])
                    db_user.real_name = member['real_name']
                    db_user.tz = member['tz']
                    db_user.save()
                    for activity in member['activity_periods']:
                        temp = ActivityPeriod.objects.create(user = db_user, start_time = get_datetime(activity['start_time']), end_time = get_datetime(activity['end_time']))
                        
                        temp.save()
                except Exception as e:
                    print('Exception : ', e)  
            return True
    return False


class Command(BaseCommand):
    help="Command to populate data base from a Data Source can be a URL or path to file."

    def add_arguments(self, parser):
        parser.add_argument('data_source', type=str)

    def handle(self, *args, **options):
        if 'data_source' not in options:
            print("Kindly Provide a Data Source a URL or Path to json file on system.")
            return
        data_source, data = options['data_source'], None
        if re.match(regex, data_source):
            print("URL Data Source")
            try:
                data = requests.get(data_source).json()
            except:
                print("Data not in JSON format, Kindly check the data source")
        else:
            print("File System Data Source")
            f = open(data_source, 'r')
            try:
                data = json.loads(f.read())
            except:
                print("Data not in JSON format, Kindly check the data source")
            f.close()
        #print(data)
        if populate_using_json(data):
                print('Validated and Inserted the Data into DB.')
        else:
            print('JSON not validated, Kindly check the data source')