#!/usr/bin/env python
"""
    Title:          start_page_gen.py
    Creation Date:  21/12/2014
    Dscription:     Start page generator

"""

# Standard libraries
import unittest
import sys
import os
import argparse
import re
import random
import subprocess
import getpass

# Additional libraries
# FIXME: Move all used filehelp functions here
import filehelp

###############################################################################
# Helping functions
###############################################################################


def foo(bar):
    return bar

###############################################################################
# Start Class
###############################################################################


class Start:
    """ Start representation """
    SEARCH_H = 45
    INPUT_SZ = 30
    LOGO_W = 65
    LOGO_H = 30
    SUBM_W = 100
    OUT = "start.html"

    def __init__(self, arg_str=""):
        """ Default constructor """

    def get_form_str(self, title, input_name, url, logo_url, hidden={}):
        """ Generate Input form HTML code """
        comment = "<!-- " + title + " -->"
        search_h = (
            "<table width=100% height=" + str(self.SEARCH_H) + ">" +
            "<tr><td align=center>")
        form_h = (
            "<form name=\"" + title + "\"" +
            " style=\"margin: 0\" method=GET" +
            " action=\"" + url + "\"><table><tr><td>")
        input_hidden = []
        for (name, value) in hidden.items():
            input_hidden.append(
                "<input type=hidden name=" + name + " value=" + value + ">")
        logo_img = (
            "<img src=\"" + logo_url + "\"" +
            " align=middle border=0 width=" + str(self.LOGO_W) +
            " height=" + str(self.LOGO_H) + "/>")
        input_logo = (
            "<a href=\"" + url + "\">" +
            (logo_img if logo_url else "Link") + "</a>")
        input_text = (
            "<input type=text" +
            " name=" + input_name +
            " size=" + str(self.INPUT_SZ) +
            " value=\"\" title=\"" + title + "\">")
        input_butn = (
            "<input type=submit style=\"width:" + str(self.SUBM_W) + "\"" +
            " value=\"" + title + "\">")
        form_f = "</td></tr></table></form>"
        search_f = "</td></tr>"
        result = (
            comment + "\n" +
            search_h + "\n" +
            "  " + form_h + "\n" +
            "".join(list(map(lambda i: "    " + i + "\n", input_hidden))) +
            "    " + input_logo + "\n" +
            "    " + input_text + "\n" +
            "    " + input_butn + "\n" +
            "  " + form_f + "\n" +
            search_f + "\n")
        return result

    def run(self, test=False):
        """ Main execution function """

        # Good page tab title
        self.page_str = "<TITLE>Start page</TITLE>\n"

        # Make sure forms can pass russian characters correctly
        self.page_str += (
            "<META http-equiv=Content-Type " +
            "content=\"text/html; charset=utf-8\">")  # old: windows-1251

        self.page_str += self.get_form_str(
            "Yandex", "text",
            "http://www.yandex.ru/yandsearch",
            "http://img.yandex.net/i/www/logo.png")
        self.page_str += self.get_form_str(
            "Google(EN)", "q",
            "http://www.google.com/search",
            "http://www.google.com/images/srpr/logo11w.png")
        self.page_str += self.get_form_str(
            "Google(RU)", "q",
            "http://www.google.com/search",
            "http://www.google.com/images/srpr/logo11w.png",
            {"hl": "ru"})
        self.page_str += self.get_form_str(
            "Bing", "q",
            "http://www.bing.com/search",
            "http://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/" +
            "Bing_logo_%282013%29.svg/200px-Bing_logo_%282013%29.svg.png")
        self.page_str += self.get_form_str(
            "Translate(Ya)", "text",
            "http://slovari.yandex.ru/search.xml",
            "https://upload.wikimedia.org/wikipedia/ru/a/ad/" +
            "%D0%AF%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BB%D0%BE%D0%B3.jpg")
        self.page_str += self.get_form_str(
            "Translate(G)", "q",
            "http://translate.google.com",
            "http://upload.wikimedia.org/wikipedia/commons/d/db/" +
            "Google_Translate_Icon.png",
            {"hl": "ru"})
        self.page_str += self.get_form_str(
            "Wiki(EN)", "search",
            "http://en.wikipedia.org/wiki/Search",
            "http://upload.wikimedia.org/wikipedia/commons/thumb/d/de/" +
            "Wikipedia_Logo_1.0.png/240px-Wikipedia_Logo_1.0.png")
        self.page_str += self.get_form_str(
            "Wiki(RU)", "search",
            "http://ru.wikipedia.org/wiki/Search",
            "http://upload.wikimedia.org/wikipedia/commons/thumb/d/de/" +
            "Wikipedia_Logo_1.0.png/240px-Wikipedia_Logo_1.0.png")
        self.page_str += self.get_form_str(
            "Finance(G)", "q",
            "https://www.google.com/finance",
            "http://upload.wikimedia.org/wikipedia/en/1/19/" +
            "Google_Finance_Beta_logo.png")
        self.page_str += self.get_form_str(
            "Maps(G)", "q",
            "http://maps.google.com/maps",
            "http://upload.wikimedia.org/wikipedia/commons/9/9a/" +
            "Google_maps_logo.png",
            {"output": "classic"})
        self.page_str += self.get_form_str(
            "Maps(Bing)", "q",
            "http://www.bing.com/maps/default.aspx",
            "http://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/" +
            "Bing_logo_%282013%29.svg/200px-Bing_logo_%282013%29.svg.png")
        self.page_str += self.get_form_str(
            "Youtube", "search_query",
            "http://www.youtube.com/results",
            "http://www.youtube.com/yt/brand/media/image/" +
            "YouTube-logo-full_color.png")
        self.page_str += self.get_form_str(
            "Zillow", "citystatezip",
            "http://www.zillow.com/search/RealEstateSearch.htm",
            "http://www.zillowstatic.com/static/images/m/apple-touch-icon.png")
        self.page_str += self.get_form_str(
            "Archive", "url",
            "http://web.archive.org/form-submit.jsp",
            "http://archive.org/web/images/logo_wayback_210x77.png",
            {"type": "urlquery"})
        self.page_str += self.get_form_str(
            "Whois", "query",
            "http://www.nic.ru/whois/",
            "http://www.nic.ru/images/logo.gif",
            {"ask_registrar": "1"})

        filehelp.write_file(self.OUT, self.page_str, append=0)


###############################################################################
# Executable code
###############################################################################


def main():

    # Sandbox
    sb = Start(" ".join(sys.argv[1:]))
    sb.run()

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    tmp_area = "/tmp/ut" + getpass.getuser()
    test_area = tmp_area + "/t" + str(random.randrange(10000))
    tmp_file = test_area + "/f" + str(random.randrange(10000))
    os.makedirs(test_area, exist_ok=True)

    def test_helping_functions(self):
        """ Helping functions testing """
        self.assertEqual(foo("bar"), "bar")

    def test_Start_class__basic_functionality(self):
        """ Start class basic testing """
        d = Start()

    def test_Start_class__get_form_str(self):
        """ Generate Input form HTML code """
        d = Start()
        form_str = d.get_form_str(
            "Title", "input_name", "url", "logo_url")
        self.assertTrue(re.search("Title", form_str))
        self.assertTrue(re.search("name=input_name", form_str))
        form_str = d.get_form_str(
            "Title", "input_name", "url", "logo_url", {"hid": "dn"})
        self.assertTrue(re.search("type=hidden name=hid value=dn", form_str))

    def test_Start_class__run(self):
        """ Main execution function """
        # Changing current directory to a temp area
        cwd = os.getcwd()
        os.chdir(self.test_area)

        d = Start()
        d.run(test=True)
        out_str = filehelp.read_file(d.OUT)

        # Changing current directory back
        os.remove(d.OUT)
        os.chdir(cwd)

    def test_xcleanup(self):
        os.rmdir(self.test_area)

if __name__ == "__main__":
    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])
    main()
