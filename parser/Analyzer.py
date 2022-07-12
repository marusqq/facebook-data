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

class TimePeriod:
    def __init__(self, path):
        self.path = path
        self.folder_name = path.stem
        self.start_date, self.end_date = self.read_dates_from_folder_name()

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def read_dates_from_folder_name(self):
        start_date_no_format = self.folder_name.split('-')[0]
        end_date_no_format = self.folder_name.split('-')[1]
        finished_dates = []
        for date in [start_date_no_format, end_date_no_format]:
            year = date.split('_')[-1]
            month = date[:3]
            day = date.split('_')[0][-2:]
            finished_date = str(year) + '-' + str(month) + '-' + str(day)
            finished_dates.append(util.get_datetime_from_string(finished_date))

        return finished_dates


class BigTimePeriod(TimePeriod):
    def __init__(self, paths, start_end_dates):
        self.paths = paths
        self.folder_names = []
        for path in self.paths:
            self.folder_names.append(path.stem)

        self.earliest_start_date = start_end_dates[0]
        self.latest_end_date = start_end_dates[1]


class Analyzer:
    def __init__(self, settings_file, ready_zips):
        self.settings_dict = None
        self.load_settings(settings_file)
        self.time_periods = []
        self.len_of_time_periods = 0
        self.create_time_periods(ready_zips)

    def start_analysis(self):
        print('anal ysis')

    def load_settings(self, settings_file):
        self.settings_dict = util.load_json_file(settings_file)

    def create_time_periods(self, ready_zips):
        time_periods = []
        for ready_zip in ready_zips:
            ready_folder = ready_zip.parent
            if ready_folder not in time_periods:
                time_periods.append(ready_folder)

        earliest_date = None
        latest_date = None

        for time_period_path in time_periods:
            time_period = TimePeriod(path=time_period_path)
            self.time_periods.append(time_period)
            self.len_of_time_periods = self.len_of_time_periods + 1

            # find earliest start date and the latest end date
            time_period_start_date = time_period.get_start_date()
            time_period_end_date = time_period.get_end_date()

            if earliest_date is None or earliest_date > time_period_start_date:
                earliest_date = time_period_start_date

            if latest_date is None or latest_date < time_period_end_date:
                latest_date = time_period_end_date

        big_time_period = BigTimePeriod(
            paths=util.get_directories_in_directory(time_periods[0].parent),
            start_end_dates=[earliest_date, latest_date]
        )

        time_periods.append(big_time_period)

        input()
