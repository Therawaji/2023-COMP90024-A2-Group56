<template>
  <div class="app">
    <NavbarVue />
    <div class="view">
      <div class="side">
        <SidebarVue />
      </div>
      <div class="route">
        <router-view />
      </div>
    </div>
  </div>
  

</template>

<script setup>
import SidebarVue from './components/SidebarVue.vue'
import NavbarVue from './components/NavbarVue.vue'
</script>

<style lang="scss">
:root {
  --primary: #4ade80;
  --grey: #64748b;
  --dark: #18124a;
  --dark-alt: #334155;
  --light: #f1f5f9;
  --sidebar-width: 300px;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}

body {
  background: var(--light);
}

button {
  cursor: none;
  appearance: none;
  border: none;
  outline: none;
  background: none;
}

.app {

  .view {
    display: flex;

    .route {
      text-align: center;
      min-width: 180vh;
    }
  }

  main {
    flex: 1 1 0;
    padding: 2rem;
    @media (max-width: 768px) {
      padding-left: 6rem;
    }
  }
}
</style>