const fs = require("fs");

const html = fs.readFileSync("ExamAdmin/MCQ Explorer.html", "utf8");
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map((match) => match[1]);

for (const script of scripts) {
  new Function(script);
}

console.log(`scripts ok: ${scripts.length}`);
