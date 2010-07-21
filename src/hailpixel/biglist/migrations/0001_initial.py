# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Todo'
        db.create_table('biglist_todo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('task', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('due', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal('biglist', ['Todo'])


    def backwards(self, orm):
        
        # Deleting model 'Todo'
        db.delete_table('biglist_todo')


    models = {
        'biglist.todo': {
            'Meta': {'object_name': 'Todo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'due': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['biglist']
