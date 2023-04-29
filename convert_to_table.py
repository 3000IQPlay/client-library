def convert_to_table(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        outfile.write("# Client Collection List\n\n")
        outfile.write("This repository contains a comprehensive list of various clients. Please note that **some clients might contain RATs (Remote Access Trojans)**. Use them at your own risk.\n\n")
        outfile.write("| Client Name         | Repository Link                                          |\n")
        outfile.write("|---------------------|-----------------------------------------------------------|\n")

        for line in infile:
            if " - " in line:
                client_name, link = line.strip().split(" - ", 1)
                outfile.write(f"| {client_name:<19} | {link:<55} |\n")
        
        outfile.write("\n## Disclaimer\n\n")
        outfile.write("This list is provided for informational purposes only. The repository owner does not endorse or support any of the listed clients. Use these clients at your own risk and ensure you understand the potential risks involved.")

convert_to_table('README.md')
