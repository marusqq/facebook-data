# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
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
        self._investigate()

        from pprint import pprint
        pprint(self.investigated_period_data['big_period'])
        df = pd.DataFrame(
            index=self.investigated_period_data['big_period'].keys(),
            data={'interactions': self.investigated_period_data['big_period'].values()}
        )

        print(df.nlargest(10, columns='interactions'))

    def create_plots(self):
        pass

    def add_to_report(self):
        pass

    def _investigate(self):
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

                if group_name in time_period_group_interactions.keys():
                    group_interaction_count = group_interaction_count + time_period_group_interactions[group_name]
                time_period_group_interactions[group_name] = group_interaction_count

                if group_name in all_time_group_interactions.keys():
                    group_interaction_count = group_interaction_count + all_time_group_interactions[group_name]
                all_time_group_interactions[group_name] = group_interaction_count

            self.investigated_period_data['periods'].append({
                time_period_name: time_period_group_interactions
            })

        self.investigated_period_data['big_period'] = all_time_group_interactions

                # input()
                # print()
            #     group
            #
            # for

            #
            # if 'entries' in group_interaction_json_data:
            #     print(group_interaction_json_data['entries'])
            #     input()

    def _look_for_group_interactions(self, time_periods):
        self.group_interaction_file_paths = {}
        for time_period in time_periods:
            file_path = None
            activity_messages_path = time_period.path / 'unzipped_data' / 'activity_messages'
            if util.check_if_directory(activity_messages_path):
                if util.check_if_file(activity_messages_path / 'group_interactions.json'):
                    file_path = activity_messages_path / 'group_interactions.json'

            self.group_interaction_file_paths[time_period.get_name_from_dates()] = file_path


class PeopleAndFriendsInvestigator:
    pass
