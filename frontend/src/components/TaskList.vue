<template>
    <div class = "accordian d-flex">
        <div class="container mt-4 accrodian left-panel">
            <ul class="list-unstyled h5 list-group w-50 mx-auto mt-4">
                <li
                    v-for="(task, index) in tasks"
                    :key="task.id"
                    class="justify-content-between align-items-center border-3 accordian-item"
                    id ="task-accordian"
                >   
                    <div class="d-flex gap-3 w-100 align-items-center accordian-item p-2">
                        <button class="btn btn-hover-red bg-danger btn-sm" @click="deleteTask(task)">
                            <p class="text-white mb-0">X</p>
                        </button>
                        <div class= "list-group-item d-flex justify-content-between align-items-center w-100 border-3 rounded-3 accordian-button" @click="toggleInfoPanel(task)">
                            <span :class="{ 'text-decoration-line-through text-muted': task.completed } " style="cursor: pointer;">
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
        </div>

        <div class="accordian-body right-panel w-45" v-if="selectedTaskId">
            <TaskPanel
                :task="tasks.find(t => t.id === selectedTaskId)"
                :steps="steps"
                @save-task="updateTask"
            />
        </div>

        <div class="modal-backdrop" v-if="deleteConfirm" @click="toggleInfoPanel({id: selectedTaskId})">
            
        </div>

    </div>
</template>

<script>
    import TaskPanel from './TaskPanel.vue';
    export default{
        props: ['tasks','steps'],
        emits: ["task-complete-undo","delete-task","update-task"],
        components: {
            TaskPanel
        },
        data() {
            return {
                selectedTaskId: null,
                deleteConfirm: false,
            };
        },
        methods: {
            taskCompleteUndoButton(task) {
                this.$emit("task-complete-undo", task);
            },
            deleteTask(task) {
                this.deleteConfirm = true
                this.$emit("delete-task", task);
            },
            toggleInfoPanel(task) {
                if (this.selectedTaskId === task.id) {
                    this.selectedTaskId = null;
                } else {
                    this.selectedTaskId = task.id;

                }
            },

            updateTask(updatedTask) {
                console.log("Updating task:", updatedTask);
                this.$emit("update-task", updatedTask);
            }
        }
    };
</script>