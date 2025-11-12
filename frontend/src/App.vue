<template>
    <div class = "bg-light">
        <Navbar />
        <div>
            <TaskList :tasks="tasks" />
        </div>
        <pre>{{ tasks }}</pre>
    </div>
  </template>
  
<script>
    import Navbar from './components/Navbar.vue';
    import TaskList from './components/TaskList.vue';

    export default {
        components: {
            Navbar,
            TaskList
        },
        data() {
            return {
                title: "To-Do Application",
                tasks: [],
            }
        },
        async mounted() {
            const response = await fetch('http://localhost:8000/api/todo.json');
            const data = await response.json();
            this.tasks = data.toDos;
        }
    }
</script>
