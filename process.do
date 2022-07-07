clear

use "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\Data\Stata\merged data.dta"

eststo: reg spendingbillion swing red gov deaths unemp_chg

esttab using "C:\Users\s94da\Desktop\Data and Do-files for papers and homework\Papers\Median Voter COVID\results.tex", title("How predictive pandemic severity and political polarization are of COVID relief spending") append
est clear