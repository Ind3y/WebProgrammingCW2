<template>
    <ul class="h5 list-group w-50 mx-auto mt-4">
        <li
            v-for="(task, index) in tasks"
            :key="index"
            class="list-group-item d-flex justify-content-between align-items-center border-3"
        >
            <span :class="{ 'text-decoration-line-through text-muted': task.completed }">
                {{ task.title }}
            </span>

            <div class="d-flex justify-content-between">
                <button class ="btn btn-sm btn-success" @click="taskCompleteUndoButton(task)">
                    {{ task.completed ? 'Undo' : 'Complete' }}
                </button>
            </div>
        </li>
    </ul>
</template>

<script>
    export default{
        props: ['tasks'],
        emits: ["task-complete-undo"],
        methods: {
            taskCompleteUndoButton(task) {
                this.$emit("task-complete-undo", task);
            }
        }

    };
</script>