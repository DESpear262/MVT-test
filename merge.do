clear

use "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\CPVI swing.dta"

merge 1:1 dist using "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\CPVI red.dta", nogen

merge 1:1 dist using "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\CPVI gov.dta", nogen

merge 1:1 dist using "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\CPVI red.dta", nogen

merge 1:1 dist using "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\CD COVID Working epi.dta", nogen

merge 1:1 dist using "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\CD Spending Working.dta", nogen

merge 1:1 dist using "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\CD COVID Working epi.dta", nogen

merge m:1 state using "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\State Unemp formatted.dta", nogen

drop incumbent clinton trump obama romney

save "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\merged data.dta", replace