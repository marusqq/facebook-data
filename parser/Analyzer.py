"""class for analysis"""

import parser.util as util
from parser.investigators import ActivityMessages
from parser.investigators.DataSizeInvestigator import DataSizeInvestigator
from parser.investigators import AdsInformation
from parser.investigators import AppsAndWebsitesOffOfFacebook

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


class TimePeriod:
    def __init__(self, path):
        self.path = path
        self.folder_name = path.stem
        self.start_date, self.end_date = self.read_dates_from_folder_name()
        self.current_data = None

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_name_from_dates(self):
        return str(self.get_start_date()) + '_' + str(self.get_end_date())

    def get_unzipped_size(self):
        size_in_bytes = util.get_directory_size(self.path)
        size_in_mb = util.convert_bytes_to_megabytes(size_in_bytes)
        return size_in_mb

    # format: oct25_2013-oct27_2013
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

    def get_name_from_dates(self):
        return str(self.get_earliest_date()) + '_' + str(self.get_latest_date())

    def get_earliest_date(self):
        return self.earliest_start_date

    def get_latest_date(self):
        return self.latest_end_date

    def get_unzipped_size(self):
        size_in_bytes = 0
        for path in self.paths:
            size_in_bytes = size_in_bytes + util.get_directory_size(path)
        size_in_mb = util.convert_bytes_to_megabytes(size_in_bytes)
        return size_in_mb


class Analyzer:
    def __init__(self, settings_file, ready_zips):
        self.settings_dict = None
        self.load_settings(settings_file)
        self.time_periods = []
        self.big_time_period = None
        self.create_time_periods(ready_zips)
        self.analysis_data = {}

    def start_analysis(self):
        # read stuff

        # TODO: if setting =>
        # TODO: also would be good to for setting.useTimePeriodDates or setting.useYearly but this is kinda impossible
        #       since we don't really the exact date of TimePeriods -> Years in data size

        # -----------------------------------------------------------
        # ----------------         SIZE (mb)         ----------------
        # -----------------------------------------------------------
        size_investigate = DataSizeInvestigator(self.time_periods, self.big_time_period)
        size_investigate.create_plots()
        size_investigate.add_to_report()
        # helpers below vvvv
        # print(size_investigate.investigated_period_data['periods'].sort_values(by=['size']).tail(5))
        # print(size_investigate.investigated_period_data['periods'].nlargest(n=5, columns='size'))
        #
        # print(size_investigate.investigated_period_data['periods'].sort_values(by=['size']).head(5))

        # -----------------------------------------------------------
        # ----------------     ACTIVITY_MESSAGES     ----------------
        # -----------------------------------------------------------

        # ------------------------------
        # ------- Group Interactions - always there
        # ------------------------------
        group_interactions_investigate = ActivityMessages.GroupInteractionsInvestigator(self.time_periods,
                                                                                        self.big_time_period)
        group_interactions_investigate.create_plots()
        group_interactions_investigate.add_to_report()
        # print(group_interactions_investigate.investigated_period_data['periods'])
        # ------------------------------
        # ------- People and Friends - optional
        # ------------------------------
        people_interactions_investigate = ActivityMessages.PeopleAndFriendsInvestigator(self.time_periods,
                                                                                        self.big_time_period)
        people_interactions_investigate.create_plots()
        people_interactions_investigate.add_to_report()
        # this is nothing interesting honestly

        # -----------------------------------------------------------
        # --------------    APPS_AND_WEBSITES_OFF_FB     ------------
        # -----------------------------------------------------------

        # ------------------------------
        # ------- Apps and Websites - always there
        # ------------------------------

        # apps_and_websites_investigate = AppsAndWebsitesOffOfFacebook.AppsAndWebsitesInvestigator(
        #     self.time_periods, self.big_time_period
        # )

        # ------------------------------
        # ------- Your Apps - always there
        # ------------------------------

        # ------------------------------
        # ------- Posts from Apps and Websites - old years
        # ------------------------------

        # ------------------------------
        # ------- Your Off Facebook Activity - later years (for me around 2019)
        # ------------------------------

        input()
        return 'wow such analysis'

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


            # find earliest start date and the latest end date
            time_period_start_date = time_period.get_start_date()
            time_period_end_date = time_period.get_end_date()

            if earliest_date is None or earliest_date > time_period_start_date:
                earliest_date = time_period_start_date

            if latest_date is None or latest_date < time_period_end_date:
                latest_date = time_period_end_date

        self.big_time_period = BigTimePeriod(
            paths=util.get_directories_in_directory(time_periods[0].parent),
            start_end_dates=[earliest_date, latest_date]
        )
