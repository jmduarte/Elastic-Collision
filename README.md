Elastic-Collision
=================

A Python simulation of elastic collision in 2d. Modified as a demonstration of matter-antimatter asymmetry in a toy universe. Blue balls represent matter, red balls represent antimatter, and green balls represent light. Motion dampening (friction) is applied to simulate the effect of an expanding universe.

Possible symmetric interactions:
red + blue -> green + green
green + green -> red + blue (if velocity is above some threshold)

Possible asymmetric interactions:
green + green -> blue + blue (if velocity is above some threshold)

Scenario A: Equal initial numbers of red and blue balls; no asymmetric interactions:
```
python main.py --red 10 --blue 10 --asymmetry 0
```

Scenario B: Unequal inital numbers of red and blue balls; no asymmetric interactions:
```
python main.py --red 5 --blue 15 --asymmetry 0
```

Scenario C: Equal initial numbers of red and blue balls; asymmetric interaction 10% of the time:
```
python main.py --red 10 --blue 10 --asymmetry 0.1
```
