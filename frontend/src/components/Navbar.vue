<template>
    <div class ="d-flex justify-content-center align-items-center p-3 bg-dark">
        <h1 class = "text-white">To-Do Application</h1> 
        <button class="btn btn-primary ms-4" @click="addTask()">Add Task</button>
    </div>
</template>

<script>
    export default{
        emits: ["Toggle-add-task"],
        methods: {
            addTask() {
                this.$emit("Toggle-add-task","open");
            }
        }
    };
</script>