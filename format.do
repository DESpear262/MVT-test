clear

use "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\State Unemp Working.dta"
rename seriesid state
label variable state "2 letter state code"
save "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\State Unemp Working.dta", replace
clear

use "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\CPVI gov.dta"
rename dt dist
rename pvi gov
save "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\CPVI gov.dta", replace
clear


use "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\CPVI red.dta"
rename pvi red
save "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\CPVI red.dta", replace
clear

use "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\CPVI swing.dta"
rename pvi swing
save "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\CPVI swing.dta", replace
clear


use "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\CD COVID Working epi.dta"
rename v1 dist
rename v4 deaths
keep deaths dist
save "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\CD COVID Working epi.dta", replace
clear