# PenRed_Tracks
### A modified version of PenRed: [original repo](https://github.com/PenRed/PenRed)

## Usage

### Installation

1. Clone this repository on NERSC or Linux computer
2. Go into `src/`
3. Run `bash compile.sh`
4. After project is built, copy the executable into our runs folder: `cp compiled/mains/penmain/pen_main ../runs/xenon`

### Running
5. Go into runs folder: `cd ../runs/xenon` 
6. Run executable with provided config file: `./pen_main config.in`

### Post-processing
7. Get NERSC python: `module load python`
8. Process data to generate all ion positions and write to a new file: `python generate_ions.py <pen_output>.dat <processed_file>.dat`
9. The generated file `processed_file.dat` should be usable

## Notes

### What was modified?

Nothing in the PenRed simulation was changed, but a new tally was activated to keep track of energy deposit and absorption locations. 
This is the `tally/track` seen in the config file. 

PenRed does not explicitly keep track of ionization sites in the simulations, so they are estimated using the energy deposits.
The `generate_ions.py` script reads the simulation output and places ions where energy was deposited, assuming energy only goes into creating secondary electrons and ions. 
