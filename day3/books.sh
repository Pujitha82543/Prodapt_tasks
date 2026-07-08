FILE="books.txt"
 
###########################################
# Display all books
###########################################
display_books() {
 
    echo "=========== Books ==========="
 
    cat "$FILE"
 
}
 
###########################################
# Search Book
###########################################
search_book() {
 
    echo "Enter Book Name:"
    read name
 
    if grep -i "$name" "$FILE"
    then
        echo "Book Found"
    else
        echo "Book Not Found"
    fi
 
}
 
###########################################
# Count Out of Stock
###########################################
count_out() {
 
    count=$(grep -c "Out Of Stock" "$FILE")
 
    echo "Out of Stock Books : $count"
 
}
 
###########################################
# Update Book Stock
###########################################
update_book_stock() {
 
    echo "Enter Book ID:"
    read id
 
    sed -i "/^$id,/ s/Out Of Stock/Available/" "$FILE"
 
    echo "Book Stock Updated Successfully"
 
}
 
###########################################
# Total Inventory Value
###########################################
calculate_total() {
 
    total=$(awk -F',' '$4=="Available" {sum+=$5} END {print sum}' "$FILE")
 
    echo "Total Inventory Value : Rs.$total"
 
}
 
###########################################
# Display Books by Category
###########################################
department_records() {
 
    echo "Enter Book Categeory:"
    read dept
 
    awk -F',' -v dep="$dept" '
 
    BEGIN{
        print "Books in Category:",dep
    }
 
    $3==dep{
        print $0
    }
 
    ' "$FILE"
 
}
 
###########################################
# Costliest Book
###########################################
highest_book() {
 
    awk -F',' '
 
    BEGIN{
        max=0
    }
 
    {
        if($5>max)
        {
            max=$5
            emp=$2
        }
    }
 
    END{
        print "Highest Cost Book :",emp
        print "Cost :",max
    }
 
    ' "$FILE"
 
}
 
###########################################
# Menu
###########################################
 
while true
do
 
echo
echo "====================================="
echo " Books Management"
echo "====================================="
echo "1.Display all books"
echo "2.Search book"
echo "3.Count Out Of Stock books"
echo "4.Update Book Stock"
echo "5.Total Inventory Value"
echo "6.Display books by category"
echo "7.Costliest book"
echo "8.Exit"
 
echo "Enter Choice:"
read choice
 
case $choice in
 
1)
display_books
;;
 
2)
search_book
;;
 
3)
count_out
;;
 
4)
update_book_stock
;;
 
5)
calculate_total
;;
 
6)
department_records
;;
 
7)
highest_book
;;
 
8)
echo "Thank You"
break
;;
 
*)
echo "Invalid Choice"
 
esac
 
done

