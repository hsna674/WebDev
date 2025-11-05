let count = 0;
let ballsPerClick = 1;
let autoBalls = 0;

let coachCount = 0;
let ballCount = 0;
let fanCount = 0;

const countDisplay = document.querySelector('#soccerBallCount');
const coachDisplay = document.querySelector('#coachCount');
const ballDisplay = document.querySelector('#ballCount');
const fanDisplay = document.querySelector('#fanCount');

const soccerBall = document.querySelector('#soccerBall');
const buyCoachBtn = document.querySelector('#buyCoach');
const buyNewBallBtn = document.querySelector('#buyNewBall');
const buyFansBtn = document.querySelector('#buyFans');

let coachCost = 10;
let newBallCost = 25;
let fanCost = 50;

soccerBall.addEventListener('click', () => {
    count += ballsPerClick;
    updateDisplay();
});

buyCoachBtn.addEventListener('click', () => {
    if (count >= coachCost) {
        count -= coachCost;
        ballsPerClick++;
        coachCount++;
        coachCost = Math.floor(coachCost * 1.5);
        buyCoachBtn.innerText = `Hire Coach (cost: ${coachCost})`;
        updateDisplay();
    }
});

buyNewBallBtn.addEventListener('click', () => {
    if (count >= newBallCost) {
        count -= newBallCost;
        ballsPerClick += 2;
        ballCount++;
        newBallCost = Math.floor(newBallCost * 2);
        buyNewBallBtn.innerText = `Buy New Ball (cost: ${newBallCost})`;
        updateDisplay();
    }
});

buyFansBtn.addEventListener('click', () => {
    if (count >= fanCost) {
        count -= fanCost;
        autoBalls++;
        fanCount++;
        fanCost = Math.floor(fanCost * 2);
        buyFansBtn.innerText = `Fan Club (+${autoBalls}/sec) (cost: ${fanCost})`;
        updateDisplay();
    }
});

setInterval(() => {
    count += autoBalls;
    updateDisplay();
}, 1000);

function updateDisplay() {
    countDisplay.innerText = count;
    coachDisplay.innerText = coachCount;
    ballDisplay.innerText = ballCount;
    fanDisplay.innerText = fanCount;
}