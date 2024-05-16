<template>
  <div>
    <p style="white-space: pre">{{ ascii }}</p>
  </div>
</template>

<script setup lang="ts">
import figlet from 'figlet';
import doom from 'figlet/importable-fonts/Doom.js';
import rectangles from 'figlet/importable-fonts/Rectangles.js';
import small from 'figlet/importable-fonts/Small.js';
import standard from 'figlet/importable-fonts/Standard.js';

const props = defineProps<{
  text: string;
}>();

let ascii: string | undefined = '';

figlet.parseFont('Doom', doom);
figlet.parseFont('Rectangles', rectangles);
figlet.parseFont('Small', small);
figlet.parseFont('Standard', standard);

figlet.text(
  props.text,
  {
    font: 'Standard',
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
