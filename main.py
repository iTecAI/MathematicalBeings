import pygame, random, math, keyboard
pygame.init()

class Particle:
    def __init__(self,pos):
        self.surf = pygame.Surface([8,8])
        self.color = [random.randint(0,255) for i in range(3)]
        self.surf.fill(self.color)
        #self.surf.fill([255,255,255])
        self.pos = pos
        self.spd = [random.randint(-35,35),random.randint(-35,35)]
        #self.spd = [0,0]
    def render(self):
        self.pos[0] += self.spd[0]
        self.pos[1] += self.spd[1]
        #print(self.pos)
        if self.pos[0] > 1921:
            self.pos[0] = 0
        if self.pos[1] > 1081:
            self.pos[1] = 0
        if self.pos[0] < -10:
            self.pos[0] = 1920
        if self.pos[1] < -10:
            self.pos[1] = 1080
        return self.surf
    def setforce(self, particles):
        for i in particles:
            if id(i) != id(self):
                xd = self.pos[0] - i.pos[0]
                yd = self.pos[1] - i.pos[1]
                #print(type(yd))
                distmodx = 0
                distmody = 0
                if abs(xd) < 200 and abs(yd) < 200:
                    if abs(xd) > 4:
                        distmodx = 4 * float(xd**-1)
                    else:
                        try:
                            distmodx = -0.01 * float(xd**-1)
                        except:
                            pass
                    if abs(yd) > 4:
                        distmody = 4 * float(yd**-1)
                    else:
                        try:
                            distmody = -0.01 * float(xd**-1)
                        except:
                            pass
                #print(distmod)
                mycolor = sum(self.color)
                theircolor = sum(i.color)
                if abs(mycolor-theircolor)/3 > 127:
                    cmod = 1
                else:
                    cmod = -1
                csmod = 0.0002 * ((mycolor-theircolor)-127)**2
                self.spd[0] += (cmod * distmodx * csmod)/3
                self.spd[1] += (cmod * distmody * csmod)/3
                self.spd[0] = self.spd[0] / 1.005
                self.spd[1] = self.spd[1] / 1.005

particles = []
for i in range(200):
    particles.append(Particle([random.randint(0,1920),random.randint(0,1080)]))

screen = pygame.display.set_mode([1920,1080],pygame.FULLSCREEN | pygame.HWSURFACE)
screen.fill([56, 56, 56])
while True:
    if not keyboard.is_pressed('space'):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        screen.fill([25, 25, 25])
        for i in particles:
            i.setforce(particles)
            screen.blit(i.render(),i.pos)
        pygame.display.flip()
        #pygame.time.Clock().tick(20)
