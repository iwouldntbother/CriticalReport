<template>
  <div>
    <ThemeChanger id="theme-changer" />
    <template v-for="(line, index) in data" :key="index">
      <template v-if="line.substring(0, 3) === '###'">
        <br />
        <Header :text="line.replace('###', '')" font="Rectangles" />
      </template>
      <template v-else-if="line.substring(0, 2) === '##'">
        <br />
        <Header :text="line.replace('##', '')" font="Small" />
      </template>
      <template v-else-if="line.substring(0, 1) === '#'">
        <br />
        <br />
        <br />
        <Header :text="line.replace('#', '')" font="ANSI Shadow" />
      </template>
      <template v-else-if="line.substring(0, 2) === 'QQ'">
        <h2 class="quote">{{ line.replace('QQ', '') }}</h2>
        <br />
      </template>
      <template v-else>
        <p class="paragraph" v-html="formatUrlsAsAnchors(line)"></p>
        <br />
      </template>
    </template>
    <!-- <span>{{ file }}</span> -->
  </div>
</template>

<script setup lang="ts">
// const fullString = ref('');

import file from '/content/Final.001.md?raw';

const data = file.split('\n');

// fullString.value = data[0].body.children;
function formatUrlsAsAnchors(input: string): string {
  const urlPattern = /https?:\/\/[^\s/$.?#].[^\s]*/g;

  // Replace URLs with anchor tags
  const formattedString = input.replace(urlPattern, (url) => {
    // Remove trailing full stop if present
    const cleanedUrl = url.endsWith('.') ? url.slice(0, -1) : url;
    return `<a class='link' href="${cleanedUrl}" target="_blank" rel="noopener noreferrer">${cleanedUrl}</a>.`;
  });

  return formattedString;
}
</script>

<style scoped>
p.paragraph {
  padding: 0 3rem 0 3rem;
  margin: 0;
}

h2.quote {
  padding: 0 3rem 0 3rem;
  margin: 0;
  font-style: italic;
  font-size: 1.5rem;
}

#theme-changer {
  position: absolute;
  top: 0;
  right: 0;
  margin-top: 1rem;
}
</style>
