const fs = require('fs');

const lines = fs.readFileSync("input", "utf-8").split("\n");

let increases = 0;

let prev = parseInt(lines[0]);
for (line of lines) {
    let next = parseInt(line);
    if (next > prev) {
        increases ++;
    }
    prev = next;
}

console.log(increases);
