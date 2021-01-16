function primeNumber(input) {
    let answer = 0;
    if (input < 2) {
        console.log(0);
        return 0;
    } else {
        let isOdd = input % 2;
        if (!isOdd && input != 2) {
            console.log(-1);
            return -1;
        }
    }
    for(i = 0; i < input; i++) {
        answer += (i + 1);
    }
    console.log(answer);
    return answer;
}
primeNumber(11);
