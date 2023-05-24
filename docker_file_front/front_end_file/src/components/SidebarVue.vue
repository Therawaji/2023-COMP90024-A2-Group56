<template>
    <aside :class="`${expanded && 'expanded'}`">
        <div class="icon">
            <button class="toggle" @click="ToggleMenu">
                <span class="material-icons">keyboard_double_arrow_right</span>
            </button>
        </div>

        <h3>Menu</h3>
        <div class="menu">
            <router-link class="button" to="/">
                <span class="material-icons">home</span>
                <span class="text">Home</span>
            </router-link>
            <router-link class="button" to="/view1">
                <span class="material-icons">label</span>
                <span class="text">S1_overall</span>
            </router-link>
            <router-link class="button" to="/view2">
                <span class="material-icons">label</span>
                <span class="text">S2_gcc</span>
            </router-link>
            <router-link class="button" to="/view5">
                <span class="material-icons">label</span>
                <span class="text">S3_sentiment</span>
            </router-link>
            <router-link class="button" to="/view7">
                <span class="material-icons">label</span>
                <span class="text">S4_infrastructure</span>
            </router-link>
            <router-link class="button" to="/view8">
                <span class="material-icons">label</span>
                <span class="text">S5_income/life</span>
            </router-link>
        </div>
    </aside>
</template>

<script setup>
import { ref } from 'vue'

const expanded = ref(false)

const ToggleMenu = () => {
    expanded.value = !expanded.value
}
</script>

<style lang="scss" scoped>
aside {
    display: flex;
    flex-direction: column;
    width: calc(2rem + 2rem);
    overflow: hidden;
    min-height: 180vh;
    padding: 1rem;
    transition: 0.5s ease-out;

    background-color: var(--dark);
    color: var(--light);

    .icon {
        display: flex;
        justify-content: flex-end;

        position: relative;
        top: 0;
        transition: 0.5s ease-out;

        .toggle {
            transition: 0.5s ease-out;
            .material-icons {
                font-size: 2rem;
                color: var(--light);
                transition: 0.3s ease-out;
            }
        }

        &:hover {
            .material-icons {
                color: var(--primary);
                transform: translateX(0.5rem);
            }
        }
    }

    .menu {
        margin: 0 -1rem;

        .button {
            display: flex;
            align-items: center;
            text-decoration: none;
            padding: 0.5rem 1rem;
            transition: 0.3s ease-out;

            .material-icons {
                font-size: 2rem;
                transition: 0.3s ease-out;
                color: var(--light);
                margin-right: 0.5rem;
            }

            .text {
                transition: 0.3s ease-out;
                color: var(--light);
            }

            &:hover {
                background-color: var(--dark-alt);
                .material-icons, .text {
                    color: var(--primary);
                }
            } 
        }
    }

    h3, .button .text {
        opacity: 0;
        transition: 0.4s ease-out;
    }

    h3 {
        font-size: 0.8rem;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
    }

    &.expanded {
        width: var(--sidebar-width);

        .icon {
            .toggle {
                transform: rotate(-180deg);
            }
        }

         h3, .button .text {
            opacity: 1;
            transition: 0.3s ease-out;
        }

        .button {
            .material-icons {
                margin-right: 0.5rem;
            }
        }
    }

    @media (max-width: 768px){
        position: fixed;
        z-index: 99;
    }
}
</style>
