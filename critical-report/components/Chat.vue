<template>
  <div class="chat-container">
    <div class="chat-section-container">
      <div class="message-container">
        <template v-if="data">
          <template v-for="message in data.body.children">
            <!-- <div v-if="message.tag === 'h1'" class="ai-message-holder">
              <p class="ai-message">{{ message.children[0].value }}</p>
            </div> -->

            <div
              v-if="message.tag === 'h2'"
              class="ai-message-holder"
              :id="
                String(message.children[0].value)
                  .toLowerCase()
                  .replaceAll(' ', '-')
              "
            >
              <p class="ai-message">{{ message.children[0].value }}</p>
            </div>

            <div v-else-if="message.tag === 'p'" class="user-message-holder">
              <!-- <p class="user-message">{{ message.children[0].value }}</p> -->
              <!-- <p v-for='text in message.children' class="user-message">{{ message.children[0].value }}</p> -->
              <p class="user-message">
                <template v-for="text in message.children">
                  <span v-if="text.tag == 'span'">
                    {{ text.children[0].value }}
                  </span>
                  <a
                    v-else-if="text.tag == 'a'"
                    :href="text.props.href"
                    target="_blank"
                  >
                    {{ text.children[0].value }}
                  </a>
                  <template v-else>{{ text.value }}</template>
                </template>
              </p>
            </div>
          </template>
        </template>
        <p>{{ data.body.children }}</p>
      </div>
    </div>
    <div class="message-box-container">
      <input type="text" placeholder="Message WillGPT..." disabled />
      <div class="send-button">
        <Icon name="material-symbols:arrow-upward-alt-rounded" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
  background-color: var(--gray-800);
  overflow: hidden;
}

/* Chat text */

.chat-section-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* width: calc(100%-240px); */
  /* max-height: 100svh; */
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  background-color: var(--gray-800);
  color: var(--white);
  overflow-y: scroll;
  padding: 50px 0 10px 0;
}

.message-container {
  display: flex;
  flex-direction: column;
  min-width: 600px;
  width: 80%;
  /* background-color: cyan; */
}

.ai-message,
.user-message {
  max-width: 90%;
  background-color: var(--gray-600);
  padding: 5px 10px;
  border-radius: 10px;
  font-size: 1.2rem;
}

.user-message-holder,
.ai-message-holder {
  position: relative;
  /* background-color: blueviolet; */
  padding: 0.5rem 0 0 0;
  width: 100%;
}

.ai-message {
  float: left;
}

.ai-message::before {
  display: flex;
  color: white;
  font-size: 0.7rem;
  height: 1rem;
  white-space: pre;
  content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1rem' height='1rem' viewBox='0 0 24 24'%3E%3Cpath fill='white' d='M4 21v-5q0-.825.588-1.412T6 14h12q.825 0 1.413.588T20 16v5zm5-8q-2.075 0-3.537-1.463T4 8t1.463-3.537T9 3h6q2.075 0 3.538 1.463T20 8t-1.463 3.538T15 13zm0-4q.425 0 .713-.288T10 8t-.288-.712T9 7t-.712.288T8 8t.288.713T9 9m6 0q.425 0 .713-.288T16 8t-.288-.712T15 7t-.712.288T14 8t.288.713T15 9'/%3E%3C/svg%3E")
    ' ai-message';
  position: absolute;
  top: 0;
  left: 0;
}

.user-message {
  float: right;
}

.user-message::before {
  display: flex;
  color: white;
  font-size: 0.7rem;
  height: 1rem;
  white-space: pre;
  content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1rem' height='1rem' viewBox='0 0 24 24'%3E%3Cpath fill='white' d='M12 12q-1.65 0-2.825-1.175T8 8t1.175-2.825T12 4t2.825 1.175T16 8t-1.175 2.825T12 12m-8 8v-2.8q0-.85.438-1.562T5.6 14.55q1.55-.775 3.15-1.162T12 13t3.25.388t3.15 1.162q.725.375 1.163 1.088T20 17.2V20z'/%3E%3C/svg%3E")
    ' user-message';
  position: absolute;
  top: 0;
  right: 0;
}

a,
a:active,
a:visited {
  color: var(--blue);
  text-decoration: none;
}

/* Message bar */

.message-box-container {
  display: flex;
  margin: 0 0 15px 0;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  box-sizing: border-box;
  width: calc(80% + 20px);
  height: 50px;
  background-color: var(--gray-800);
  color: var(--white);
  padding: 10px 5px 10px 5px;
  border: solid 0.2rem var(--gray-700);
  border-radius: 10px;
}

.message-box-container input {
  width: 90%;
  font-size: 1rem;
  background: none;
  color: var(--white);
  border: none;
  padding: 0 10px;
}

.send-button {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 30px;
  height: 30px;
  margin-right: 4px;
  font-size: 1.75rem;
  color: var(--gray-900);
  border-radius: 10px;
  cursor: pointer;
  background: var(--gray-700);
}
</style>

<script setup lang="ts">
const props = defineProps({
  title: {
    type: String,
    required: true,
  },
  data: {
    type: Object,
    required: true,
  },
});

const { title, data } = props;
</script>
