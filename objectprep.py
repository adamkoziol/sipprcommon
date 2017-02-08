#!/usr/bin/env python
from sipprcommon.accessoryfunctions.accessoryFunctions import *
import createFastq
import createObject

__author__ = 'adamkoziol'


class Objectprep(object):

    def objectprep(self):
        """
        Creates fastq files from an in-progress Illumina MiSeq run or create an object and moves files appropriately
        """
        printtime('Starting genesippr analysis pipeline', self.starttime)
        # Run the genesipping if necessary. Otherwise create the metadata object
        if self.bcltofastq:
            if self.customsamplesheet:
                assert os.path.isfile(self.customsamplesheet), 'Cannot find custom sample sheet as specified {}' \
                    .format(self.customsamplesheet)
            self.samples = createFastq.FastqCreate(self)
        else:
            self.samples = createObject.ObjectCreation(self)

    def __init__(self, inputobject):
        self.starttime = inputobject.starttime
        self.customsamplesheet = inputobject.customsamplesheet
        self.bcltofastq = inputobject.bcltofastq
        self.sequencepath = inputobject.sequencepath
        self.samples = MetadataObject()
