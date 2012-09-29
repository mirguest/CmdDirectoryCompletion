#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lintao

from DIRAC.Core.Base import Script
Script.parseCommandLine( ignoreErrors = False )

from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

from AbstractFileSystem import DFCFileSystem

import pprint

fc = FileCatalogClient()

dfc_fs = DFCFileSystem(fc)

#pprint.pprint( dfc_fs.is_dir("/bes") )
#pprint.pprint( dfc_fs.is_dir("/lintao") )
#pprint.pprint( list( dfc_fs.list_dir("/bes") ) )
#pprint.pprint( list( dfc_fs.list_dir("/lintao") ) )

from DirectoryCompletion import DirectoryCompletion

dc = DirectoryCompletion(dfc_fs)

print dc.parse_text_line("", "/", "/")
