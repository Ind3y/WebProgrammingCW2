<template>
    <div class="container mt-4 accordion">
        <div class="accordion-item" v-for="task in tasks">
            <h2 class="accordion-header">
                <button 
                    class="accordion-button collapsed d-flex justify-content-between align-items-center w-100" 
                    type="button" 
                    data-bs-toggle="collapse" 
                    :data-bs-target="'#task-' + task.id" 
                >
                    <div class="justify-content-between">
                        <span :class="{ 'text-decoration-line-through text-muted': task.completed } " style="cursor: pointer;">
                            <strong>
                                {{ task.title }}
                            </strong>
                        </span>
                        <span class="mx-3" v-if="task.due_date">
                            <strong>
                                Due: {{ task.due_date }}
                            </strong>
                        </span>
                    </div>  
                </button>
            </h2>
            <div 
                :id="'task-' + task.id" 
                class="accordion-collapse collapse" 
                :aria-labelledby="'heading-' + task.id" 

            >
                <div class="accordion-body">
                    <input 
                        type="text" 
                        class="form-control mb-3" 
                        v-model="task.title" 
                        placeholder="Task Title">
                    <p><strong>Status:</strong> {{ task.completed ? 'Completed' : 'Incomplete' }}</p>
                    <p><strong>Due Date:</strong></p>
                        <input 
                        type="date" 
                        class="form-control mb-3" 
                        v-model="task.due_date" 
                        placeholder="Due Date"/>
                    <div class="mb-3">
                        <label for="notes" class="form-label"><strong>Notes:</strong></label>
                        <textarea 
                            id="notes" 
                            class="form-control" 
                            v-model="task.notes" 
                            rows="4" 
                            placeholder="Enter notes here..."
                        ></textarea>
                    </div>
                    <div class ="d-flex align-items-center mt-3 gap-2">
                        <button class ="btn btn-sm btn-success" data-bs-toggle="collapse" :data-bs-target="'#task-' + task.id"  @click="taskCompleteUndoButton(task)">
                            {{ task.completed ? 'Undo' : 'Complete' }}
                        </button>
                        <button class="btn bg-primary btn-sm" data-bs-toggle="collapse" :data-bs-target="'#task-' + task.id" @click="updateTask(task)">
                            <p class="text-white mb-0"> Save changes </p>
                        </button>
                        <button class="btn bg-danger btn-sm"  data-bs-toggle="modal" data-bs-target="#task-deletion" @click="deletingTask = task">
                            <p class="text-white mb-0">Delete Task</p>
                        </button>
                    </div>

                    <div class="d-flex flex-column mb-3">

                        <label for="steps" class="form-label"><strong>Steps:</strong></label>
                        <input type="text" class="form-control mb-2" v-model="newStepDescription" placeholder="Enter step description"/>
                        <button class="btn btn-secondary" @click="addStep(task.id)">+ Add Step</button>

                        <ul class="list-group">
                            <li 
                                v-for="step in steps.filter(s => s.task_id === task.id)" 
                                :key="step.id" 
                                class="list-group-item d-flex justify-content-between align-items-center"
                            >
                                <span :class="{ 'text-decoration-line-through text-muted': step.completed }">
                                    {{ step.description }}
                                </span>
                                <div class="d-flex alighn-items-center gap-2">
                                    <button class="btn btn-danger btn-sm" @click="deleteStep(step)">X</button>
                                    <button class="btn btn-sm btn-success" @click="stepCompleteUndo(step)">
                                        {{ step.completed ? 'Undo' : 'Complete' }}
                                    </button>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <div class="modal" id="task-deletion">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 class="modal-title">Delete Task</h4>
                    </div>
                    <div class="modal-body" v-if="deletingTask">
                        <p>Are you sure you want to delete the task</p>
                        <p><strong>{{ deletingTask.title }}</strong>?</p>
                    
                    </div>
                    <div class="modal-footer">
                        <button class="btn btn-danger" @click="deleteTask(deletingTask)" data-bs-dismiss="modal">
                            Delete
                        </button>
                        <button class="btn btn-primary" data-bs-dismiss="modal">
                            Cancel
                        </button>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
    export default{
        props: ['tasks','steps'],
        emits: ["task-complete-undo","delete-task","update-task","add-step","delete-step","complete-undo-step"],
        data() {
            return {
                selectedTaskId: null,
                deleteConfirm: false,
                newStepDescription: '',
                deletingTask: null,
            };
        },
        methods: {
            taskCompleteUndoButton(task) {
                this.$emit("task-complete-undo", task);
            },
            deleteTask(task) {
                this.deleteConfirm = true;

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
            },
            addStep(task_id) {
                if (this.newStepDescription.trim() === "") {
                    alert("Please enter step description");
                    return;
                }
                console.log("Adding step to task ID" , task_id);
                console.log("adding description:", this.newStepDescription);
                this.$emit("add-step", {
                    taskId: task_id,
                    description: this.newStepDescription,
                    completed: false
                });
                console.log("emitted add-step");
                this.newStepDescription = "";
            },
            deleteStep(step){
                this.$emit("delete-step", step);
            },

            stepCompleteUndo(step) {
                this.$emit("complete-undo-step", step);
            },
        }
    };
</script>