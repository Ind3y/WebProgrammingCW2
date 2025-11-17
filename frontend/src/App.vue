<template>
    <div >
        <Navbar @Toggle-add-task="showAddTask"/>
        <div class="d-flex" >
            <div class="left-panel flex-fill">
                <AddTask 
                    v-if = "openAddTask" 
                    @add-task="postNewTask" 
                    @close-add-task="closeAddTask"
                />
                <TaskList 
                    :tasks="tasks"
                    :steps="steps"
                    @task-complete-undo="completeUndoTask" 
                    @delete-task="deleteTask" 
                    @update-task="updateTask"
                    @add-step="addSteps"
                    @delete-step="deleteStep"
                    @complete-undo-step="completeUndoStep"

                    
                />

            </div>

            <!-- <div class="right-panel w-25" v-if="toggleTaskPanel">
                <TaskPanel 
                    :task="selectedTask"
                    :steps="steps" 
                    @toggle-info-panel = "showTaskPanel"
                    @save-task="updateTask"
                    @add-step="addSteps"
                    @delete-step="deleteStep"
                    @complete-undo-step="completeUndoStep"/>
            </div> -->
        </div>
        <!-- <pre>{{ tasks }}</pre>
        <pre>{{ steps }}</pre> -->
    </div>
</template>
  
<script>
    import Navbar from './components/Navbar.vue';
    import TaskList from './components/TaskList.vue';
    import AddTask from './components/AddTask.vue';


    export default {
        components: {
            Navbar,
            TaskList,
            AddTask,
        },
        data() {
            return {
                title: "To-Do Application",
                tasks: [],
                steps: [],
                incompletedTask: [],
                completedTask: [],
                openAddTask: false,
                selectedTask: null,
                toggleTaskPanel: false,
            }
        },
        async mounted() {
            const response = await fetch('http://localhost:8000/api/tasks/',{
                method: 'GET',
            });
            const data = await response.json();
            console.log(data.tasks.length);
            for (let i = 0; i < data.tasks.length; i++){
                if (data.tasks[i].completed){
                    this.completedTask.push(data.tasks[i]);
                } else {
                    this.incompletedTask.push(data.tasks[i]);
                }
            }
            this.tasks = this.incompletedTask.concat(this.completedTask);
            this.completedTask = [];
            this.incompletedTask = [];
            this.steps = data.steps;
            
        },

        methods: {
            async completeUndoTask(task){
                const response = await fetch(`http://localhost:8000/api/tasks/${task.id}/`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        completed: !task.completed
                    })
                });
                const putResponse = await response.json();
                
                const index = this.tasks.findIndex(t => t.id === putResponse.id);
                if (index !== -1) {
                    this.tasks[index].completed = putResponse.completed;
                }
                

                for (let x = 0; x < this.tasks.length ;x++){
                    if (this.tasks[x].completed){
                        this.completedTask.push(this.tasks[x]);
                    } else {
                        this.incompletedTask.push(this.tasks[x]);
                    }
                }
                this.tasks = [];
                console.log(this.tasks);
                this.tasks = this.incompletedTask.concat(this.completedTask);
                this.incompletedTask=[];
                this.completedTask=[];
                console.log(this.tasks);
            },

            async updateTask(task){
                console.log("Updating task:", task);
                const response = await fetch(`http://localhost:8000/api/tasks/update/${task.id}/`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        title: task.title,
                        due_date: task.due_date,
                        completed: task.completed,
                        note: task.notes
                    })
                });
                const putResponse = await response.json();
                
                const index = this.tasks.findIndex(t => t.id === putResponse.id);
                if (index !== -1) {
                    this.tasks[index] = putResponse;
                }
            },

            showAddTask(toggleStatus){
                console.log("Add Task button clicked");
                if (toggleStatus === "open"){
                    this.openAddTask = true;
                }

                console.log(this.openAddTask);
            },

            closeAddTask(){
                this.openAddTask = false;
            },

            async postNewTask(newTask){
                console.log("Posting new task:", newTask);
                const response =  await fetch('http://localhost:8000/api/tasks/create/', {
                    method: 'POST',
                    body: JSON.stringify(newTask)
                });
                const createdTask = await response.json();
                this.tasks.push(createdTask);
                this.openAddTask = false;
            },

            async deleteTask(task){
                if (confirm(`Are you sure you want to delete this task: ${task.title}?`)){
                    await fetch(`http://localhost:8000/api/tasks/${task.id}/`, {
                        method: 'DELETE',
                    });
                    this.tasks = this.tasks.filter(t => t.id !== task.id);
                }
            },

            async addSteps(step){
                console.log("Emitted add-step received in App.vue");
                console.log("Adding step:", step);
                const response =  await fetch(`http://localhost:8000/api/tasks/${step.taskId}/steps/`, {
                    method: 'POST',
                    body: JSON.stringify({
                        taskId: step.taskId,
                        description: step.description,
                        completed: step.completed
                    })
                });
                const createdStep = await response.json();
                this.steps.push(createdStep);
            },

            async deleteStep(step){
                console.log("Deleting step:", step);
                await fetch(`http://localhost:8000/api/steps/${step.id}/`, {
                    method: 'DELETE',
                });
                this.steps = this.steps.filter(s => s.id !== step.id);
        
            },


            async completeUndoStep(step){
                console.log("Toggling step completion:", step);
                const response = await fetch(`http://localhost:8000/api/steps/${step.id}/`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        completed: !step.completed
                    })
                });

                const putResponse = await response.json();
                const index = this.steps.findIndex(s => s.id === putResponse.id);
                if (index !== -1) {
                    this.steps[index].completed = putResponse.completed;
                }
            }
        }   
    }   
</script>
