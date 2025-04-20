// Regex that validates Philippine mobile numbers starting with 09 and 11 digits total

const regex = /^(09|\+639)\d{9}$/;

// Test cases
const testCases = [
  "09123456789", // valid
  "+639123456789", // valid
  "0912345678", // invalid
  "091234567890", // invalid
  "1234567890", // invalid
  "+63912345678", // invalid
  "0912345678a", // invalid
  "09123456789b" // invalid
];

// Function to test regex
function testRegex() {
  testCases.forEach((testCase) => {
    const isValid = regex.test(testCase);
    console.log(`Testing "${testCase}": ${isValid ? "Valid" : "Invalid"}`);
  });
}

// Run the test
testRegex();