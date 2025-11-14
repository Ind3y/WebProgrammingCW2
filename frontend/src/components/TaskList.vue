<template>
    <ul class="list-unstyled h5 list-group w-50 mx-auto mt-4">
        <li
            v-for="(task, index) in tasks"
            :key="task.id"
            class="justify-content-between align-items-center border-3"
        >   
            <div class="d-flex gap-3 w-100 align-items-center">
                <button class="btn btn-hover-red bg-danger btn-sm" @click="deleteTask(task)">
                    <p class="text-white mb-0">X</p>
                </button>
                <div class= "list-group-item d-flex justify-content-between align-items-center w-100 border-3 rounded-3">
                    <span :class="{ 'text-decoration-line-through text-muted': task.completed } " @click="toggleInfoPanel(task)" style="cursor: pointer;">
                        {{ task.title }}
                    </span>
                    
                    <div class="d-flex align-items-center">
                        <span class="mx-3" v-if="task.due_date">
                            Due: {{ task.due_date }}
                        </span>

                        <button class ="btn btn-sm btn-success" @click="taskCompleteUndoButton(task)">
                            {{ task.completed ? 'Undo' : 'Complete' }}
                        </button>
                    </div>
                </div>
            </div>
        </li>
    </ul>
</template>

<script>    
    export default{
        props: ['tasks'],
        emits: ["task-complete-undo","delete-task","toggle-info-panel"],
        methods: {
            taskCompleteUndoButton(task) {
                this.$emit("task-complete-undo", task);
            },
            deleteTask(task) {
                this.$emit("delete-task", task);
            },
            toggleInfoPanel(task) {
                if (this.selectedTaskId === task.id) {
                    this.selectedTaskId = null;
                } else {
                    this.selectedTaskId = task.id;
                }
                this.$emit("toggle-info-panel", "open", task);
            }
        }
    };
</script>