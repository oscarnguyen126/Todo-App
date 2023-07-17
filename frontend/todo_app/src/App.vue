<script>
import TodoList from "./components/TodoList.vue";

export default {
  components: {
    TodoList,
  },
  data() {
    return {
      todos: [],
    };
  },
  methods: {
    async list_todo() {
      const res = await fetch("http://127.0.0.1:8000/todos/");
      const todos = await res.json();
      this.todos = todos;
    },
  },
  mounted() {
    this.list_todo();
  },
};
</script>

<template>
  <h1 id="title">Todo App</h1>

  <div v-for="todo in todos">
    <TodoList :todo="todo" />
  </div>
</template>

<style>
#title {
  color: white;
}
</style>
