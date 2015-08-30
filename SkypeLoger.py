#!/usr/bin/env python2
#!coding:utf-8

import Skype4Py


class SkypeLoger:
	def __init__(self):
		'''
			Initial login
		'''
		print 'Start Initial...'
		self.skype = Skype4Py.Skype()
		self.Attach()
		print 'Finish Initial...'

		print 'Hello,', self.skype.CurrentUser.FullName
	
	def showChatRooms(self):
		'''
			Display Chat Rooms
		'''
		for i in range(len(self.skype.Chats)):
			print '%d)\t%s' % (i+1, self.skype.Chats[i].FriendlyName)



if __name__ == '__main__':
	s = SkypeLoger()
		
