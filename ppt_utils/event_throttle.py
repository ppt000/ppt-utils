'''
Created on 19 Nov 2017

@author: PierPaolo
'''

import time

_stages = ['ok','error','recovering']

class eventThrottle:
            
    def __init__(self, period = 60):
        self.total = 0
        self.seq = 0
        self.nonseqblocks = 0
        self._timer = time.time()
        self._lasteventok = True
        self._lasttotal = 0
        self._period = period
        self._stage = 0
    
    def _trigger(self):
        if self.total == 0:
            return False
        t = time.time()
        if self._lasttotal == 0:
                self._timer = t # reset timer
                self._lasttotal = self.total
                return True
        elif (t - self._timer) > self._period:
            if (self.total == self._lasttotal): # no errors in that period
                self.total = 0
                self._lasttotal = 0
                self.seq = 0
                self.nonseqblocks = 0
                return True # this is an 'all goes back to normal' event!
            else:
                self._timer = t # reset timer
                self._lasttotal = self.total
                return True
        
    def fail(self):
        '''
        Called when an error has happened. Increment total errors, if prior
        event was an error, increment consecutive errors otherwise increment the
        block count.
        '''
        self._stage = 1
        if self.total == 0:
            self._timer = time.time()
        self.total += 1
        if self._lasteventok: # last event was not an error
            self.nonseqblocks += 1 # starting a new block
        else:
            self.seq += 1
        self._lasteventok = False
        return self._trigger()

    def success(self):
        '''
        Called when the event has succesfully completed. It HAS to be called
        when things go well otherwise the information returned by this class is
        meaningless.
        '''
        self._lasteventok = True
        return self._trigger()
