import { mkdir, readFile, unlink, writeFile } from 'node:fs/promises';

// Django serves the HTML; Vite's hashed assets are collected from static-vuedj.
const html = await readFile(new URL('../static-vuedj/index.html', import.meta.url), 'utf8');
await mkdir(new URL('../templates/', import.meta.url), { recursive: true });
await writeFile(new URL('../templates/index.html', import.meta.url), html);
await unlink(new URL('../static-vuedj/index.html', import.meta.url));
