var numbers = [];
for (let i = 1; i <= 10; i++) {
	numbers.push(i);
}


numbers = numbers.filter((n) => { return n % 2 === 0; });

console.log(numbers);
