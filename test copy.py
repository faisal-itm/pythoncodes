
class Counter:
    def getValue(self):
        return self._strokes
    def click(self):
        self._strokes=self._strokes+"|"
    def reset(self):
        self._strokes=""

tally =Counter()

tally.reset()
tally.click()
tally.click()
tally.click()
r=tally.getValue()

print(r)


class Clock(n):
    def hours(self):

        self._hours= self._hours/60
    def minitues(self):
        return self._minutes

r=Clock(30)
c=Clock.hours()
print (c)

