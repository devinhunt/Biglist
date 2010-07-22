# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Todo.due'
        db.delete_column('biglist_todo', 'due')

        # Adding field 'Todo.finished'
        db.add_column('biglist_todo', 'finished', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Todo.due'
        db.add_column('biglist_todo', 'due', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Deleting field 'Todo.finished'
        db.delete_column('biglist_todo', 'finished')


    models = {
        'biglist.todo': {
            'Meta': {'object_name': 'Todo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'finished': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['biglist']
