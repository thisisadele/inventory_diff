# inventory_diff
The program will find out the discrency on the system inventory from both sides. After finish, the problem will create 4 files. 
  - in_bb        <== S/N are found in the OR side, as well as in the BB side
  - not_in_bb    <== S/N are found in the OR side, but do not found in the BB side
  - in_or        <== S/N are found in the BB side, as well as in the OR sice
  - not_in_or    <== S/N are found in the BB side, but do not found in the OR side 


prerequisites:
  - create a inventory list called bb_list
  - create another inventory list called or_list
  
  
 To generate the report:
    $ python inventory_diff 
 
