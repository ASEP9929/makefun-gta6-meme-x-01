// gta6-meme-x-01 entrypoint (Node 22, standard library only).
//
// The entry is the X post itself: the meme (meme.png) is posted on X from a
// public account, and POST.json at the repo root names that post. This
// program does one thing: it copies POST.json from the repository into the
// output directory, where the gate reads it. The house then reads the post
// from X and hands its first picture plus its text to the judge.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(outDir, { recursive: true });
const outPath = join(outDir, "POST.json");
copyFileSync(join(botDir, "POST.json"), outPath);

// Sanity check: the copied file must be a JSON object with a url string.
const post = JSON.parse(readFileSync(outPath, "utf8")) as { url?: unknown };
if (typeof post.url !== "string" || post.url.length === 0) {
  throw new Error("POST.json has no url string");
}
console.log("POST.json copied to", outPath, "->", post.url);
