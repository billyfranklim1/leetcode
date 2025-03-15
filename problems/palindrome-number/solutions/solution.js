/**
 * @param {number} x
 * @return {boolean}
 */
function solution(x) {
    // Special cases
    if (x < 0) return false;
    if (x === 0) return true;
    if (x % 10 === 0 && x !== 0) return false;
    
    let reversed = 0;
    let original = x;
    
    while (x > 0) {
        const digit = x % 10;
        reversed = reversed * 10 + digit;
        x = Math.floor(x / 10);
    }
    
    return reversed === original;
}

// For Node.js compatibility
module.exports = solution;

// For testing locally
if (require.main === module) {
    const testCases = [121, -121, 10, 12321, 0];
    testCases.forEach(tc => {
        console.log(`${tc}: ${solution(tc)}`);
    });
}