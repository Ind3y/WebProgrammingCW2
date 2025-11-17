<template>
    <section class= "border border-dark p-3 mt-4 bg-white rounded">
        <input 
            type="text" 
            class="form-control mb-3" 
            v-model="task.title" 
            placeholder="Task Title"
        />


        <div class="d-flex">
            <p><strong>Due Date:</strong></p>
            <input 
            type="date" 
            class="form-control mb-3" 
            v-model="task.due_date" 
            placeholder="Due Date"/>
        </div>
        
        <p><strong>Status:</strong> {{ task.completed ? 'Completed' : 'Incomplete' }}</p>

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

        <div class="d-flex flex-column mb-3">

            <label for="steps" class="form-label"><strong>Steps:</strong></label>
            <input type="text" class="form-control mb-2" v-model="newStepDescription" placeholder="Enter step description"/>
            <button class="btn btn-secondary" @click="addStep">+ Add Step</button>

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

        <button class="btn btn-success" @click="saveTask()">Save</button>
    </section>
</template>

<script>
    export default {
        props: ['task','steps'],
        emits: ["save-task","add-step","delete-step","complete-undo-step"],
        data() {
            return {
                newStepDescription: ""
            };
        },
        methods: {
            saveTask() {
                this.$emit("save-task", this.task);
            },
            addStep() {
                if (this.newStepDescription.trim() === "") {
                    alert("Please enter step description");
                    return;
                }
                this.$emit("add-step", {
                    taskId: this.task.id,
                    description: this.newStepDescription,
                    completed: false
                });
                this.newStepDescription = "";
            },
            deleteStep(step){
                this.$emit("delete-step", step);
            },

            stepCompleteUndo(step) {
                this.$emit("complete-undo-step", step);
            },
        }
    }
</script>