"""
PseudoCode：
FILENAME = "subject_data.txt"
function main()
subject_data = load_data()
call display_subject_details with subject_data as parameter
function load_data()
create empty list subject_data
open FILENAME for reading as input_file
for each line in input_file
remove newline from line
split line into parts by comma
convert parts[2] to integer
add parts to subject_data
return subject_data
function display_subject_details(subject_data)
for each subject in subject_data
unpack subject into subject_code, lecturer, student_count
display subject_code, lecturer, student_count in formatted string
"""

"""Read and display subject details from a data file."""

FILENAME = "subject_data.txt"


def main():
    """Main function to run the subject details program."""
    subject_data = load_data()
    display_subject_details(subject_data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    with open(FILENAME, 'r') as input_file:
        for line in input_file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data


def display_subject_details(subject_data):
    """Display details for each subject in the subject_data list."""
    for subject_code, lecturer, student_count in subject_data:
        print(f"{subject_code} is taught by {lecturer:12} and has {student_count:3} students")


main()
