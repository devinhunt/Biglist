# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Todo.due'
        db.alter_column('biglist_todo', 'due', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True))


    def backwards(self, orm):
        
        # Changing field 'Todo.due'
        db.alter_column('biglist_todo', 'due', self.gf('django.db.models.fields.DateTimeField')(blank=True))


    models = {
        'biglist.todo': {
            'Meta': {'object_name': 'Todo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'due': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['biglist']
