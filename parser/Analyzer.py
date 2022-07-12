"""class for analysis"""

import parser.util as util

# activity_messages:
#       group_interactions.json TODO
#       people_and_friends.json ????

# ads_information:
#       advertisers_using_your_activity_or_information.json TODO
#       other_categories_used_to_reach_you TODO

# apps_and_websites_off_of_facebook
#       apps_and_websites.json TODO
#       your_apps.json TODO

# bug_bounty
#       no-data.txt TODO

# comments_and_reactions
#       comments.json TODO
#       posts_and_comments.json TODO

# communities
#       no-data.txt here TODO

# events
#       event_invitations.json TODO
#       your_event_responses.json TODO

# facebook_accounts_center
#       accounts_center.json TODO

# facebook_assistant

# facebook_gaming

# facebook_marketplace

# facebook_payments

# facebook_portal

# friends_and_followers

# fundraisers

# groups

# your_interactions_on_facebook

# your_places

# your_problem_reports

# your_topics

# live_audio_rooms

# location

# messages !

# music_recommendations

# notifications

# other_activity

# other_logged_information

# other_personal_information

# pages

# polls

# posts

# preferences

# privacy_checkup

# profile_information

# reviews

# saved_items_and_collections

# search

# security_and_login_information

# short_videos

# spark_ar

# stories

from parser.logger import logger


# [WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/aug05_2009-may22-2013/facebook-pozniakovasmarius (1).zip'),
#  WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2013-may22-2015/facebook-pozniakovasmarius (2).zip'),
#  WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2015-may22_2017/facebook-pozniakovasmarius (1).zip'),
#  WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2015-may22_2017/facebook-pozniakovasmarius (2).zip'),
#  WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2015-may22_2017/facebook-pozniakovasmarius.zip'),
#  WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2017-may22_2019/facebook-pozniakovasmarius.zip'),
#  WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2019-may22_2020/facebook-pozniakovasmarius (3).zip'),
#  WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2019-may22_2020/facebook-pozniakovasmarius (4).zip'),
#  WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2019-may22_2020/facebook-pozniakovasmarius (5).zip'),
#  WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2019-may22_2020/facebook-pozniakovasmarius (6).zip'),
#  WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2020-may22_2021/facebook-pozniakovasmarius (1).zip'),
#  WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2020-may22_2021/facebook-pozniakovasmarius (2).zip'),
#  WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2020-may22_2021/facebook-pozniakovasmarius.zip'),
#  WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2021-may22_2022/facebook-pozniakovasmarius.zip'),
#  WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2021-may22_2022/facebook-pozniakovasmarius1.zip'),
#  WindowsPath('C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2022-jul09_2022/mpozniakovas.zip')]


class TimePeriod:
    def __init__(self, path):
        self.path = path
        self.folder_name = path.stem
        self.start_date, self.end_date = self.read_dates_from_folder_name()

    def read_dates_from_folder_name(self):
        start_date_no_format = self.folder_name.split('-')[0]
        end_date_no_format = self.folder_name.split('-')[1]
        finished_dates = []
        for date in [start_date_no_format, end_date_no_format]:
            year = date.split('_')[-1]
            month = date[:3]
            day = date.split('_')[0][-2:]
            finished_date = str(year) + '-' + str(month) + '-' + str(day)
            finished_dates.append(finished_date)

        return finished_dates


class Analyzer:
    def __init__(self, settings_file, ready_zips):
        self.settings_dict = None
        self.load_settings(settings_file)
        self.time_periods = []
        self.create_time_periods(ready_zips)

    def start_analysis(self):
        print('anal ysis')

    def load_settings(self, settings_file):
        self.settings_dict = util.load_json_file(settings_file)

    def create_time_periods(self, ready_zips):
        # get only unique
        time_periods = []
        for ready_zip in ready_zips:
            ready_folder = ready_zip.parent
            if ready_folder not in time_periods:
                time_periods.append(ready_folder)

        for time_period_path in time_periods:
            time_period = TimePeriod(path=time_period_path)
            self.time_periods.append(time_period)

        # TODO big period for all periods as well
        #

        input()
