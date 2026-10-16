// scripts/remove-bg.cjs
// Quita el fondo blanco del logo de Lía usando sharp.
// Genera un PNG transparente (sharp tiene un quirk con WebP lossless + RGBA).

const sharp = require("../node_modules/.pnpm/sharp@0.34.5/node_modules/sharp");
const path = require("path");

const SRC = path.join(__dirname, "..", "public", "logo_lia.webp");
const DST = path.join(__dirname, "..", "public", "logo_lia.png"); // PNG con alfa

(async () => {
  const { data, info } = await sharp(SRC)
    .ensureAlpha()
    .raw()
    .toBuffer({ resolveWithObject: true });

  const { width, height, channels } = info;
  console.log(`Input: ${width}x${height} channels=${channels}`);

  const THRESHOLD = 240;
  let transparentCount = 0;
  for (let i = 0; i < data.length; i += channels) {
    const r = data[i];
    const g = data[i + 1];
    const b = data[i + 2];
    if (r >= THRESHOLD && g >= THRESHOLD && b >= THRESHOLD) {
      data[i + 3] = 0;
      transparentCount++;
    }
  }
  console.log(
    `Transparent pixels: ${transparentCount} (${((transparentCount / (data.length / channels)) * 100).toFixed(1)}%)`,
  );

  await sharp(data, { raw: { width, height, channels: 4 } })
    .png({ compressionLevel: 9 })
    .toFile(DST);

  console.log(`PNG transparent saved: ${DST}`);

  const meta = await sharp(DST).metadata();
  console.log(
    `Output: ${meta.width}x${meta.height} format=${meta.format} hasAlpha=${meta.hasAlpha} channels=${meta.channels}`,
  );
})();