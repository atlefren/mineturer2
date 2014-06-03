#!/usr/bin/env python

#
# Generated Tue Jun  3 22:17:54 2014 by generateDS.py version 2.12d.
#
# Command line options:
#   ('-o', 'gpx11.py')
#   ('-s', 'gpssubs11.py')
#
# Command line arguments:
#   schemas/gpx.1.1.xsd
#
# Command line:
#   venv/bin/generateDS.py -o "gpx11.py" -s "gpssubs11.py" schemas/gpx.1.1.xsd
#
# Current working directory (os.getcwd()):
#   mineturer2
#

import sys

import ??? as supermod

etree_ = None
Verbose_import_ = False
(
    XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError(
                        "Failed to import ElementTree from any known place")


def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
            'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class gpxTypeSub(supermod.gpxType):
    def __init__(self, version=None, creator=None, metadata=None, wpt=None, rte=None, trk=None, extensions=None):
        super(gpxTypeSub, self).__init__(version, creator, metadata, wpt, rte, trk, extensions, )
supermod.gpxType.subclass = gpxTypeSub
# end class gpxTypeSub


class metadataTypeSub(supermod.metadataType):
    def __init__(self, name=None, desc=None, author=None, copyright=None, link=None, time=None, keywords=None, bounds=None, extensions=None):
        super(metadataTypeSub, self).__init__(name, desc, author, copyright, link, time, keywords, bounds, extensions, )
supermod.metadataType.subclass = metadataTypeSub
# end class metadataTypeSub


class wptTypeSub(supermod.wptType):
    def __init__(self, lat=None, lon=None, ele=None, time=None, magvar=None, geoidheight=None, name=None, cmt=None, desc=None, src=None, link=None, sym=None, type_=None, fix=None, sat=None, hdop=None, vdop=None, pdop=None, ageofdgpsdata=None, dgpsid=None, extensions=None):
        super(wptTypeSub, self).__init__(lat, lon, ele, time, magvar, geoidheight, name, cmt, desc, src, link, sym, type_, fix, sat, hdop, vdop, pdop, ageofdgpsdata, dgpsid, extensions, )
supermod.wptType.subclass = wptTypeSub
# end class wptTypeSub


class rteTypeSub(supermod.rteType):
    def __init__(self, name=None, cmt=None, desc=None, src=None, link=None, number=None, type_=None, extensions=None, rtept=None):
        super(rteTypeSub, self).__init__(name, cmt, desc, src, link, number, type_, extensions, rtept, )
supermod.rteType.subclass = rteTypeSub
# end class rteTypeSub


class trkTypeSub(supermod.trkType):
    def __init__(self, name=None, cmt=None, desc=None, src=None, link=None, number=None, type_=None, extensions=None, trkseg=None):
        super(trkTypeSub, self).__init__(name, cmt, desc, src, link, number, type_, extensions, trkseg, )
supermod.trkType.subclass = trkTypeSub
# end class trkTypeSub


class extensionsTypeSub(supermod.extensionsType):
    def __init__(self, anytypeobjs_=None):
        super(extensionsTypeSub, self).__init__(anytypeobjs_, )
supermod.extensionsType.subclass = extensionsTypeSub
# end class extensionsTypeSub


class trksegTypeSub(supermod.trksegType):
    def __init__(self, trkpt=None, extensions=None):
        super(trksegTypeSub, self).__init__(trkpt, extensions, )
supermod.trksegType.subclass = trksegTypeSub
# end class trksegTypeSub


class copyrightTypeSub(supermod.copyrightType):
    def __init__(self, author=None, year=None, license=None):
        super(copyrightTypeSub, self).__init__(author, year, license, )
supermod.copyrightType.subclass = copyrightTypeSub
# end class copyrightTypeSub


class linkTypeSub(supermod.linkType):
    def __init__(self, href=None, text=None, type_=None):
        super(linkTypeSub, self).__init__(href, text, type_, )
supermod.linkType.subclass = linkTypeSub
# end class linkTypeSub


class emailTypeSub(supermod.emailType):
    def __init__(self, domain=None, id=None):
        super(emailTypeSub, self).__init__(domain, id, )
supermod.emailType.subclass = emailTypeSub
# end class emailTypeSub


class personTypeSub(supermod.personType):
    def __init__(self, name=None, email=None, link=None):
        super(personTypeSub, self).__init__(name, email, link, )
supermod.personType.subclass = personTypeSub
# end class personTypeSub


class ptTypeSub(supermod.ptType):
    def __init__(self, lat=None, lon=None, ele=None, time=None):
        super(ptTypeSub, self).__init__(lat, lon, ele, time, )
supermod.ptType.subclass = ptTypeSub
# end class ptTypeSub


class ptsegTypeSub(supermod.ptsegType):
    def __init__(self, pt=None):
        super(ptsegTypeSub, self).__init__(pt, )
supermod.ptsegType.subclass = ptsegTypeSub
# end class ptsegTypeSub


class boundsTypeSub(supermod.boundsType):
    def __init__(self, minlat=None, maxlon=None, minlon=None, maxlat=None):
        super(boundsTypeSub, self).__init__(minlat, maxlon, minlon, maxlat, )
supermod.boundsType.subclass = boundsTypeSub
# end class boundsTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'gpxType'
        rootClass = supermod.gpxType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'gpxType'
        rootClass = supermod.gpxType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'gpxType'
        rootClass = supermod.gpxType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'gpxType'
        rootClass = supermod.gpxType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
