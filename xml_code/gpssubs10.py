#!/usr/bin/env python

#
# Generated Tue Jun  3 22:47:21 2014 by generateDS.py version 2.12d.
#
# Command line options:
#   ('-o', 'gpx10.py')
#   ('-s', 'gpssubs10.py')
#
# Command line arguments:
#   schemas/gpx.1.0.xsd
#
# Command line:
#   venv/bin/generateDS.py -o "gpx10.py" -s "gpssubs10.py" schemas/gpx.1.0.xsd
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


class gpxSub(supermod.gpx):
    def __init__(self, version=None, creator=None, name=None, desc=None, author=None, email=None, url=None, urlname=None, time=None, keywords=None, bounds=None, wpt=None, rte=None, trk=None, anytypeobjs_=None):
        super(gpxSub, self).__init__(version, creator, name, desc, author, email, url, urlname, time, keywords, bounds, wpt, rte, trk, anytypeobjs_, )
supermod.gpx.subclass = gpxSub
# end class gpxSub


class boundsTypeSub(supermod.boundsType):
    def __init__(self, minlat=None, maxlon=None, minlon=None, maxlat=None):
        super(boundsTypeSub, self).__init__(minlat, maxlon, minlon, maxlat, )
supermod.boundsType.subclass = boundsTypeSub
# end class boundsTypeSub


class wptTypeSub(supermod.wptType):
    def __init__(self, lat=None, lon=None, ele=None, time=None, magvar=None, geoidheight=None, name=None, cmt=None, desc=None, src=None, url=None, urlname=None, sym=None, type_=None, fix=None, sat=None, hdop=None, vdop=None, pdop=None, ageofdgpsdata=None, dgpsid=None, anytypeobjs_=None):
        super(wptTypeSub, self).__init__(lat, lon, ele, time, magvar, geoidheight, name, cmt, desc, src, url, urlname, sym, type_, fix, sat, hdop, vdop, pdop, ageofdgpsdata, dgpsid, anytypeobjs_, )
supermod.wptType.subclass = wptTypeSub
# end class wptTypeSub


class rteTypeSub(supermod.rteType):
    def __init__(self, name=None, cmt=None, desc=None, src=None, url=None, urlname=None, number=None, anytypeobjs_=None, rtept=None):
        super(rteTypeSub, self).__init__(name, cmt, desc, src, url, urlname, number, anytypeobjs_, rtept, )
supermod.rteType.subclass = rteTypeSub
# end class rteTypeSub


class rteptTypeSub(supermod.rteptType):
    def __init__(self, lat=None, lon=None, ele=None, time=None, magvar=None, geoidheight=None, name=None, cmt=None, desc=None, src=None, url=None, urlname=None, sym=None, type_=None, fix=None, sat=None, hdop=None, vdop=None, pdop=None, ageofdgpsdata=None, dgpsid=None, anytypeobjs_=None):
        super(rteptTypeSub, self).__init__(lat, lon, ele, time, magvar, geoidheight, name, cmt, desc, src, url, urlname, sym, type_, fix, sat, hdop, vdop, pdop, ageofdgpsdata, dgpsid, anytypeobjs_, )
supermod.rteptType.subclass = rteptTypeSub
# end class rteptTypeSub


class trkTypeSub(supermod.trkType):
    def __init__(self, name=None, cmt=None, desc=None, src=None, url=None, urlname=None, number=None, anytypeobjs_=None, trkseg=None):
        super(trkTypeSub, self).__init__(name, cmt, desc, src, url, urlname, number, anytypeobjs_, trkseg, )
supermod.trkType.subclass = trkTypeSub
# end class trkTypeSub


class trksegTypeSub(supermod.trksegType):
    def __init__(self, trkpt=None):
        super(trksegTypeSub, self).__init__(trkpt, )
supermod.trksegType.subclass = trksegTypeSub
# end class trksegTypeSub


class trkptTypeSub(supermod.trkptType):
    def __init__(self, lat=None, lon=None, ele=None, time=None, course=None, speed=None, magvar=None, geoidheight=None, name=None, cmt=None, desc=None, src=None, url=None, urlname=None, sym=None, type_=None, fix=None, sat=None, hdop=None, vdop=None, pdop=None, ageofdgpsdata=None, dgpsid=None, anytypeobjs_=None):
        super(trkptTypeSub, self).__init__(lat, lon, ele, time, course, speed, magvar, geoidheight, name, cmt, desc, src, url, urlname, sym, type_, fix, sat, hdop, vdop, pdop, ageofdgpsdata, dgpsid, anytypeobjs_, )
supermod.trkptType.subclass = trkptTypeSub
# end class trkptTypeSub


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
        rootTag = 'gpx'
        rootClass = supermod.gpx
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:gpx="http://www.topografix.com/GPX/1/0"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'gpx'
        rootClass = supermod.gpx
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
        rootTag = 'gpx'
        rootClass = supermod.gpx
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:gpx="http://www.topografix.com/GPX/1/0"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'gpx'
        rootClass = supermod.gpx
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
