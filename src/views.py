# coding: utf-8
#######################################################################################
#Copyright (C) 2010 Quest Software, Inc.
#File:        views.py
#Version:       1.0.0.0

#######################################################################################
#
#       THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
#       EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
#       WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
#
########################################################################################
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response as _render_to_response
from django_websocket.decorators import require_websocket, accept_websocket
import protocol
import traceback, sys, logging, os

LOG_FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)),'waferslim-websocket-server.log')
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log = logging.getLogger('waferslim')

__all__ = ('handler',)
_isolate_imports = False
_executioncontext=protocol.ExecutionContext(isolate_imports=_isolate_imports)

@accept_websocket
def handler(request):
    if not request.is_websocket():
        log.debug('Not a webSocket connection')
        return HttpResponse('<html><body>WebSocket connection required</body></html>', status=403)
    for message in request.websocket:
            try:
                log.debug('Handling message: %s' % message)
                message = handle_message(message)
                log.debug('Handling responsing with message: %s' % message)
            except Exception, ex:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                message = "%s\n%s" % ( ex, traceback.extract_tb(exc_traceback) )
                log.error(message)
            request.websocket.send(message)
    log.debug('WebSocket connection closed')
    _executioncontext=protocol.ExecutionContext(isolate_imports=_isolate_imports)
    log.debug('Recreating Waferslim ExecutionContext')
    return HttpResponse()


def instructions_for(datas):
    instructions = []
    for instruction in datas:
        instruction_id, instruction_params, instruction_instance = instruction[0], instruction[2:], instruction[1]
        instruction_instance = protocol._INSTRUCTION_TYPES[instruction_instance](instruction_id,instruction_params)
        instructions += [ instruction_instance ] 
    return instruction_instance

def handle_message(data, isolate_imports=False, executioncontext=_executioncontext, new_result=protocol.Results, instructions=instructions_for):
    result = new_result()
    execution_context = executioncontext#executioncontext(isolate_imports=isolate_imports)
    try:
        instruction_list = instructions(protocol.unpack(data))
        instruction_list.execute(execution_context, result)
    except protocol.UnpackingError, error:
        result.failed(error, error.description())

    results = result.collection()
    return protocol.pack(results)
