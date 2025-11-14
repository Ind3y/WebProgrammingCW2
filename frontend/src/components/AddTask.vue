<template>
    <div class="container mt-4">
        <section class="list-group-item flex justify-content-between align-items-center border-3 ">
            <h2 class="text-center">Add New Task</h2>
            <input
                type="text"
                class="form-control mb-2"
                placeholder="Enter task"
                v-model="newTaskTitle"/>
            <input type="date" class="form-control mb-2" v-model="due_date"/>
            <div class = "d-flex gap-2">
                <button type = "submit" class="btn btn-primary w-100" @click="addTask">Add Task</button>
                <button class="btn btn-light w-100 border-2 border-dark" @click="closeForm">Close</button>
            </div>
        </section>
    </div>
</template>

<script>
    export default {
        emits: ["close-add-task","add-task"],
        data() {
            return {
                newTaskTitle: "",
                due_date: ""
            };
        },
        methods: {
            addTask() {
                if (this.newTaskTitle.trim() === "" || this.newTaskTitle === null) {
                    alert("Please enter Task details")
                } else if (this.due_date === "" || this.due_date === null  ) {
            
                    this.$emit("add-task", {
                        title: this.newTaskTitle,
                    });
                    this.newTaskTitle = "";
                } else {
                    this.$emit("add-task", {
                        title: this.newTaskTitle,
                        due_date: this.due_date,
                    });
                    this.newTaskTitle = "";
                }
            },

            closeForm() {
                this.$emit("close-add-task");
            }   
        }
    };
</script>
