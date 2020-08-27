//Whats the value of result?
let result = 2001
const test = () => {
    inner();
    console.log(result);
    return;
    function inner() {
        result = 2020
    }
};
test();
