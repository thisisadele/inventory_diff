with open("bb_list") as bb_h:
     bb_sn = bb_h.readlines()
     # converting the list to the lower case
     bb_sn = [ j.lower() for j in bb_sn ]
     open("in_bb","w").close()
     open("not_in_bb","w").close()
     with open("or_list") as or_h:
         for i in or_h:
             if i.lower() in bb_sn:
                 with open("in_bb", "a") as fh_in:
                     fh_in.write(i)
             else:
                 with open("not_in_bb","a") as fh_not:
                     fh_not.write(i)
