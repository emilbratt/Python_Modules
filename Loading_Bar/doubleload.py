#!/usr/bin/env python3
# Emil Bratt -> emilbratt@gmail.com
import sys
from time import sleep
import os

class Loadbar:
    def __init__(
    self, taskname, laps,clear='false',
    headLeft='<', headRight='>',
    eatLeft=' ', eatRight=' ',
    trailLeft =' ', trailRight =' '
    ):
        self.animations = {
        'headLeft':headLeft,
        'headRight':headRight,
        'eatLeft':eatLeft,
        'eatRight':eatRight,
        'trailLeft':trailLeft,
        'trailRight':trailRight
        }

        self.platform = sys.platform
        self.clear = clear
        self.clearScreen = lambda : os.system(
            'cls' if os.name == 'nt' else 'clear')

        # base 1, 10 or 100 affects the increments
        # for number of digits in each round
        if len(str(laps)) < 2:
            self.base = 1
        if len(str(laps)) == 2:
            self.base = 10
        if len(str(laps)) > 2:
            self.base = 100

        self.laps = laps
        self.taskname = taskname[:51]
        self.horizontal = '+'+'-'*51 +'+'
        self.totalLaps = ('Total Iterations: '+
        str(laps)).center(25, " ")


    def display(self, round):

        round += 1

         # force increments within 100% regardless if laps is  < 100
        basePercent = int(str(
            self.base).ljust(3, '0'))

        # calculate progress in %
        progress = (basePercent/self.laps)*round
        showPercentage = 'Progress: '+str(
            int(progress))+'/100%'

        self.roundCount = ('Current Iteration: ' + str(
            round)).center(25, " ")+'|'

        if round == self.laps:
            loadingRight = (self.animations[
                'trailRight'] * 50 + self.animations[
                'headRight']).ljust(51,
                self.animations['eatRight'])
            loadingLeft = (self.animations[
                'headLeft'] + self.animations[
                'trailLeft'] * 50).rjust(51,
                self.animations['eatLeft'])
        else:
            loadingRight = (self.animations[
                'trailRight'] * (int(progress//2)) +
                self.animations[
                'headRight']).ljust(51,
                self.animations[
                'eatRight'])
            loadingLeft = (self.animations[
                'headLeft'] + self.animations['trailLeft'] *
                (int(progress//2))).rjust(51,
                self.animations['eatLeft'])

        print(self.horizontal)
        print(f'|{loadingRight}|')
        print(f'+{self.taskname.center(51, "-")}+')
        print(f'|{self.totalLaps}|{self.roundCount}')
        print(f'+{showPercentage.center(51, "-")}+')
        print(f'|{loadingLeft}|')
        print(self.horizontal)
        
        if round != self.laps:
            if self.platform.startswith(
            'linux'
            ) or self.platform.startswith(
            'darwin'):
                [sys.stdout.write("\033[F") for _ in range(7)]
            elif self.platform.startswith(
            'win32'):
                self.clearScreen()
        else:
            if self.clear == 'clear':
                sleep(1)
                self.clearScreen()


    def iterations(self):
        return self.laps
