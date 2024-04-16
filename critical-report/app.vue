<script setup lang="ts">
const { data } = await useAsyncData('main-data', () =>
  queryContent('/main').findOne()
);
</script>

<template>
  <div>
    <template v-if="data">
      <Sidebar :data="data" />
      <Chat :title="'title'" :data="data" />
    </template>
  </div>
</template>

<style scoped>
div {
  display: flex;
  flex-direction: row;
  width: 100svw;
  height: 100svh;
}
</style>

<style>
html,
body {
  margin: 0;
  padding: 0;
  overflow: hidden;
  font-family: monospace;
}

:root {
  --white: #fff;
  --black: #000;
  --gray-50: #f9f9f9;
  --gray-100: #ececec;
  --gray-200: #cdcdcd;
  --gray-300: #b4b4b4;
  --gray-400: #9b9b9b;
  --gray-500: #676767;
  --gray-600: #424242;
  --gray-700: #2f2f2f;
  --gray-800: #212121;
  --gray-900: #171717;
  --gray-950: #0d0d0d;
  --red: #ff5c5c;
  --green: #89ff68;
  --blue: #68a9ff;
  --purple: #ab68ff;
}
</style>
