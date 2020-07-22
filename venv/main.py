from volumes import cubevolume, pyramidvolume, ellipsoidvolume
prompt = True

#This is where I create my various lists.
shapes = []
cubes = []
pyramids = []
ellipsoids = []

#This is the loop that prompts the user to choose a shape. Once a shape is chosen, it then runs the corresponding function from the volumes file.
#Once the volume is returned from the function in the volumes file, the volume is added to the corresponding list.
while prompt == True:
    #Requesting valid shape input from the user
    shapes.append(input("Enter a shape: "))
    shapes[-1] = shapes[-1].lower()

    #If the user inputs "q" or "quit" with any combination of upper and lowercase characters, it ends the session.
    #It quits by setting the "prompt" variable to "False", and thus ending the while loop.
    if "q" in shapes or "quit" in shapes:
        prompt = False
        del shapes[-1]
        print("")
        print("You have reached the end of your session.")
        cubes.sort()
        pyramids.sort()
        ellipsoids.sort()

    #This is where the "cubevolume" function from the volumes file is called.
    elif shapes[-1] == "cube" or shapes[-1] == "c":
        shapes[-1] == "cube"
        cubes.append(cubevolume())

    #This is where the "pyramidvolume" function from the volumes file is called.
    elif shapes[-1] == "pyramid" or shapes[-1] == "p":
        shapes[-1] == "pyramid"
        pyramids.append(pyramidvolume())

    #This is where the "ellipsoidvolume" function from the volumes file is called.
    elif shapes[-1] == "ellipsoid" or shapes[-1] == "e":
        shapes[-1] == "ellipsoid"
        ellipsoids.append(ellipsoidvolume())

    #if the user's input is invalid, this prints "Invalid input." on the screen, removes the input from the shapes list, and continues the list.
    else:
        print("Invalid input.")
        del shapes[-1]
    print("")

#This is where the final output is pieced together.
#If no shapes were entered at all, is will state that "You did not perform any volume calculations."
#If nothing was entered for any specific shape, then that shape will say "No shapes entered."
if len(shapes) == 0:
    print("You did not perform any volume calculations.")
else:
    print("The volumes calculated for each shape are:")
    if len(cubes) > 0:
        print("Cube:",str(cubes)[1:-1])
    else:
        print("Cube: No shapes entered.")

    if len(pyramids) > 0:
        print("Pyramid:",str(pyramids)[1:-1])
    else:
        print("Pyramid: No shapes entered.")

    if len(ellipsoids) > 0:
        print("Ellipsoid:",str(ellipsoids)[1:-1])
    else:
        print("Ellipsoid: No shapes entered.")

