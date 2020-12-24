drone1 = [input()]
drone2 = [input()]
couples = ["dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
   "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"]
company1 = couples[0].split('-')
company2 = []
# create certain list for certain company
for n in range(1, len(couples)):
    one_couple=couples[n].split('-')
    if one_couple[0] in company1 or one_couple[1] in company1:
        company1+=one_couple
    else:
        company2+=one_couple
if set(drone1).issubset(company1) and set(drone2).issubset(company1) or set(drone1).issubset(company2) and set(drone2).issubset(company2):
    print('True')
else:
    print('False')