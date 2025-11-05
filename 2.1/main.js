function string_sum(str) {
    return Array.from(str).reduce((sum, d) => sum + Number(d), 0);
}

function keep_evens(arr) {
    return arr.filter(n => n % 2 === 0);
}

let x = [
    {name: 'Paul', age: 60},
    {name: 'Sue', age: 40},
    {name: 'Frank', age: 70},
    {name: 'Mom', age: 90}
];
let over40 = x.filter(obj => obj.age > 40);

function find_max(arr) {
    return Math.max(...arr);
}

function find_max_min(arr) {
    return {max: Math.max(...arr), min: Math.min(...arr)};
}

function sum_double(arr) {
    return 2 * arr.reduce((s, n) => s + n, 0);
}

function sum_double_evens(arr) {
    return 2 * arr.filter(n => n % 2 === 0).reduce((s, n) => s + n, 0);
}

function capitalize_firsts(str) {
    return str.split(" ").map(word =>
        word.charAt(0).toUpperCase() + word.slice(1)
    ).join(" ");
}

function longest_word(str) {
    return str.split(/[\s.]+/).reduce((a, w) => w.length > a.length ? w : a, "");
}

function longest_shortest_word(str) {
    let words = str.split(/[\s.]+/);
    return {
        longest: words.reduce((a, w) => w.length > a.length ? w : a, ""),
        shortest: words.reduce((a, w) => w.length < a.length ? w : a, words[0])
    };
}

function digits_only(str) {
    return Array.from(str).filter(c => /\d/.test(c));
}

const add = (a, b) => a + b;

const makesTen = (a, b) => (a === 10 || b === 10 || a + b === 10);

const person = {name: 'Paul', school: 'TJ', year: 2025};
const {school, year} = person;

function complimentCats(name, numCats) {
    return `Hello, ${name}. Did you know I have ${numCats} cats. It's a whole vibe.`;
}