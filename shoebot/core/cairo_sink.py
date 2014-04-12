#!/usr/bin/env python2

# This file is part of Shoebot.
# Copyright (C) 2007-2009 the Shoebot authors
# See the COPYING file for the full license text.
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#
#   Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#   The name of the author may not be used to endorse or promote products
#   derived from this software without specific prior written permission.
#
#   THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED
#   WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#   MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
#   EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#   OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
#   WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
#   OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import os
import cairocffi as cairo

from drawqueue_sink import DrawQueueSink

class CairoImageSink(DrawQueueSink):
    '''
    DrawQueueSink that uses cairo contexts as the render context.
    '''
    def __init__(self, filename=None, format=None, multifile=False, buff=None):
        """
        :param filename:  output filename
        :param format:    if filename is specified this is not needed.
        :param multifile: If used with filename, then numbered files will be output for each froam.
        :param buff:      optionally a file like object can be used instead of a filename
                          this is useful for streaming output.

        """
        DrawQueueSink.__init__(self)
        if format is None:
            if filename is not None:
                format = os.path.splitext(filename)[1][1:].lower()
            elif buff is not None:
                raise AttributeError("No format specified, but using buff")
        self.buff = buff
        self.format = format
        self.filename = filename
        self.multifile = multifile
        self.file_root, self.file_ext = os.path.splitext(filename)

    def _output_file(self, frame):
        """
        If filename was used output a filename, along with multifile
        numbered filenames will be used.

        If buff was specified it is returned.

        :return: Output buff or filename.
        """
        if self.buff:
            return self.buff
        elif self.multifile:
            return self.file_root + "_%03d" % frame + self.file_ext
        else:
            return self.filename

    def create_rcontext(self, size, frame):
        """
        Called when CairoCanvas needs a cairo context to draw on
        """
        if self.format == 'pdf':
            surface = cairo.PDFSurface(self._output_file(frame), *size)
        elif self.format == 'png':
            surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, *size)
        elif self.format in ('ps', 'eps'):
            surface = cairo.PSSurface(self._output_file(frame), *size)
        if self.format == 'svg':
            surface = cairo.SVGSurface(self._output_file(frame), *size)
        return cairo.Context(surface)

    def rendering_finished(self, size, frame, cairo_ctx):
        """
        Called when CairoCanvas has rendered a bot
        """
        surface = cairo_ctx.get_target()
        if self.format == 'png':
            surface.write_to_png(self._output_file(frame))
        surface.finish()
        surface.flush()

    def finish(self):
        pass
