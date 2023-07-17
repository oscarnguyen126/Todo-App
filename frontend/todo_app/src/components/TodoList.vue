<script>
export default {
  props: ["todo"],
};
</script>

<template>
  <div class="todo-container">
    <div class="todo-note">
      <strong
        ><p class="todo-attrs">{{ todo.description }}</p></strong
      >
      <p class="todo-attrs">Complete Date: {{ todo.complete_date }}</p>
      <p class="todo-attrs">Done: {{ todo.is_done }}</p>
      <p class="todo-attrs">Expired: {{ todo.is_expired }}</p>
    </div>
  </div>
</template>

<style>
.todo-note {
  background-color: rgb(29, 161, 201);
  color: black;
  display: flex;
  text-align: start;
  flex-direction: column;
  margin: 10px auto;
}

.todo-attrs {
  margin: 0;
  padding: 0;
  font-size: 18px;
}
</style>
