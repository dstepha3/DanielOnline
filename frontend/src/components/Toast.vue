<template>
    <div class="toast-wrapper">
        <div v-if="success" class="success toastie">
            <i class="fas fa-thumbs-up" style="margin-right: 10px;"></i>{{ message }}
        </div>
        <div v-if="fail" class="fail toastie">
            <i class="fas fa-exclamation-circle" style="margin-right: 10px;"></i>{{ message }}
        </div>
        <div v-if="primary" class="primary toastie">
            <i class="fas fa-info-circle" style="margin-right: 10px;"></i>{{ message }}
        </div>
        <div v-if="warning" class="warning toastie">
            <i class="fas fa-exclamation-circle" style="margin-right: 10px;"></i>{{ message }}
        </div>
    </div>
</template>

<script lang="js">

export default {
    name: 'Toast',
    props: {
        message: String,
        mode: String,
        success: Boolean,
        fail: Boolean,
        primary: Boolean,
        warning: Boolean
    }
}
</script>


<style scoped>
    .toast-wrapper{
        width: 100%;
        z-index: 90;
        position: fixed;
        display: flex;
        justify-content: flex-end;
        margin-top: 20px;
        padding-right: 20px;
        width: 400px;
        right: 0;

    }
    .toastie{
        padding: 5px 50px 5px 25px;
        color: rgba(255, 255, 255, 0.7);
        border-radius: 5px;
        border-left: 2px solid rgba(255, 255, 255, 0.35);
        width: 300px;
        max-width: 400px;
        font-weight: 700;
        text-align: left;
        font-size: 14px;
    }
    .success.toastie{
        background: rgba(12, 255, 156, 0.7);
        color: black;
    }
    .fas{
        font-size: 14px;
    }
    .success.toastie .fas{
        color: black;
    }
    .fail.toastie{
        background: rgba(175, 0, 0, 0.7);
    }
    .primary.toastie{
        background: rgba(4, 155, 224, 0.7);
        color: black;
    }
    .primary.toastie .fas{
        color: black;
    }
    .warning.toastie{
        background: rgba(143, 134, 4, 0.7);
        color: black;
    }

</style>