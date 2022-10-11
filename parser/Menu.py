"""class for menu workflow"""
import os

import parser.util as util
from parser.Reporter import ReporterPDF
from parser.logger import logger

from parser.DataUnzipper import DataUnzipper
from parser.Analyzer import Analyzer

from consolemenu import *
from consolemenu.items import *


class Menu:
    def menu(self, mode='main'):
        if mode == 'main':
            menu = ConsoleMenu("Main menu")
            start = FunctionItem(function=self.analysis, text="Start analyzing")
            settings = FunctionItem(function=self.menu, args=['analyzer_settings'], text="Settings")

            menu.append_item(start)
            menu.append_item(settings)
            menu.show()

        elif mode == 'analyzer_settings':
            menu = ConsoleMenu("Setup analyzer")
            menu.show()

        else:
            self.menu()

    def analysis(self):

        # Unzip files
        fb_data_path = os.getcwd() + '/data/'
        data_unzipper = DataUnzipper(path=fb_data_path)
        data_unzipper.unzip_files()

        # Read settings / anaylyse
        analyzer = Analyzer('settings.json', data_unzipper.get_ready_zips())
        analysed_data = analyzer.start_analysis()

        reporter = ReporterPDF(title='facebook_data')
        reporter.save_pdf()

        # # Write analysed data to report
        # # TODO: fix this one day
        # pdf = PDF()
        # pdf.set_title_to_pdf('Facebook data analysis')
        # pdf.set_author('Marius Pozniakovas')
        # pdf.print_chapter(1, 'File Sizes', 'settings.json')
        # pdf.print_chapter(2, 'Settings', 'settings.json')
        # pdf.output('/reports/report_4.pdf')
        # # pdf.save_pdf()
