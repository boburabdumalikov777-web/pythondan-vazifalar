"""Wild Roger is participating in a Western Showdown, meaning he has to draw (pull out and shoot) his gun faster than his opponent in a gun standoff.

Given two strings,p1 and p2, return which person drew their gun the fastest. If both are drawn at the same time, return "tie".

Examples
showdown(
  "   Bang!        ",
  "        Bang!   "
) ➞ "p1"

# p1 draws his gun sooner than p2

showdown(
  "               Bang! ",
  "             Bang!   "
) ➞ "p2"

showdown(
  "     Bang!   ",
  "     Bang!   "
) ➞ "tie"""
def showdown(p1, p2):
    for x, y in zip(p1, p2):
        if x=="B" and y!="B":
            return "p1"
        elif x!="B" and y=="B":
            return "p2"
        elif x=="B" and y=="B":
            return "tie"
print(showdown(
  "   Bang!        ",
  "        Bang!   "
))
print(showdown(
  "               Bang! ",
  "             Bang!   "
))
print(showdown(
  "     Bang!   ",
  "     Bang!   "
))