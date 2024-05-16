<template>
  <div>
    <p style="white-space: pre">{{ ascii }}</p>
  </div>
</template>

<script setup lang="ts">
import figlet from 'figlet';
// @ts-ignore
import doom from 'figlet/importable-fonts/Doom.js';
// @ts-ignore
import rectangles from 'figlet/importable-fonts/Rectangles.js';
// @ts-ignore
import small from 'figlet/importable-fonts/Small.js';
// @ts-ignore
import standard from 'figlet/importable-fonts/Standard.js';
// @ts-ignore
import ansiShadow from 'figlet/importable-fonts/ANSI Shadow.js';

const props = defineProps<{
  text: string;
  font: string;
}>();

let ascii: string | undefined = '';

figlet.parseFont('Doom', doom);
figlet.parseFont('Rectangles', rectangles);
figlet.parseFont('Small', small);
figlet.parseFont('Standard', standard);
figlet.parseFont('ANSI Shadow', ansiShadow);

// @ts-expect-error
figlet.text(
  props.text || 'Standard',
  {
    font: props.font,
  },
  function (err, data) {
    if (err) {
      console.log('Something went wrong...');
      console.dir(err);
      return;
    }
    ascii = data;
  }
);
</script>
