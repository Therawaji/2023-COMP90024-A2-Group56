<template>
    <nav>
        <div class="menu-item">COMP90024</div>
    </nav>
</template>

<script>
export default {
    name: "NavbarVue"
}
</script>

<style lang="scss" scoped>
nav {
    display: flex;
    align-items: center;
    justify-content: left;
    background-color: var(--dark);
}

nav .menu-item {
    color: #FFF;
    padding: 10px 20px;
    position: relative;
    text-align: left;
    border-bottom: 3px solid transparent;     
}

nav .menu-item a {
    color: inherit;
    text-decoration: none;
}

</style>
