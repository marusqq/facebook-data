# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
"""base investigator class"""

from parser import util
import pandas as pd


class Investigator:
    def __init__(self, time_periods, big_time_period, category_name, data_file_name):
        self.investigated_period_data = {
            'periods': [],
            'big_period': {},
            'stats': {}
        }

        self._look_for_files(time_periods, category_name, data_file_name)
        self._parse_group_interactions()
        self._investigate()

    def _look_for_files(self, time_periods, category_name, data_file_name):
        self.file_paths = {}
        for time_period in time_periods:
            file_path = None
            activity_messages_path = time_period.path / 'unzipped_data' / category_name
            if util.check_if_directory(activity_messages_path):
                if util.check_if_file(activity_messages_path / data_file_name):
                    file_path = activity_messages_path / data_file_name

            if file_path:
                self.file_paths[time_period.get_name_from_dates()] = file_path

    def _investigate(self):
        file_sizes = []
        file_size_in_mbs_per_day = []
        time_period_dates = []

        for time_period in self.time_periods:
            size_of_time_period = time_period.get_unzipped_size()
            time_period_time = time_period.get_name_from_dates()

            period_length_in_days = util.get_difference_between_datetimes(
                time_period.get_end_date(),
                time_period.get_start_date(),
                interval='days'
            )
            time_period_mbs_per_day = round(size_of_time_period / period_length_in_days, 3)

            time_period_dates.append(time_period_time)
            file_size_in_mbs_per_day.append(time_period_mbs_per_day)
            file_sizes.append(size_of_time_period)

        file_sizes_df_only = pd.DataFrame({'size': file_sizes}, index=time_period_dates)
        file_size_in_mbs_per_day_only = pd.DataFrame(
            {'size_per_day': file_size_in_mbs_per_day}, index=time_period_dates)

        self.investigated_period_data['periods'] = file_sizes_df_only.join(file_size_in_mbs_per_day_only)

        big_period_size = self.big_time_period.get_unzipped_size()
        big_period_length_in_days = util.get_difference_between_datetimes(
            self.big_time_period.get_latest_date(),
            self.big_time_period.get_earliest_date(),
            interval='days'
        )

        mbs_per_day_big_period = round(big_period_size / big_period_length_in_days, 3)
        mbs_per_year_big_period = round(mbs_per_day_big_period / 365, 3)

        big_period_df = pd.DataFrame({
            'size': self.big_time_period.get_unzipped_size(),
            'size_per_day': mbs_per_day_big_period,
            'size_per_year': mbs_per_year_big_period
        },
            index=[self.big_time_period.get_name_from_dates()])

        self.investigated_period_data['big_period'] = big_period_df

        return self.investigated_period_data

    def create_plots(self):
        # TODO:
        print('bim bam plot created')

    def add_to_report(self):
        # TODO
        print('bim bam added to report')
