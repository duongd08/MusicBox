import musicbox
m = musicbox.MusicBox()

NOTES = [("C", 60), ("D", 62), ("E", 64), ("F", 65), ("G", 67), ("A", 69), ("B", 71)]
MAJOR_SCALES_INTERVALS = [2, 2, 1, 2, 2, 2, 1]
MINOR_SCALES_INTERVALS = [2, 1, 2, 2, 1, 2, 2]
MAJOR_TRIAD_INTERVALS = [0, 4, 7]
MINOR_TRIAD_INTERVALS = [0, 3, 7]

# get_notes() asks user to input notes then split notes into list of strings
# then create an empty list
# iterate through the list of notes and converts notes into integers corresponding to NOTES
# then append the integers into a new list of integers


def get_notes():
    sequence = str(input("Please enter a sequence of notes separated by spaces: "))
    sequence_split = sequence.split(" ")
    note_tuple = []
    for x in sequence_split:
        note_tuple.append(note_to_int(x))
    return note_tuple

# note_to_int(note) converts notes to integers corresponding to NOTES
# if notes does not correspond to any notes in NOTES, then function returns -1


def note_to_int(note):
    for n in NOTES:
        (note_str, integer) = n
        if note[0] == note_str:
            if note == note_str + "b":
                return integer - 1
            elif note == note_str + "#":
                return integer + 1
            else:
                return integer
        else:
            pass
    return -1

# play_notes(notes) use the list of integers returned from get_notes() to put into musicbox
# whenever note == -1, function say recognize error

def play_notes(notes):
    for note in notes:
        if note == -1:
            print("I don't know this note.")
            print()
        else:
            m.play_note(note, 500)

# get_triad() converts user into note and type then call note_to_int(note) to convert to integer value then return the tuple

def get_triad():
    triad = input("Please enter a triad name (Ex: C major): ")
    space = triad.find(" ")
    if space - 1 == 0:
        note = note_to_int(triad[:1])
    else:
        note = note_to_int(triad[:2])
    type = triad[space + 1:]
    if type != "major" and type != "minor":
        type = "invalid"
    triad_tuple = (note, type)
    return triad_tuple

# note_to_triad(triad_tuple) uses what's returned from get_triad to convert the tuple to a list of integers corresponding to the triad the user wants

def note_to_triad(triad_tuple):
    (note, type) = triad_tuple
    if type == "major":
        return [note + MAJOR_TRIAD_INTERVALS[0], note + MAJOR_TRIAD_INTERVALS[1], note + MAJOR_TRIAD_INTERVALS[2]]
    elif type == "minor":
        return [note + MINOR_TRIAD_INTERVALS[0], note + MINOR_TRIAD_INTERVALS[1], note + MINOR_TRIAD_INTERVALS[2]]

# play_triad(triad) plugs the list of integers corresponding to the triad the user wants into the music box

def play_triad(triad):
    m.play_chord(triad, 1500)

# get_scales() asks user to into name of a scale, splits the user input into a note and a type, call note_to_int to convert note into an integer in NOTES
# returns a tuple = (note, type)

def get_scales():
    scale = input("Please enter a scale name (Ex: C major): ")
    space = scale.find(" ")
    if space - 1 == 0:
        note = note_to_int(scale[:1])
    else:
        note = note_to_int(scale[:2])
    type = scale[space + 1:]
    if type != "major" and type != "minor":
        type = "invalid"
    scale_tuple = (note, type)
    return scale_tuple

# note_to_scale(scale_tuple) converts a tuple into a list of note integers depending on whether the type is a major or a minor

def note_to_scale(scale_tuple):
    (note, type) = scale_tuple
    if type == "major":
        scale_list = [note]
        for i in MAJOR_SCALES_INTERVALS:
            note_scale = note + i
            note = note_scale
            scale_list.append(note)
        return scale_list
    elif type == "minor":
        scale_list = [note]
        for i in MINOR_SCALES_INTERVALS:
            note_scale = note + i
            note = note_scale
            scale_list.append(note)
        return scale_list

# play_scale calls note_to_scale to convert the scale_tuple to a list of integers
# then for each integer in that list, plug it into the music box
# then call play_triad to play the corresponding triad

def play_scale(scale_tuple):
    notes = note_to_scale(scale_tuple)
    for note in notes:
        m.play_note(note, 500)
    play_triad(note_to_triad(scale_tuple))

# main() presents a menu, ask user for a choice
# then call get_notes, get_triad, or get_scales according to the user's choice
# else the program terminates

def main():
    menu = 0
    cont = True
    while cont == True:
        print("Main Menu:")
        print("1. Play Notes")
        print("2. Play Triad")
        print("3. Play Scale")
        print("4. Quit")
        menu = int(input("Please enter a selection: "))
        if menu == 1:
            notes_tuple = get_notes()
            play_notes(notes_tuple)
            print()
            menu = 0
            cont = True
        elif menu == 2:
            triad_tuple = get_triad()
            (note, type) = triad_tuple
            if note == -1:
                print("I don't know that triad.")
                print()
                menu = 0
            elif type == "invalid":
                print("I don't know that triad.")
                print()
                menu = 0
            else:
                triad = note_to_triad(triad_tuple)
                play_triad(triad)
                print()
                menu = 0
            cont = True
        elif menu == 3:
            scale_tuple = get_scales()
            (note, type) = scale_tuple
            if note == -1:
                print("I don't know that scale.")
                print()
                menu = 0
            elif type == "invalid":
                print("I don't know that scale.")
                print()
                menu = 0
            else:
                play_scale(scale_tuple)
                print()
                menu = 0
            cont = True
        elif menu == 4:
            print("Have a good day!")
            cont = False
        else:
            print("Please select options 1-4.")
            cont = True

main()
m.close()




