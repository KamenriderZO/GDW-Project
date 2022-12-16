import os
from random import randrange
import shutil
import glob
# Install tensorflow if you don't have it installed yet :D
import tensorflow

# Temporary path buffer, for convenience
projectPath01 = "C:/UNI/Uni WiSe 22-23/GDW/ProjectPizza/train"
projectPath02 = "C:/Users/Marcel/Desktop/Universitaet/2022W/GrundlagenDatenWissenschaften/GDW-Project/train"
projectPath03 = ""
projectPath04 = ""

# Path concatinations from project
relativePizzaDir = "/pizza"
relativeNonPizzaDir = "/not_pizza"
relativeMixedFoodDir = "/mixedFood"

# Directories of pizza and not_pizza. Manually change projectPaths depending on local environment.
pizzaDir = projectPath01 + relativePizzaDir
nonPizzaDir = projectPath01 + relativeNonPizzaDir
mixedFoodDir = projectPath01 + relativeMixedFoodDir

# Amount of pictures per directory
pizzaDir = os.listdir(pizzaDir)
nonPizzaDir = os.listdir(nonPizzaDir)

def randomizeFoodPictures():
    selectedPizza = []
    selectedNonPizza = []

    # Get random amount of random pizza images
    for i in range(randrange(len(pizzaDir))):
        # The selected random picture
        randomPic = randrange(len(pizzaDir))
       # print(randomPic)
        # Add picture to list if not already added
        if randomPic not in selectedPizza:
            selectedPizza.append(pizzaDir[randomPic])

    # Get random amount of random non-pizza images
    for i in range(randrange(len(nonPizzaDir))):
        # The selected random picture
        randomPic = randrange(len(nonPizzaDir))
       # print(randomPic)
        # Add picture to list if not already added
        if randomPic not in selectedNonPizza:
            selectedNonPizza.append(pizzaDir[randomPic])

    # Creates the mixedFood directory, if it doesn't exist
    if not os.path.exists(mixedFoodDir):
        os.makedirs(mixedFoodDir)

    # TODO mix both arrays and copy files towards outputDirectory

    print(len(selectedPizza))
    print(selectedPizza)
    print(len(selectedNonPizza))
    print(selectedNonPizza)

# Main function of the class
def main():
    randomizeFoodPictures()

# ... some python specific ... thing?
if __name__ == "__main__":
    main()
