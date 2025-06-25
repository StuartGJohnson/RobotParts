# RobotParts
Miscellaneous robot parts - generated from known robot dimensions with cadquery in python. Likely I will upload the robot XACRO here as well. Note that since these robot parts are highly correlated with the robot itself (which is generated from scratch from geometric primitives), it makes a lot of sense that these parts are generated from geometric primitives.

If you aren't a frequent CAD user, this is a lot faster than trying to get CAD SW to bend to your will!

## Robot ARUCO tag mount plate.

[Aruco tag plate](tag_plate.stl)

(GitHub has a very nice built-in STL viewer! But you gotta click that link.)

First part! This part velcros to the top of the robot compute (an NVIDIA Orin AGX) and allows connection of an Aruco tag via M3 standoffs (to get the tag above the Lidar). More adjustments will follow after inspection of the part (my first 3d printed part).

First cut part print was from:

[craftcloud](https://craftcloud3d.com/)

## Usage

All usage is by running unit tests (see the code). I have installed cadquery via conda/mamba and point my pycharm at that conda env. Code completion and introspection of cadquery is worth its weight in gold when trying to generate a CAD file. And GPT4o was a lot of help as well!

## Gotchas

`cadquery` installation was initially a challenge as I had a conda base install based on an old python version (3.8). I believe this was caused by an Ubuntu 20.04 to 22.04 upgrade. This caused infinite churn in conda's dependency management ("Solving Environment"). GPT4o had a great suggestion of introducing a new conda python env (based on python 3.10) for dependency management (and install of mamba). `cadquery` install was very quick after this.

## Credit/References

- [cadquery](https://github.com/CadQuery/cadquery)

- This code was developed with some assistance from ChatGPT4o (OpenAI, June 2025). Actually, once I knew what I wanted to do, GPT4o suggested using cadquery.