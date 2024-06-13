import random

# Predefined dictionary with already allotted berths and their genders
# Testing
# alloted = {
#     1: "Male", 4: "Female", 7: "Female", 10: "Male",
#     13: "Female", 16: "Male", 19: "Female", 22: "Male", 24: "Female"
# }


def berth_allotment(alloted, gender):
    """
    Function to allot a berth based on availability and gender preference.

    Parameters:
    alloted (dict): Dictionary with berth numbers as keys and genders as values
    gender (str): Gender of the person for whom the berth is being allotted

    Returns:
    int or None: Allotted berth number or None if all berths are occupied
    """
    # If all berths are already allotted, return None
    if len(alloted) == 24:
        return None

    while True:
        # Generate a random berth number between 1 and 24
        berth = random.randint(1, 24)

        # Check if the generated berth is not already allotted
        if berth not in alloted:
            # Check the conditions for berth allotment based on gender and adjacency
            if berth % 3 == 2:
                if berth - 1 not in alloted:
                    return berth
                elif gender == "Female" and alloted[berth - 1] == "Female":
                    return berth
                elif gender == "Male" and alloted[berth - 1] == "Male":
                    return berth
            elif berth % 3 == 1:
                if berth + 1 not in alloted:
                    return berth
                elif gender == "Female" and alloted[berth + 1] == "Female":
                    return berth
                elif gender == "Male" and alloted[berth + 1] == "Male":
                    return berth
            else:
                return berth

    # In case of any issue, re-attempt to generate a valid berth
    while True:
        berth = random.randint(1, 24)
        if berth not in alloted:
            return berth
#Testing
# while True:
#     gender=input("Enter your gender : ")
#     berth=berth_allotment(alloted,gender)
#     if berth is None:
#         print("All berths are occupied")
#         break
#     print(berth)
#     print(alloted)
#     alloted[berth]=gender