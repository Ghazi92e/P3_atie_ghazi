**Help MacGyver to escape !**

A maze game whose goal is to help MacGyver escape by collecting 3 objects: a needle, a plastic tube and ether to be able to make a syringe and put the guardian to sleep! This game was made thanks to pygame.

The main features of this program are: -There is only one level. The structure (start, location of the walls, finish) should be saved in a file to easily modify it if necessary.

-MacGyver will be controlled by the directional keys on the keyboard.

-The objects will be distributed randomly in the maze and will change location if the user closes the game and relaunches it.

-The game window will be a square that can display 15 sprites in length.

-MacGyver will therefore have to move from square to square, with 15 squares along the length of the window!

-It will pick up an item simply by moving over it.

-The program stops only if MacGyver has successfully retrieved all the objects and found the exit of the labyrinth. If he does not have all the items and he appears in front of the guard, he dies (life is cruel for the heroes).

-The program will be standalone, that is to say that it can be executed on any computer.


##
**To install MacGyver game**
##

1. Clone the repository: "git clone https://github.com/Ghazi92e/P3_atie_ghazi.git"
2. Create a virtual env: "python -m venv env" 
3. Activate the virtual env: "env\Scripts\activate"
4. Install packages from requirements.txt: "pip install -r requirements.txt"
5. In the folder "\P3_atie_ghazi" create a file setup.py with this configuration: 
```
from cx_Freeze import setup, Executable

setup(
    name="MacgyverGame",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["ressources",
                                             "modules", "map.txt"]}},
    description="Game MacGyver",
    executables=[Executable("main.py")],
)
```
6. Compile with this command: "python.exe setup.py build"
7. Open the folder build -> exe.win-amd64-3.8 and double click on main.exe

**Enjoy !!** 
