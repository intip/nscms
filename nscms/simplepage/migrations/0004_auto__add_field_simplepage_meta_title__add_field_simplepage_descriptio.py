# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SimplePage.meta_title'
        db.add_column(u'simplepage_simplepage', 'meta_title',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SimplePage.description'
        db.add_column(u'simplepage_simplepage', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


        # Changing field 'SimplePage.slug'
        db.alter_column(u'simplepage_simplepage', 'slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=255, separator=u'-', populate_from='title', overwrite=True))
        # Adding index on 'SimplePage', fields ['modified']
        db.create_index(u'simplepage_simplepage', ['modified'])

        # Adding index on 'SimplePage', fields ['created']
        db.create_index(u'simplepage_simplepage', ['created'])

        # Adding index on 'SimplePage', fields ['publish_date']
        db.create_index(u'simplepage_simplepage', ['publish_date'])

        # Adding index on 'SimplePage', fields ['expire_date']
        db.create_index(u'simplepage_simplepage', ['expire_date'])


        # Changing field 'SimplePage.title'
        db.alter_column(u'simplepage_simplepage', 'title', self.gf('django.db.models.fields.CharField')(max_length=255))
        # Adding index on 'SimplePage', fields ['published']
        db.create_index(u'simplepage_simplepage', ['published'])


    def backwards(self, orm):
        # Removing index on 'SimplePage', fields ['published']
        db.delete_index(u'simplepage_simplepage', ['published'])

        # Removing index on 'SimplePage', fields ['expire_date']
        db.delete_index(u'simplepage_simplepage', ['expire_date'])

        # Removing index on 'SimplePage', fields ['publish_date']
        db.delete_index(u'simplepage_simplepage', ['publish_date'])

        # Removing index on 'SimplePage', fields ['created']
        db.delete_index(u'simplepage_simplepage', ['created'])

        # Removing index on 'SimplePage', fields ['modified']
        db.delete_index(u'simplepage_simplepage', ['modified'])

        # Deleting field 'SimplePage.meta_title'
        db.delete_column(u'simplepage_simplepage', 'meta_title')

        # Deleting field 'SimplePage.description'
        db.delete_column(u'simplepage_simplepage', 'description')


        # Changing field 'SimplePage.slug'
        db.alter_column(u'simplepage_simplepage', 'slug', self.gf('django_extensions.db.fields.AutoSlugField')(populate_from='title', allow_duplicates=False, max_length=120, separator=u'-', overwrite=True))

        # Changing field 'SimplePage.title'
        db.alter_column(u'simplepage_simplepage', 'title', self.gf('django.db.models.fields.CharField')(max_length=120))

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'simplepage.simplepage': {
            'Meta': {'ordering': "['-created']", 'object_name': 'SimplePage'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expire_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'meta_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['simplepage.SimplePage']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'redirect_to': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'redirected_from'", 'null': 'True', 'to': u"orm['simplepage.SimplePage']"}),
            'redirect_to_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '255', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        }
    }

    complete_apps = ['simplepage']