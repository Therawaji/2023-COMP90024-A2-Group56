<template>
    <div align = 'center'>
        <div id="map" style="height: 100px"></div>
        <img src="@/components/testmap.png" style="height:350px; width:350px; object-fit:cover;">
        <h1>This is 3rd View</h1>
        <ul>{{string}}</ul>
    </div>
</template>

<script>
export default {
    name: 'ThirdView',
    props: {
        msg: String
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
    margin: 40px 0 0;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}
a {
    color: #42b983;
}
</style>

