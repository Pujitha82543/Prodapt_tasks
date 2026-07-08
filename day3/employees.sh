echo "Enter log file:"

read logfile

if [[ ! -f $logfile ]]

then

        echo "File not exsist"

        exit

fi

echo "EMPID NAME SALARY TAX BONUS NET">payroll_report.txt

while IFS=',' read id name salary

do

        if ((salary <= 30000 ));then

                tax=$((salary*5/100))

        elif ((salary >= 30001)) && ((salary <= 60000))

        then

                tax=$((salary*10/100))

        else

                tax=$((salary*15/100))

        fi

        if ((salary <= 50000 ))

        then

                bonus=2000

        else

                bonus=5000

        fi

        net=$(( salary-tax+bonus))

echo "$id $name $salary $tax $bonus $net">>payroll_report.txt

done<"$logfile"

echo "Payroll report generated: payroll_report.txt"

 
