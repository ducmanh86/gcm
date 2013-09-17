db.define_table('gcm_user',
    Field('gcm_id', type = 'string', label = T('GCM ID')),
    Field('name', type = 'string', length = 50, label = T('Name')),
    Field('email', type = 'string', length = 255, label = T('Name')),
    format = '%(name)s')
db.gcm_user._singular = 'GCM User'
db.gcm_user._plural = 'GCM Users'