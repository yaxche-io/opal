"""
Unittests for opal.utils
"""
from django.test import TestCase
from django.db.models import ForeignKey, CharField

from opal import utils

class StringportTestCase(TestCase):

    def test_import(self):
        import collections
        self.assertEqual(collections, utils.stringport('collections'))

    def test_import_no_period(self):
        with self.assertRaises(ImportError):
            utils.stringport('wotcha')

    def test_import_perioded_thing(self):
        self.assertEqual(TestCase, utils.stringport('django.test.TestCase'))

    def test_empty_name_is_valueerror(self):
        with self.assertRaises(ValueError):
            utils.stringport('')


class ItersubclassesTestCase(TestCase):
    def test_tree_structure(self):
        class A(object):
            pass

        class B(A):
            pass

        class C(B, utils.AbstractBase):
            pass

        class D(C):
            pass

        results = {i for i in utils._itersubclasses(A)}
        self.assertEqual(results, set([B, D]))

    def test_old_style_classes(self):
        class Old: pass
        with self.assertRaises(TypeError):
            list(utils._itersubclasses(Old))


class FindTemplateTestCase(TestCase):

    def test_find_template_first_exists(self):
        self.assertEqual('base.html',
                         utils.find_template(['base.html', 'baser.html', 'basest.html']))

    def test_find_template_one_exists(self):
        self.assertEqual('base.html',
                         utils.find_template(['baser.html', 'base.html', 'basest.html']))

    def test_find_template_none_exists(self):
        self.assertEqual(None, utils.find_template(['baser.html', 'basest.html']))
