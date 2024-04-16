<template>
  <div class="sidebar-container">
    <div class="top-section">
      <Icon name="material-symbols:robot-2" />
      <span>WillGPT</span>
    </div>
    <div class="section-header-list">
      <template v-for="section in data.body.children">
        <p
          v-if="section.tag === 'h2'"
          class="section-header-link"
          @click="
            goto(
              String(section.children[0].value)
                .toLowerCase()
                .replaceAll(' ', '-')
            )
          "
        >
          {{ section.children[0].value }}
        </p>
      </template>
    </div>
  </div>
</template>

<style scoped>
.sidebar-container {
  display: flex;
  flex-direction: column;
  max-width: 240px;
  /* width: 100%; */
  height: 100%;
  padding: 10px;
  background-color: var(--gray-900);
  color: var(--white);
}

.top-section {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  padding: 10px;
  border-bottom: 1px solid var(--gray-800);
}
.section-header-list {
  display: flex;
  flex-direction: column;
  padding: 10px;
}

.section-header-link {
  padding: 5px;
  border-radius: 10px;
  cursor: pointer;
}

.section-header-link:hover {
  background-color: var(--gray-800);
}
</style>

<script setup lang="ts">
const props = defineProps({
  data: {
    type: Object,
    required: true,
  },
});

const { data } = props;

const goto = (id: string) => {
  const element = document.getElementById(id);
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' });
  }
};
</script>
