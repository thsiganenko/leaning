var animals = ['cat', 'dog', 'rat'];
for (let i = 0, len = animals.length; i < len; i++) {
	animals[i] += 's';
}
console.log(animals);
// console.log(animals.map((s) => { return s + 's'; }));
