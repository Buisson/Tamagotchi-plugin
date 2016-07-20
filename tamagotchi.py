import sublime, sublime_plugin

class TamagotchiCommand(sublime_plugin.TextCommand):


# 1000 2000 --- 1
# 3000 4000 --- 2
# 5000 6000 --- 3


    def run(self, edit):
		self.view.insert(edit,0, "--(^o^)--\n")

		def display_happy():
			#sublime.message_dialog("dans fonc ...")
			self.view.replace(edit, sublime.Region(0,10), "--(^o^)--\n")

		def display_normal():
			#sublime.message_dialog("dans fonc ...")
			self.view.replace(edit, sublime.Region(0,10), "--(^-^)--\n")

		def normal_move(i):
			if i==1:
				sublime.set_timeout(display_happy, i*1000)
				sublime.set_timeout(display_normal, (i+1)*1000)
			else:
				sublime.set_timeout(display_happy, (i+(i-1))*1000)
				sublime.set_timeout(display_normal, (i+i)*1000)

		def doLoop():
			for i in range (1,10) :
				normal_move(i)			
		 	# return
		# for x in range(1,10):
		# 	sublime.set_timeout(lambda x=x: self.view.insert(edit,0,x), x*1000)
		#i = 0
		#while i<10 :
		# sublime.set_timeout(fonc , 5000)
		# self.view.replace(edit, sublime.Region(0,9), "--(^-^)--")
		# self.view.replace(edit, sublime.Region(0,9), "--(^o^)--")
		# self.view.replace(edit, sublime.Region(0,9), "--(^-^)--")
		#	i = i + 1
		
		doLoop()
