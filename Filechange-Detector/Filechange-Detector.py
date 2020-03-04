import os, hashlib
from os import path

#Collects the location of the folder to overlook and the location for the log file
current_location = path.dirname(__file__)
file_to_overlook = path.join(current_location, "./"+"YOUR-FILENAME")
log_file = str(current_location) + "/" + "YOUR-FILENAME"

#Gets the location of all items in the file
def get_all_items(file_to_overlook):
    all_items = []

    for item in os.listdir(file_to_overlook):
        
        file_items = file_to_overlook + "/" + item
        
        if(path.isdir(file_items) == True):
            all_items += get_all_items(file_items)

        else:
            all_items.append(file_items)

    return all_items

#If the log file exists, looks through the file and 
try:
    changes = False
    removed = False
    added = False
    
    added_files = []
    removed_files = []
    existing_files = []
    changed_files = []
    hash_current_files = []

    log_items = []
    log_hashes = []

    with open(log_file) as log_to_read:
        read_log = log_to_read.readlines()
    read_log = [back_n.strip() for back_n in read_log]

    #separates the name of the file from its hash value
    for string in read_log:
        separator = string.index(" : ")

        log_items.append(string[0:separator])    

        log_hashes.append(string[(separator + 3):])

    #Detects if the hashed content of all files currently in the folder are the same as in the log file
    for file_to_hash in get_all_items(file_to_overlook):
        
        with open(file_to_hash, "r") as content_to_hash:
            hashed_content = content_to_hash.readlines()
        
        hashed_content = [back_n.strip() for back_n in hashed_content]

        sha256 = hashlib.sha256()
        
        sha256.update(str(hashed_content).encode("utf-8"))
        
        file_hash = sha256.hexdigest()
        
        hash_current_files.append(file_to_hash + " : " + file_hash)

    #Detects if there are more or less items in the folder
    for item in get_all_items(file_to_overlook):        

        if (len(log_items) <= len(get_all_items(file_to_overlook))):
            existing_files.append(item)

        if (len(log_items) >= len(get_all_items(file_to_overlook))):    
            existing_files.append(item)

    #Gets the removed files and puts them in the removed file list
    for item in range(len(log_items)):
    
        if (log_items[item] not in existing_files):
            
            removed = True

            removed_files.append(log_items[item])
    
    #Gets the added files and puts them in the added file list
    for item in range(len(existing_files)):
        
        if(existing_files[item] not in log_items and existing_files[item] not in added_files):
        
            added = True

            added_files.append(existing_files[item])

    #If the hash value of a certain file has been altered it will be detected here
    for item in read_log:
        if(item in hash_current_files):
            del hash_current_files[hash_current_files.index(item)]

    for item in hash_current_files:
        if item not in read_log:
            changes = True
            changed_files.append(item)

    for item in changed_files:
        separator = item.index(" : ")

        if(item[0:separator] in added_files):
            del changed_files[changed_files.index(item)]
            
        if(item[0:separator] in removed_files):
            del changed_files[changed_files.index(item)]
    
    #if files have been changed
    if (changes == True):

        print("The folowing file(s) have been changed\n")
        print(*changed_files, sep="\n")

        item_to_log = {}

        outfile = open(log_file, "w+")
        
        #updates the log file
        for item in get_all_items(file_to_overlook):
        
            with open(item, "r") as content_to_hash:
                hashed_content = content_to_hash.readlines()
            
            hashed_content = [back_n.strip() for back_n in hashed_content]
            
            sha256 = hashlib.sha256()
            
            sha256.update(str(hashed_content).encode("utf-8"))
            
            file_hash = sha256.hexdigest()

            item_to_log[str(hashed_content)] = file_hash 

            outfile.write(item + " : " + item_to_log[str(hashed_content)])
            
            outfile.write("\n")

        outfile.close()
        
    #if files have been added
    if(added == True):
        print("These files have been added:\n")
        print(*added_files, sep="\n")
        
        item_to_log = {}

        outfile = open(log_file, "w+")
        
        #updates the log file
        for item in get_all_items(file_to_overlook):
        
            with open(item, "r") as content_to_hash:
                hashed_content = content_to_hash.readlines()
            
            hashed_content = [back_n.strip() for back_n in hashed_content]
            
            sha256 = hashlib.sha256()
            
            sha256.update(str(hashed_content).encode("utf-8"))
            
            file_hash = sha256.hexdigest()

            item_to_log[str(hashed_content)] = file_hash 

            outfile.write(item + " : " + item_to_log[str(hashed_content)])
            
            outfile.write("\n")

        outfile.close()

    #if files have been removed
    if(removed == True):
        print("These files have been removed:\n")
        print(*removed_files, sep="\n")
        
        item_to_log = {}

        outfile = open(log_file, "w+")

        #updates the log file
        for item in get_all_items(file_to_overlook):
        
            with open(item, "r") as content_to_hash:
                hashed_content = content_to_hash.readlines()
            
            hashed_content = [back_n.strip() for back_n in hashed_content]
            
            sha256 = hashlib.sha256()
            
            sha256.update(str(hashed_content).encode("utf-8"))
            
            file_hash = sha256.hexdigest()

            item_to_log[str(hashed_content)] = file_hash 

            outfile.write(item + " : " + item_to_log[str(hashed_content)])
            
            outfile.write("\n")

        outfile.close()

    #if nothing has changed
    if(changes == False and added == False and removed == False):
        print("No changes")

#If the log file does not already exist ceate one
except FileNotFoundError:

    item_to_log = {}

    outfile = open(log_file, "w+")

    for item in get_all_items(file_to_overlook):
        
        with open(item, "r") as content_to_hash:
            hashed_content = content_to_hash.readlines()
        
        hashed_content = [back_n.strip() for back_n in hashed_content]
        
        sha256 = hashlib.sha256()
        
        sha256.update(str(hashed_content).encode("utf-8"))
        
        file_hash = sha256.hexdigest()

        item_to_log[str(hashed_content)] = file_hash 

        outfile.write(item + " : " + item_to_log[str(hashed_content)])
        
        outfile.write("\n")

    outfile.close()