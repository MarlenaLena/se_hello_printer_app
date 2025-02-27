import json
import xml
import unittest
from hello_world import app
from hello_world.formater import SUPPORTED
#import xml.etree.ElementTree as xml


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        test_data = {"imie": "Marlena", "msg": "Hello World!"}
        rv = self.app.get('/?output=json')
        js = json.loads(rv.data)
        self.assertEqual(test_data['msg'], js['msg'])
        self.assertEqual(test_data['imie'], js['imie'])
        self.assertEqual(len(test_data), len(js))

    #    self.assertEqual(b'{ "imie":"Marlena", "mgs":Hello World!"}', rv.data)

    #def test_msg_with_output1(self):
        #test_data = {"imie": "Marlena", "msg": "Hello World!"}
        #rv = self.app.get('/?output=xml')
        #js = xml.parse(rv.data)
        #self.assertEqual(test_data['msg'], js['msg'])
        #self.assertEqual(test_data['imie'], js['imie'])
        #self.assertEqual(len(test_data), len(js))

    #def test_msg_with_output2(self):
        #rv = self.app.get('/?output=xml')
        #self.assertEqual(b'<greetings><name>Marlena</name>' +
                        # b'<msg>Hello World!</msg></greetings>', rv.data)
