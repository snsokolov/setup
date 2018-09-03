#!/usr/bin/env python
# start_page_gen.py - Start bage generator program by Sergey 2014

import unittest
import sys
import os
import argparse
import re
import random
import subprocess
import getpass

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
    OUT = "start_page.html"

    def get_form_str(self, title, input_name, url, hidden={}):
        """ Generate Input form HTML code """
        comment = "<!-- " + title + " -->"
        logo_url = "imgs/" + title + ".jpg"
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
            "content=\"text/html; charset=utf-8\">\n")  # old: windows-1251

        self.page_str += self.get_form_str(
            "Yandex", "text",
            "https://yandex.ru/search",
        )
        self.page_str += self.get_form_str(
            "Google(EN)", "q",
            "http://www.google.com/search",
        )
        self.page_str += self.get_form_str(
            "Google(RU)", "q",
            "http://www.google.com/search",
            {"hl": "ru"}
        )
        self.page_str += self.get_form_str(
            "Bing", "q",
            "http://www.bing.com/search",
        )
        self.page_str += self.get_form_str(
            "Translate(Ya)", "text",
            "http://slovari.yandex.ru/search.xml",
        )
        self.page_str += self.get_form_str(
            "Translate(G)", "q",
            "http://translate.google.com",
            {"hl": "ru"},
        )
        self.page_str += self.get_form_str(
            "Wiki(EN)", "search",
            "http://en.wikipedia.org/wiki/Search",
        )
        self.page_str += self.get_form_str(
            "Wiki(RU)", "search",
            "http://ru.wikipedia.org/wiki/Search",
        )
        self.page_str += self.get_form_str(
            "Finance(G)", "q",
            "https://www.google.com/finance",
        )
        self.page_str += self.get_form_str(
            "Maps(G)", "q",
            "http://maps.google.com/maps",
            {"output": "classic"},
        )
        self.page_str += self.get_form_str(
            "Maps(Bing)", "q",
            "http://www.bing.com/maps/default.aspx",
        )
        self.page_str += self.get_form_str(
            "Youtube", "search_query",
            "http://www.youtube.com/results",
        )
        self.page_str += self.get_form_str(
            "Zillow", "citystatezip",
            "http://www.zillow.com/search/RealEstateSearch.htm",
        )
        self.page_str += self.get_form_str(
            "Archive", "url",
            "http://web.archive.org/form-submit.jsp",
            {"type": "urlquery"},
        )
        self.page_str += self.get_form_str(
            "Whois", "query",
            "http://www.nic.ru/whois/",
            {"ask_registrar": "1"},
        )

        write_file(self.OUT, self.page_str, append=0)


def write_file(filename, file_str, append=0):
    """ Write string into a file (will overwrite existing file) """
    fh = open(filename, "a+" if append else "w", newline="\n")
    fh.write(file_str + "\n")
    fh.close()


def read_file(filename):
    """ Read a string from a file """
    fh = open(filename, "r")
    file_str = fh.read()
    file_str = re.sub("$\n", "", file_str)
    fh.close()
    return file_str


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    tmp_area = "/tmp/ut" + getpass.getuser()
    test_area = tmp_area + "/t" + str(random.randrange(10000))
    tmp_file = test_area + "/f" + str(random.randrange(10000))
    os.makedirs(test_area, exist_ok=True)

    def test_Start_class__basic_functionality(self):
        """ Start class basic testing """
        d = Start()

    def test_Start_class__get_form_str(self):
        """ Generate Input form HTML code """
        d = Start()
        form_str = d.get_form_str(
            "Title", "input_name", "url")
        self.assertTrue(re.search("Title", form_str))
        self.assertTrue(re.search("name=input_name", form_str))
        form_str = d.get_form_str(
            "Title", "input_name", "url", {"hid": "dn"})
        self.assertTrue(re.search("type=hidden name=hid value=dn", form_str))

    def test_Start_class__run(self):
        """ Main execution function """
        # Changing current directory to a temp area
        cwd = os.getcwd()
        os.chdir(self.test_area)

        d = Start()
        d.run(test=True)
        out_str = read_file(d.OUT)

        # Changing current directory back
        os.remove(d.OUT)
        os.chdir(cwd)

    def test_xcleanup(self):
        os.rmdir(self.test_area)

if __name__ == "__main__":
    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])
    Start().run()
