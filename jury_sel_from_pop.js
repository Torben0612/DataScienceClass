const probabilitiesPopulation = [66, 721, 0, 72, 3, 137];
const juryPoolPopulation = [];

// Populate jury pool based on probabilities
for (let i = 0; i < probabilitiesPopulation[0]; i++) {
  juryPoolPopulation.push("Black");
}
for (let i = 0; i < probabilitiesPopulation[1]; i++) {
  juryPoolPopulation.push("White");
}
for (let i = 0; i < probabilitiesPopulation[2]; i++) {
  juryPoolPopulation.push("Pacific Islander");
}
for (let i = 0; i < probabilitiesPopulation[3]; i++) {
  juryPoolPopulation.push("Asian");
}
for (let i = 0; i < probabilitiesPopulation[4]; i++) {
  juryPoolPopulation.push("Native American");
}
for (let i = 0; i < probabilitiesPopulation[5]; i++) {
  juryPoolPopulation.push("Other");
}

console.log("Here is the jury pool based on the overall community demographics:");
console.log(juryPoolPopulation);
console.log("");

const whiteJurrorsPopulation = [];
const blackJurrorsPopulation = [];
const pacificIslanderJurrorsPopulation = [];
const asianJurrorsPopulation = [];
const nativeAmericanJurrorsPopulation = [];
const otherJurrorsPopulation = [];



// Simulate 200 juries
for (let j = 0; j < 20; j++) {
  const jury = [];
  let whiteCounter = 0;
  let blackCounter = 0;
  let pacificCounter = 0;
  let asianCounter = 0;
  let nativeCounter = 0;
  let otherCounter = 0;

  // Select 12 jurors randomly
  for (let k = 0; k < 12; k++) {
    const juror = juryPoolPopulation[Math.floor(Math.random() * juryPoolPopulation.length)];
    jury.push(juror);

    if (juror === "White") {
      whiteCounter++;
    } else if (juror === "Black") {
      blackCounter++;
    } else if (juror === "Pacific Islander") {
      pacificCounter++;
    } else if (juror === "Asian") {
      asianCounter++;
    } else if (juror === "Native American") {
      nativeCounter++;
    } else if (juror === "Other") {
      otherCounter++;
    }
  }

  console.log("Here is jury " + (j + 1) + " :");
  console.log(jury);

  whiteJurrorsPopulation.push(whiteCounter);
  blackJurrorsPopulation.push(blackCounter);
  pacificIslanderJurrorsPopulation.push(pacificCounter);
  asianJurrorsPopulation.push(asianCounter);
  nativeAmericanJurrorsPopulation.push(nativeCounter);
  otherJurrorsPopulation.push(otherCounter);
}

console.log("");
console.log("Here is the count of jurors based on demographic on each jury using the actual community demographics:");
console.log("White: " + whiteJurrorsPopulation);
console.log("Black: " + blackJurrorsPopulation);
console.log("Pacific Islander: " + pacificIslanderJurrorsPopulation);
console.log("Asian: " + asianJurrorsPopulation);
console.log("Native American: " + nativeAmericanJurrorsPopulation);
console.log("Other: " + otherJurrorsPopulation);