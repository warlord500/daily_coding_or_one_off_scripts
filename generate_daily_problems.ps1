$pathDailyProblems = "D:\programming\daily_coding_problems"
#$pathEditor = 'D:\portable applications\windows\notepadplusplus\notepad++.exe'
$pathEditor = "C:\Program Files (x86)\Vim\vim90\gvim.exe"
#assume extra info is always supplied 
#code works if you just hit enter any way.
$extraInfo = Read-Host -Prompt "extra info for name"
$problemNumber = Read-Host -Prompt "problem number"

$dateDay = Get-Date -Format "dd"
$dateMonth = Get-Date -Format "MM"
$dateYear = Get-Date -Format "yyyy"

if(-NOT (test-Path "$pathDailyProblems\$dateYear" -PathType Container)) {
   New-Item  -Path "$pathDailyProblems\$dateYear" -ItemType directory
}

$currentMonth = (Get-Culture).DateTimeFormat.GetMonthName($dateMonth)
if(-NOT (test-Path "$pathDailyProblems\$dateYear\$currentMonth" -PathType Container)) {
	New-Item  -Path "$pathDailyProblems\$dateYear\$currentMonth" -ItemType directory
}




$fullPath = "$pathDailyProblems\$dateYear\$currentMonth\p$dateMonth-$dateDay$extraInfo"

#split this two different ways
if ($extraInfo -like "*-rust"){ 
#check for -rust at the end to generate rust project

	cargo new --vcs none $fullPath 
	& ($pathEditor)  "$fullPath/src/main.rs" "$fullPath/cargo.toml" 
	#& ('git-bash.exe') $fullPath
} else {
# not sure if that works 
$fullPath = "$fullPath.py" 

	echo "#!/bin/python" >> $fullPath;
	echo "#problem number: $problemNumber" >> $fullPath;
	echo "def $extraInfo():" >> $fullPath;
	echo '	return "hello world"' >> $fullPath;
	echo "" >> $fullPath;
	echo "" >> $fullPath;
	echo 'if __name__ == "__main__":' >> $fullPath;
	echo "	print($extraInfo())" >> $fullPath;

	& ($pathEditor)  $fullPath
}
# end else