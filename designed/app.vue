<template>
  <div>
    <ClientOnly>
      <NuxtPage />
    </ClientOnly>
  </div>
</template>

<style>
body {
  margin: 0;
  padding: 0;
  font-family: monospace;
  background-color: rgb(var(--bg));
  color: rgb(var(--text));
  transition: background-color 0.5s, color 0.5s;
}

:root {
  --text: 255, 255, 255;
  --bg: 33, 37, 41;
}

.textColour {
  color: rgb(var(--text));
  transition: color 0.5s;
}

.bgColour {
  background-color: rgb(var(--bg));
  transition: background-color 0.5s;
}

.textColourInvert {
  color: rgb(var(--bg));
  transition: color 0.5s;
}

.bgColourInvert {
  background-color: rgb(var(--text));
  transition: background-color 0.5s;
}
</style>
