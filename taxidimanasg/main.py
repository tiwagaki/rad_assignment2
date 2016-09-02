#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import urllib2
import urllib
import json

url = 'http://datamall2.mytransport.sg/ltaodataservice/Taxi-Availability'

#Autjentication parameters
param = { 'AccountKey' : 'jmh3bT4mS0awdFDL6G6pSA==',
          'UniqueUserID' : '115dd78c-afb1-4eb3-88b1-44a194423d9b',
          'accept' : 'application/json'}

encoded_param = urllib.urlencode(param)

urlwithparam = url + '?' + encoded_param

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #response = urllib2.urlopen(urlwithparam).read()
        #data = json.loads(response)
        self.response.write(urlwithparam)
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
