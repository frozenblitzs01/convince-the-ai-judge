// convince-the-ai-judge entry (Node 22, standard library only).
//
// The image is drawn ahead of time by draw.py (PIL, DejaVu) and shipped
// beside this file as entry.png; the program just places it where the
// grader reads it. Deterministic: same bytes in, same bytes out.
//
// Local run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { chmodSync, copyFileSync, existsSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
if (!existsSync(outDir)) {
  mkdirSync(outDir, { recursive: true });
}
const src = join(here, "entry.png");
// The gate allows at most 1 MiB: refuse to ship an oversized image
// rather than letting the grader reject it.
if (statSync(src).size > 1048576) {
  throw new Error(`entry.png is ${statSync(src).size} bytes, over the 1 MiB gate`);
}
const dest = join(outDir, "entry.png");
copyFileSync(src, dest);
chmodSync(dest, 0o644);
