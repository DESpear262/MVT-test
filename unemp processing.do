clear

use "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\State Unemp Working.dta"
rename value val_19
gen is_19 = (mod(2020,year))
drop if period !=  "M04"
gen val_20 = (val_19[_n+1]*is_19)
drop if year == 2020
drop period label monthchange
drop is_19
drop year
gen unemp_chg = (val_20-val_19)

save use "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\State Unemp Processed.dta"

clear