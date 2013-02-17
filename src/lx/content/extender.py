from zope.component import adapts
from zope.interface import implements

from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField
from plone.app.blob.field import BlobField, ImageField

from Products.Archetypes import atapi

from lx.content.interfaces import ILxarquivo
from lx.content import contentMessageFactory as _


class ExtensionBlobField(ExtensionField, BlobField):
    """ derivative of blobfield for extending schemas """


class ExampleATTypeExtender(object):
    adapts(ILxarquivo)
    implements(ISchemaExtender)

    fields = [
        ExtensionBlobField('file',
            widget=atapi.FileWidget(
                label=_(u"A File - arquivo de video"),
                description=_(u"Some File"),
            ),

            required=True,
            validators=('isNonEmptyFile'),
        ),

        #ExtensionBlobField('secondfile',
        #    widget=atapi.FileWidget(
        #        label=_(u"Some other file"),
        #        description=_(u"Some other file"),
        #    ),
        #    required=False,
        #    #validators=('isNonEmptyFile'),
        #),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
