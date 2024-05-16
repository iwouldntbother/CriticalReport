<template>
  <div>
    <Header text="Introduction" />
    <!-- <span>{{ file }}</span> -->
    <!-- <span>{{ data.join('<br />') }}</span> -->
    <div v-for="(line, index) in data" :key="index">
      <template v-if="line.substring(0, 2) === '##'">
        <!-- <h2>{{ line.replace('##', '') }}</h2> -->
        <Header :text="line.replace('##', '')" />
      </template>
      <template v-else-if="line.substring(0, 1) === '#'">
        <h1>{{ line.replace('#', '') }}</h1>
      </template>
      <template v-else>
        <span>{{ line }}</span>
      </template>
      <br />
    </div>
  </div>
</template>

<script setup lang="ts">
// const fullString = ref('');

import file from '/content/Final.001.md?raw';

const data = file.split('\n');

// fullString.value = data[0].body.children;
</script>
