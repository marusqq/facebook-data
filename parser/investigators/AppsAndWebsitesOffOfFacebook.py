# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"

from parser.logger import logger
import pandas as pd

"""class used to find, parse and analyze AppsAndWebsitesOffOfFacebook 
    - Apps and Websites - always
    - Your apps - always
    - Posts from apps and websites - old data
    - Your Off Facebook Activity - new data    
"""

class YourOffFacebookActivity:
    def __init__(self, time_periods, big_period):
        self.investigated_period_data = {
            'periods': [],
            'big_period': {},
            'stats': {}
        }

        self._look_for_(time_periods)
        self._parse_group_interactions()

        df = pd.DataFrame(
            index=self.investigated_period_data['big_period'].keys(),
            data={'interactions': self.investigated_period_data['big_period'].values()}
        )

    # print(df.nlargest(10, columns='interactions'))


class AppsAndWebsitesInvestigator:
    def __init__(self, time_periods, big_period):
        self.investigated_period_data = {
            'periods': [],
            'big_period': {},
            'stats': {}
        }

        self._look_for_apps_and_websites(time_periods)
        self._parse_group_interactions()

        df = pd.DataFrame(
            index=self.investigated_period_data['big_period'].keys(),
            data={'interactions': self.investigated_period_data['big_period'].values()}
        )

        # print(df.nlargest(10, columns='interactions'))


class OffFacebookActivity:
    def __init__(self, time_periods, big_period):