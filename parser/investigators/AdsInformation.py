# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"

from parser.logger import logger

"""class used to find, parse and analyze ActivityMessages (GroupInteractions & PeopleAndFriends)"""

from parser import util
import pandas as pd


def convert_string_of_times_to_integer(times_string):
    number = times_string.split('time')[0].replace(' ', '').replace(',', '')
    try:
        int_number = int(number)
    except:
        int_number = None

    return int_number


class GroupInteractionsInvestigator:
    def __init__(self, time_periods, big_period):

        self.investigated_period_data = {
            'periods': [],
            'big_period': {},
            'stats': {}
        }

        self._look_for_group_interactions(time_periods)
        self._parse_group_interactions()

        df = pd.DataFrame(
            index=self.investigated_period_data['big_period'].keys(),
            data={'interactions': self.investigated_period_data['big_period'].values()}
        )

        # print(df.nlargest(10, columns='interactions'))

    def create_plots(self):
        pass

    def add_to_report(self):
        pass

    def _parse_group_interactions(self):
        all_time_group_interactions = {}
        for time_period_name, group_interaction_json in self.group_interaction_file_paths.items():
            time_period_group_interactions = {}

            group_interaction_json_data = util.load_json_file(group_interaction_json)
            if 'group_interactions_v2' not in group_interaction_json_data.keys():
                continue

            group_interaction_json_data_v2 = group_interaction_json_data['group_interactions_v2']

            if 'entries' not in group_interaction_json_data_v2[0].keys():
                continue

            group_interaction_json_data_v2_entries = group_interaction_json_data_v2[0]['entries']
            for entry in group_interaction_json_data_v2_entries:
                if 'data' not in entry.keys():
                    continue
                data = entry['data']
                group_name = util.get_ascii_string(data['name'])
                group_interaction_count = convert_string_of_times_to_integer(data['value'])

                if group_name not in time_period_group_interactions.keys():
                    time_period_group_interactions[group_name] = group_interaction_count

                if group_name not in all_time_group_interactions.keys():
                    all_time_group_interactions[group_name] = group_interaction_count

            self.investigated_period_data['periods'].append({
                time_period_name: time_period_group_interactions
            })

        self.investigated_period_data['big_period'] = all_time_group_interactions

    def _look_for_group_interactions(self, time_periods):
        self.group_interaction_file_paths = {}
        for time_period in time_periods:
            file_path = None
            activity_messages_path = time_period.path / 'unzipped_data' / 'activity_messages'
            if util.check_if_directory(activity_messages_path):
                if util.check_if_file(activity_messages_path / 'group_interactions.json'):
                    file_path = activity_messages_path / 'group_interactions.json'

            if file_path:
                self.group_interaction_file_paths[time_period.get_name_from_dates()] = file_path


class PeopleAndFriendsInvestigator:
    def __init__(self, time_periods, big_period):
        self.investigated_period_data = {
            'periods': [],
            'big_period': {},
            'stats': {}
        }

        self._look_for_people_and_friends_interactions(time_periods)
        self._parse_people_and_friends_interactions()

        df_people_names = []
        df_interactions = []
        for key, value in self.investigated_period_data['big_period'].items():
            df_people_names.append(key)
            person_interactions = self.investigated_period_data['big_period'][key]['interactions']
            if person_interactions == 1:
                logger.info(key)
            df_interactions.append(person_interactions)

        df = pd.DataFrame(
            index=df_people_names,
            data={'interactions': df_interactions}
        )

        print(df.nlargest(10, columns='interactions'))

    def _look_for_people_and_friends_interactions(self, time_periods):
        self.people_and_friend_interaction_file_paths = {}
        for time_period in time_periods:
            file_path = None
            activity_messages_path = time_period.path / 'unzipped_data' / 'activity_messages'
            if util.check_if_directory(activity_messages_path):
                if util.check_if_file(activity_messages_path / 'people_and_friends.json'):
                    file_path = activity_messages_path / 'people_and_friends.json'
            if file_path:
                self.people_and_friend_interaction_file_paths[time_period.get_name_from_dates()] = file_path

    def _parse_people_and_friends_interactions(self):
        all_time_people_and_friends_interactions = {
        }
        for time_period_name, people_and_friends_interaction_json in \
                self.people_and_friend_interaction_file_paths.items():
            time_period_people_and_friends_interactions = {}

            people_and_friends_interaction_json_data = util.load_json_file(people_and_friends_interaction_json)
            if 'people_interactions_v2' not in people_and_friends_interaction_json_data.keys():
                continue

            people_and_friends_interaction_json_data_v2 = \
                people_and_friends_interaction_json_data['people_interactions_v2']

            if 'entries' not in people_and_friends_interaction_json_data_v2[0].keys():
                continue

            people_and_friends_interaction_json_data_v2_entries = \
                people_and_friends_interaction_json_data_v2[0]['entries']
            for entry in people_and_friends_interaction_json_data_v2_entries:
                if 'data' not in entry.keys() or 'timestamp' not in entry.keys():
                    continue
                time = util.get_datetime_from_timestamp(entry['timestamp'])
                data = entry['data']
                person_name = util.get_ascii_string(data['name'])

                if person_name not in time_period_people_and_friends_interactions.keys():
                    time_period_people_and_friends_interactions[person_name] = {
                        "interactions": 0,
                        "interaction_dates": []
                    }

                time_period_people_and_friends_interactions[person_name]['interactions'] = \
                    time_period_people_and_friends_interactions[person_name]['interactions'] + 1
                time_period_people_and_friends_interactions[person_name]['interaction_dates'].append(time)

                if person_name not in all_time_people_and_friends_interactions.keys():
                    all_time_people_and_friends_interactions[person_name] = {
                        "interactions": 0,
                        "interaction_dates": []
                    }
                else:
                    logger.info('repeat? not unique')

                all_time_people_and_friends_interactions[person_name]['interactions'] = \
                    all_time_people_and_friends_interactions[person_name]['interactions'] + 1
                all_time_people_and_friends_interactions[person_name]['interaction_dates'].append(time)

            self.investigated_period_data['periods'].append({
                time_period_name: time_period_people_and_friends_interactions
            })

        self.investigated_period_data['big_period'] = all_time_people_and_friends_interactions

    def create_plots(self):
        pass

    def add_to_report(self):
        pass
