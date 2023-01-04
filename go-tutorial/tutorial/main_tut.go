package main

import (
	"fmt"
	"math"
	"sort"
	"strings"
)

func sayGreeting(n string) {
	fmt.Println("Good morning", n)
}

func sayBye(n string) {
	fmt.Println("Bye bye", n)
}

func cycleNames(n []string, f func(string)) {
	for _, v := range n {
		f(v)
	}
}

func circleArea(r float64) float64 {
	return math.Pi * r * r
}

func getInitials(n string) (string, string) {
	s := strings.ToUpper(n)
	names := strings.Split(s, " ")

	var initials []string
	for _, v := range names {
		initials = append(initials, v[:1])
	}

	if len(initials) > 1 {
		return initials[0], initials[1]
	}
	return initials[0], "_"
}

func updateName(n *string) {
	*n = "Håkon"
}

func main() {
	fmt.Println("Hello hello!")

	// strings
	var nameOne string = "Håkon"
	var nameTwo = "Emma"
	var nameThree string

	fmt.Println(nameOne, nameTwo, nameThree)

	nameThree = "Apple"

	fmt.Println(nameOne, nameTwo, nameThree)

	nameFour := "Samsung"

	fmt.Println(nameOne, nameTwo, nameThree, nameFour)

	// integers
	var ageOne int = 20
	var ageTwo = 30
	ageThree := 40

	fmt.Println(ageOne, ageTwo, ageThree)

	// bits and memory
	var numOne int8 = 40
	var numTwo int8 = -128
	var numThree uint8 = 200

	fmt.Println(numOne, numTwo, numThree)

	// float

	var scoreOne float32 = 25.98
	var scoreTwo float64 = 124.42314

	fmt.Println(scoreOne, scoreTwo)

	// print
	fmt.Print("Hello\n")
	fmt.Print("Hello\n")

	fmt.Println("Automatic new line")

	age := 35
	name := "Shaun"

	fmt.Println("My age is", age, "and my name is", name)
	fmt.Printf("My age is %T and my name is %T\n", age, name)

	var str = fmt.Sprintf("My age is %v and my name is %v\n", age, name)
	fmt.Println(str)

	// arrays and slices

	var ages [3]int = [3]int{20, 25, 30}
	names := [4]string{"Hei", "på", "deg", "!"}

	fmt.Println(ages, len(ages), ages[2], names)

	// slices
	var scores = []int{1, 2, 3, 4, 5}
	scores[2] = 25
	scores = append(scores, 4)
	fmt.Println(scores)

	rangeOne := names[1:3]
	rangeTwo := names[2:]
	rangeThree := names[:4]
	fmt.Println(rangeOne, rangeTwo, rangeThree)

	// different packages
	// strings
	fmt.Println()
	greeting := "hello there friends!"
	fmt.Println(strings.Contains(greeting, "hello"))
	fmt.Println(strings.ReplaceAll(greeting, "hello", "hi"))
	fmt.Println(strings.ToUpper(greeting))
	fmt.Println(strings.Index(greeting, "ll"))
	fmt.Println(strings.Split(greeting, " "))

	// sort
	fmt.Println()
	numbers := []int{12, 24, 543, 234, 5, 43, 56, 364, 6}
	sort.Ints(numbers)
	fmt.Println(numbers)

	index := sort.SearchInts(numbers, 5)
	fmt.Println(index)
	letters := []string{"a", "A", "B", "b"}
	sort.Strings(letters)
	fmt.Println(letters)

	fmt.Println(sort.SearchStrings(letters, "B"))

	// loops
	fmt.Println()

	x := 0
	for x < 5 {
		fmt.Println("the value of x is", x)
		x++
	}

	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	for i := 0; i < len(letters); i++ {
		fmt.Println(letters[i])
	}

	for index, val := range letters {
		fmt.Println(index, val)
		val = "C"
	}

	fmt.Println(letters)

	// bools
	number := 25
	fmt.Println(number <= 50)
	fmt.Println(number >= 50)
	fmt.Println(number == 50)
	fmt.Println(number != 50)

	if number < 30 {
		fmt.Println("less than 30")
	} else if number < 40 {
		fmt.Println("less than 40")
	} else {
		fmt.Println("Not less than 40")
	}

	myNames := []string{"Sindre", "Amund", "Håkon"}
	fmt.Println()
	for index, value := range myNames {
		if index == 1 {
			fmt.Printf("continuing at pos %v\n", index)
			continue
		}

		fmt.Printf("the value at %v is %v\n", index, value)
	}

	fmt.Println()
	for index, value := range myNames {
		if index == 1 {
			fmt.Printf("breakes at pos %v\n", index)
			break
		}

		fmt.Printf("the value at %v is %v\n", index, value)
	}

	// functions
	sayGreeting("Mario")
	sayBye("Louigi")

	cycleNames([]string{"cloud", "tifa", "barret"}, sayGreeting)
	cycleNames([]string{"cloud", "tifa", "barret"}, sayBye)

	a1 := circleArea(12.4)
	a2 := circleArea(43.5)

	fmt.Println(a1, a2)
	fmt.Printf("a1: %0.3f. a2: %0.3f\n", a1, a2)

	// more functions
	fn1, sn1 := getInitials("Håkon Høksnes")
	fmt.Println(fn1, sn1)
	fn2, sn2 := getInitials("Håkon")
	fmt.Println(fn2, sn2)
	fn3, sn3 := getInitials("Amund Høksnes")
	fmt.Println(fn3, sn3)

	// package scope
	// from greetings.go
	// sayHello("Håkon")
	// go run main.go greetings.go

	// maps

	menu := map[string]float64{
		"soup":    4.99,
		"pie":     7.99,
		"salad":   6.99,
		"pudding": 3.55,
	}
	fmt.Println()
	fmt.Println(menu)
	fmt.Println(menu["salad"])

	for k, v := range menu {
		fmt.Printf("The price of %v is %v\n", k, v)
	}

	phonebook := map[int]string{
		95009077: "Håkon",
		99169507: "Emma",
		95061025: "Nina",
	}
	fmt.Println(phonebook)
	fmt.Println(phonebook[95009077])

	phonebook[95009077] = "Haakon"
	fmt.Println(phonebook)
	fmt.Println(phonebook[95009077])

	// pass by value
	fmt.Println()
	name2 := "hakon"
	m := &name2

	updateName(m)

	fmt.Println("memory adress of name is: ", &name2)
	fmt.Println("value at memory adress", *m)

	fmt.Println(name2)

}
