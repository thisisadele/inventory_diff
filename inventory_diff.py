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
                    
with open("or_list") as or_h:
     or_sn = or_h.readlines()
     # converting the list to the lower case
     or_sn = [ j.lower() for j in or_sn ]
     open("in_or","w").close()
     open("not_in_or","w").close()
     with open("bb_list") as bb_h:
         for i in bb_h:
             if i.lower() in or_sn:
                 with open("in_or", "a") as fh_in_o:
                     fh_in_o.write(i)
             else:
                 with open("not_in_or","a") as fh_not_o:
                     fh_not_o.write(i)

