package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getInput(promt string, r *bufio.Reader) (string, error) {
	fmt.Print(promt)
	input, err := r.ReadString('\n')

	return strings.TrimSpace(input), err
}

func createBill() bill {
	reader := bufio.NewReader(os.Stdin)

	name, _ := getInput("Create a new bill name: ", reader)

	b := newBill(name)
	fmt.Println("Created the bill - ", b.name)

	return b
}

func promtOptions(b bill) {
	reader := bufio.NewReader(os.Stdin)

	opt, _ := getInput("Choose option (a - add item, s - save bill, t - add tip): ", reader)
	switch opt {
	case "a":
		name, _ := getInput("What would you like to add? ", reader)
		price, _ := getInput("What is the price? ", reader)
		p, err := strconv.ParseFloat(price, 64)
		if err != nil {
			fmt.Println("The price must be a number")
			promtOptions(b)
		}
		b.addItem(name, p)
		fmt.Println("Added: ", name, price)
		promtOptions(b)
	case "t":
		tip, _ := getInput("Tip amount ($): ", reader)
		t, err := strconv.ParseFloat(tip, 64)
		if err != nil {
			fmt.Println("The tip must be a number")
			promtOptions(b)
		}
		b.updateTip(t)
		fmt.Println("Tip updated: ", tip)
		promtOptions(b)
	case "s":
		b.save()
	default:
		fmt.Println("Not an valid option...")
		promtOptions(b)
	}
}

func main() {
	mybill := createBill()
	promtOptions(mybill)
}

// mybill := newBill("Håkon's bill")
// mybill.addItem("beef", 7.99)
// mybill.addItem("pie", 5.99)
// mybill.addItem("cake", 3.99)
// mybill.updateTip(10)
// fmt.Println(mybill.format())
