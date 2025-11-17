<template>
    <div class ="d-flex justify-content-center align-items-center p-3 bg-dark">
        <h1 class = "text-white">To-Do Application</h1> 
        <button class="btn btn-primary ms-4" data-bs-toggle="modal" data-bs-target="#task-creation">Add Task</button>
    </div>
    <div class="modal" id="task-creation">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title">Create New Task</h4>
                    <button class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <p>Enter Task Details:</p>
                    <input
                        type="text"
                        class="form-control mb-2"
                        placeholder="Enter task"
                        v-model="newTaskTitle"/>
                    
                    <p>Due Date (optional):</p>
                    <input type="date" class="form-control mb-2" v-model="due_date"/>
                </div>
                <div class="modal-footer">
                    <button type = "submit" class="btn btn-primary w-100" data-bs-dismiss="modal" @click="addTask">Add Task</button>

                </div>  
            </div>
        </div>
    </div>
</template>

<script>
    export default{
        emits: ["add-task"],
        data() {
            return {
                newTaskTitle: "",
                due_date: ""
            };
        },
        methods: {
            addTask() {
                console.log(this.newTaskTitle);
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
        }
    };
</script>