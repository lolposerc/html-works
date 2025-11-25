const salaries = {
    ivan: 1200,
    maria: 1500,
    petr: 1100,
    anna: 1600
};

let totalSum = 0;

for (const key in salaries) {
    if (salaries.hasOwnProperty(key)) {
        totalSum += salaries[key];
    }
}

console.log(totalSum);