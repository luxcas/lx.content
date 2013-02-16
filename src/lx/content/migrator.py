from plone.app.blob.migrations import migrate


def migrateLxarquivo(context):
    return migrate(context, 'Lxarquivo')
