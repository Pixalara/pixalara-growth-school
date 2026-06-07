const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '..', 'blog-quize.html');
const content = fs.readFileSync(filePath, 'utf8');

// Find the questionData array
const startIdx = content.indexOf('const questionData = [');
if (startIdx === -1) {
    console.error('Could not find questionData in blog-quize.html');
    process.exit(1);
}

// Find the end of the array (bracket match)
let bracketCount = 1;
let currentIdx = startIdx + 'const questionData = ['.length;
let arrayStr = '[';

while (bracketCount > 0 && currentIdx < content.length) {
    const char = content[currentIdx];
    if (char === '[') bracketCount++;
    if (char === ']') bracketCount--;
    arrayStr += char;
    currentIdx++;
}

// Eval the array safely
try {
    const questionData = eval(arrayStr);
    const outputPath = path.join(__dirname, 'questions.json');
    fs.writeFileSync(outputPath, JSON.stringify({ success: true, count: questionData.length, data: questionData }, null, 2), 'utf8');
    console.log('Successfully wrote questions to questions.json');
} catch (err) {
    console.error('Failed to parse questionData:', err);
}
