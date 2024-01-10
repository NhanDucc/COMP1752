# import database01 as db

# names = db.get_names()
# user_ids = db.get_user_ids()
# infos = db.get_infos()

# # print out all the user details
# for i in range(len(names)):
#     name = names[i]
#     user_id = user_ids[i]
#     info = infos[i]
#     print(f"name:      {name}")
#     if user_id is not None:
#         print(f"user id:   {user_id}")
#     if info is not None:
#         if info.startswith("BSc ") or info.startswith("MSc "):  # this is a student
#             print(f"programme: {info}")
#         else:  # this is a member of staff
#             print(f"job title: {info}")
#     print()

# while True:
#     group = input("Group (staff, students or all)? ")
#     if group == "":
#         break
#     message = input("Message? ")
#     if message == "":
#         break
#     for i in range(len(infos)):
#         info = infos[i]
#         send_message = False
#         if group == "all":
#             send_message = True
#         elif info is not None:
#             is_student = info.startswith("BSc ") or info.startswith("MSc ")
#             if group == "students" and is_student:
#                 send_message = True
#             if group == "staff" and not is_student:
#                 send_message = True
#         if send_message:
#             name = names[i]
#             print(f" '{message}' sent to {name}")

import database01 as db

def in_group(group, info):
    if group == "all":
        return True
    elif info is not None:
        is_student = info.startswith("BSc ") or info.startswith("MSc ")
        if group == "students" and is_student:
            return True
        elif group == "staff" and not is_student:
            return True
    return False

names = db.get_names()
user_ids = db.get_user_ids()
infos = db.get_infos()

# print out all the user details
for i in range(len(names)):
    name = names[i]
    user_id = user_ids[i]
    info = infos[i]
    print(f"name:      {name}")
    if user_id is not None:
        print(f"user id:   {user_id}")
    if info is not None:
        if info.startswith("BSc ") or info.startswith("MSc "):  # this is a student
            print(f"programme: {info}")
        else:  # this is a member of staff
            print(f"job title: {info}")
    print()

while True:
    group = input("Group (staff, students or all)? ")
    if group == "":
        break
    message = input("Message? ")
    if message == "":
        break
    for i in range(len(infos)):
        info = infos[i]
        if in_group(group, info):
            name = names[i]
            print(f" '{message}' sent to {name}")
