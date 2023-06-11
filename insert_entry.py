import re

def insert_client_alphabetically(client_name, repo_link, file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_entry_line = f"| {client_name} | {repo_link} |\n"
    entry_regex = re.compile(r'\| .+ \| .+ \|')

    total_clients = 0

    inserted = False

    for index, line in enumerate(lines):
        if entry_regex.match(line):
            total_clients += 1
            curr_client_name = line.split('|')[1].strip()
            if client_name.lower() < curr_client_name.lower() and not inserted:
                lines.insert(index, new_entry_line)
                inserted = True
                total_clients += 1  

    if not inserted:
        lines.append(new_entry_line)
        total_clients += 1  

    header_index = next(i for i, line in enumerate(lines) if line.startswith("# Client Collection List"))
    lines[header_index] = f"# Client Collection List - Total Clients: {total_clients}\n"

    with open(file_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    client_name = input("Enter the new client's name: ")
    repo_link = input("Enter the new client's repository link: ")
    file_path = "README.md" 

    insert_client_alphabetically(client_name, repo_link, file_path)
