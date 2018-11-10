current_users=('funyoung','plain','ariel','phil','jack')
new_users=['lucy','harry','funyoung','selina','Jack']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('this username already exists please input other user_name')
    else:
        print('you can use this name')