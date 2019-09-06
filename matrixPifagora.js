/*jshint esversion: 6 */
let fullName = 'Владимир Владимирович Путин';
let indata = '13.06.1966';
//let indata = '13.02.2000'; // после 2000 включительно
//let indata = '07.10.1952';  // +
let dmyArr = indata.split(/[.,;-]/);

let GodNumbers = [10,11,12];


let strSum = (num) => {
    return String(num).split('').reduce((sum, item) => {
        sum = Number(sum);
        return sum += Number(item);
    });
};
let trueGod = (num) => (num >=10 && num <= 12 ) ? true : false;

//console.log('id:' + indata);

let firstWorkNumber = strSum(indata.replace(/[.,;-]/g,''));
console.log('WN1: ' + firstWorkNumber);

let secondWorkNumber = 0;
if (trueGod(firstWorkNumber)) {
    secondWorkNumber = firstWorkNumber;
} else {
    secondWorkNumber = strSum(String(firstWorkNumber));
}
console.log('WN2: ' + secondWorkNumber);

let threeWorkNumber = 0;
if (dmyArr[2] >= Number(2000)) {
    //после 2000 включительно
    threeWorkNumber = Number(firstWorkNumber) + 19;
} else {
    threeWorkNumber = firstWorkNumber - Number(dmyArr[0])*2;
}
console.log('WN3: ' + threeWorkNumber);

let fourWorkNumber = 0;
if (trueGod(threeWorkNumber)) {
    fourWorkNumber = threeWorkNumber;
} else {
    fourWorkNumber = strSum(String(threeWorkNumber));
}
console.log('WN4: ' + fourWorkNumber);

console.log(fullName);
console.log(indata);
let all = '';
if (dmyArr[2] >= Number(2000)) {
    //после 2000 включительно
    console.log(`${firstWorkNumber} ${secondWorkNumber} 19 ${threeWorkNumber} ${fourWorkNumber}`);
    all = dmyArr.join('') + String(firstWorkNumber) + String(secondWorkNumber) + '19' + String(threeWorkNumber) + String(fourWorkNumber);
} else {
    console.log(`${firstWorkNumber} ${secondWorkNumber} ${threeWorkNumber} ${fourWorkNumber}`);
    all = dmyArr.join('') + String(firstWorkNumber) + String(secondWorkNumber) + String(threeWorkNumber) + String(fourWorkNumber);
}



console.log(all);
console.log(all.match(/1/g) + '|' + all.match(/4/g) + '|' + all.match(/7/g));
console.log(all.match(/2/g) + '|' + all.match(/5/g) + '|' + all.match(/8/g));
console.log(all.match(/3/g) + '|' + all.match(/6/g) + '|' + all.match(/9/g));
