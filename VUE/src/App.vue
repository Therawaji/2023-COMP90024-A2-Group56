<template>
  <CNavGroup visible toggler="Nav dropdown">
    <CNav variant="tabs">
      <CNavItem>
        <CNavLink href="/life" active>
          Life
        </CNavLink>
      </CNavItem>
      <CNavItem>
        <CNavLink href='/genre'>Genre</CNavLink>
      </CNavItem>
      <CNavItem>
        <CNavLink href='/contrast'>Contrast</CNavLink>
      </CNavItem>
      <CNavItem>
        <CNavLink href='/events/by_month'>Events by Month</CNavLink>
      </CNavItem>
      <CNavItem>
        <CNavLink href="/cob">
          COB
        </CNavLink>
      </CNavItem>
    </CNav>
  </CNavGroup>
    <router-view></router-view>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
}
</script>