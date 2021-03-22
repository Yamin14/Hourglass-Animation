import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import *
from kivy.clock import Clock

class Animation(Widget):
	def __init__(self, **kwargs):
		super(Animation, self).__init__(**kwargs)
		self.play()
		
	def play(self):
		with self.canvas:
			#border
			Color(rgb=(0.7, 0.4, 0.3))
			Triangle(points=[350, 600, 230, 380, 470, 380])
			Triangle(points=[350, 600, 230, 820, 470, 820])
			Line(points=[230, 380, 230, 820], width=5)
			Line(points=[470, 380, 470, 820], width=5)
			
			#inside
			Color(rgb=(0, 1, 1))
			Triangle(points=[350, 600, 250, 400, 450, 400])
			Triangle(points=[350, 600, 250, 800, 450, 800])
			
			#upper sand
			col = (1, 0.8, 0, 1)
			self.tall = 780
			self.base1, self.base2 = 260, 440
			Color(rgba=col)
			self.up = Triangle(points=[350, 600, self.base1, self.tall, self.base2, self.tall])
			
			#lower sand
			Color(rgba=col)
			self.xl, self.xr = 250, 450
			self.lineY = 400
			
			self.topLine = Line(points=[(self.xl, self.lineY), (self.xr, self.lineY)])
			
			self.rexW, self.rexH = 200, 0
			self.rexX, self.rexY = 250, 400
			  
			self.rex = Rectangle(size=(self.rexW, self.rexH), pos=(self.rexX, self.rexY))
			
			self.triLBX, self.triLBY = 250, 400
			self.triLHX, self.triLHY = 250, 400
			
			self.triL = Triangle(points=[250, 400, self.triLBX, self.triLBY, self.triLHX, self.triLHY])
			
			self.triRBX, self.triRBY = 450, 400
			self.triRHX, self.triRHY = 450, 400
			
			self.triR = Triangle(points=[450, 400, self.triRBX, self.triRBY, self.triRHX, self.triRHY])
			
			#falling
			self.grainSize = (5, 5)
			self.grainPos = (347.5, 595)
			self.grainsNum = 40
			self.grains = []
			self.dec = 5
			self.speed = 0.5
			Color(rgba=col)
			for i in range(self.grainsNum):
				self.grains.append(Ellipse(size=self.grainSize, pos=(self.grainPos[0], self.grainPos[1]+(i*5))))

		Clock.schedule_interval(self.falling, 0)
			
	def falling(self, dt):
		#grains falling
		for i in range(self.grainsNum):
			if self.grains[i].pos[1] > 400:
				self.grains[i].pos = (self.grainPos[0], self.grains[i].pos[1] - self.dec)
			
			elif self.tall >= 600:
				self.grains[i].pos = (self.grainPos[0], self.grainPos[1])
				
		#upper sand decreasing
		if self.tall >= 600:
			self.tall -= self.speed
			self.base1 += (self.speed/2)
			self.base2 -= (self.speed/2)
			self.up.points = [350, 600, self.base1, self.tall, self.base2, self.tall]
			
		#lower sand increasing
		if self.lineY <= 500:
			self.lineY += self.speed/2
			self.xl += (self.speed/4)
			self.xr -= (self.speed/4)
			self.topLine.points = [(self.xl, self.lineY), (self.xr, self.lineY)]
			
			self.rexH += self.speed/2
			self.rexW -= self.speed/2
			self.rexX += self.speed/4
			self.rex.size = (self.rexW, self.rexH)
			self.rex.pos = (self.rexX, self.rexY)
			
			self.triLBX += self.speed/4
			self.triLHX += self.speed/4
			self.triLHY += self.speed/2
			self.triL.points = [250, 400, self.triLBX, self.triLBY, self.triLHX, self.triLHY]
			
			self.triRBX -= self.speed/4
			self.triRHX -= self.speed/4
			self.triRHY += self.speed/2
			self.triR.points = [450, 400, self.triRBX, self.triRBY, self.triRHX, self.triRHY]
											
class MyApp(App):
	def build(self):
		return Animation()
		
if __name__ == "__main__":
	MyApp().run()
