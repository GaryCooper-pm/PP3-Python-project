![pixelmixel logo](docs/images/pixelmixel.png "Pixel Mixel Logo")

Welcome to my third Code Institute diploma project.

# Introduction and Overview
For my third project I decided to create a ***choose your own adventure*** style text game.

### **Live Project can be viewed:**  [HERE](https://garycooper-pm.github.io/PP3-Python-project/)

### **The repository can be found here:**  [HERE](https://github.com/GaryCooper-pm/PP3-Python-project)

---

## Acknowledgements

* Community over on Stack Overflow for code to create the 'typewriter effect for the player welcome text.
```
from time import sleep
import sys

for line in lines:
    for c in line:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.2)
    print('')
```

---

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
