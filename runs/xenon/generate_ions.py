import re
import numpy as np
import sys

W = 13.5
def parse_and_process_file(input_filename, output_filename):
    
    # Regex for parsing the input file
    creation_pattern = re.compile(r"# Gen (\d+) particle \d+ created with\s+(\d+\.\d+E[+-]\d+)\s+eV energy...")
    deposit_pattern = re.compile(r"# Gen (\d+) particle \d+ deposited\s+(\d+\.\d+E[+-]\d+)\s+eV.")
    coordinates_pattern = re.compile(r"\s+-?\d+\.\d+E[+-]\d+\s+(-?\d+\.\d+E[+-]\d+)\s+(-?\d+\.\d+E[+-]\d+)\s+(-?\d+\.\d+E[+-]\d+)")
    absorbed_pattern = re.compile(r"# Gen (\d+) particle \d+ tracked until it has\s+(\d+\.\d+E[+-]\d+)\s+eV and then absorbed\. Creating (\d+) ions:")

    # Dictionaries to hold energies and coordinates by generation
    deposited_energies = {}
    creation_energies = {}
    coordinates_by_gen = {}
    ions_by_absorption = {}
    energy_array = []

    # Reading the input file
    with open(input_filename, 'r') as file:
        current_history = None
        for line in file:
            
            if 'Begin history' in line:
                current_history = int(line.split()[2].strip(':'))
                deposited_energies[current_history] = {}
                creation_energies[current_history] = {}
                coordinates_by_gen[current_history] = {}
                ions_by_absorption[current_history] = {}

                next_line = next(file)
                energy_array.append( next_line.split()[-1] )
                
            elif '# Gen' in line:
                
                if 'created with' in line:
                    match = creation_pattern.search(line)
                    gen = int(match.group(1))
                    energy = float(match.group(2))
                    creation_energies[current_history].setdefault(gen, []).append(energy)
                    
                elif 'deposited' in line:
                    match = deposit_pattern.search(line)
                    gen = int(match.group(1))
                    deposited_energy = float(match.group(2))
                    coords_line = next(file)
                    coords = coordinates_pattern.search(coords_line)
                    x, y, z = coords.group(1), coords.group(2), coords.group(3)
                    deposited_energies[current_history].setdefault(gen, []).append(deposited_energy)
                    coordinates_by_gen[current_history].setdefault(gen, []).append((x, y, z))
                    
                elif 'tracked' in line:
                    match = absorbed_pattern.search(line)
                    gen = int(match.group(1))
                    energy = float(match.group(2))
                    num_ions = int(match.group(3))
                    
                    coords_line = next(file)
                    coords = coordinates_pattern.search(coords_line)
                    x, y, z = coords.group(1), coords.group(2), coords.group(3)
                    for n in range(num_ions):
                        ions_by_absorption[current_history].setdefault(gen, []).append((x, y, z))
                    

    # Process energies and output data
    with open(output_filename, 'w') as output_file:
        for history_num, history in enumerate(deposited_energies):
            output_file.write(f"\n# Begin history {history} with energy {energy_array[history_num]} keV:\n")
            
            # Write the ions created by absorption
            output_file.write("# Ions created by absorption - copied from PenRed output\n")
            for gen in ions_by_absorption[history_num+1]:
                output_file.write("## Gen {}\n".format(gen))
                for (x, y, z) in ions_by_absorption[history_num+1][gen]:
                    output_file.write(f"{x}  {y}  {z}\n")
            
            output_file.write("# Ions created by deposits - calculated from PenRed output\n")
            for gen in sorted(deposited_energies[history].keys()):
                
                output_file.write("## Gen {}\n".format(gen))
                
                deposits = deposited_energies[history][gen]
                coordinates = coordinates_by_gen[history][gen]

                # Pair and sort deposits and coordinates together based on energy
                paired = sorted(zip(deposits, coordinates), key=lambda x: x[0], reverse=True)
                deposits, coordinates = zip(*paired) if paired else ([], [])
                deposits = list(deposits)

                if gen + 1 in creation_energies[history]: # If energy deposits created new particles    

                    creations = sorted(creation_energies[history][gen + 1], reverse=True)
                    # Adjust the energy deposits
                    for i, creation_energy in enumerate(creations):
                        deposits[i] -= creation_energy

                # Write adjusted energies and corresponding ions
                for adjusted_energy, (x, y, z) in zip(deposits, coordinates):
                    num_ions = max(round(adjusted_energy / W), 1)  # Ensure non-negative ion count
                    for _ in range(num_ions):
                        output_file.write(f"{x}  {y}  {z}\n")
                        
def main():
    pen_file = sys.argv[1]
    out_file = sys.argv[2]
    parse_and_process_file(pen_file, out_file)
    print('Wrote to {}'.format(out_file))

if __name__=="__main__":
    main()
