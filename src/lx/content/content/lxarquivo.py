"""Definition of the Lx arquivo content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from plone.app.blob.field import BlobField, ImageField

# -*- Message Factory Imported Here -*-
from lx.content import contentMessageFactory as _

from lx.content.interfaces import ILxarquivo
from lx.content.config import PROJECTNAME

LxarquivoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.ImageField(
        'imagem_video',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Imagem de video"),
            description=_(u"Inserir imagem do video"),
        ),
        required=True,
        validators=('isNonEmptyFile'),
    ),

))


schemata.finalizeATCTSchema(LxarquivoSchema, moveDiscussion=False)


class Lxarquivo(base.ATCTContent):
    """Description of the Example Type"""
    implements(ILxarquivo)

    meta_type = "Lxarquivo"
    schema = LxarquivoSchema


atapi.registerType(Lxarquivo, PROJECTNAME)
