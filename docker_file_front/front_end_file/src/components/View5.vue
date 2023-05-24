<template>
    <div class="title">
        <h3> Scenario 3 - Sentimant analysis from Twitter and Mastodon </h3>
    </div>
    <div class="c1">
        <div ref="chart1" style="height: 500px"></div>
    </div>
    <div class="c2">
        <div ref="chart2" style="height: 500px"></div>
    </div>
</template>

<script>
import axios from 'axios';
import * as echarts from 'echarts';

export default {
    name: 'FirstView',
    props: {
        msg: String
    },
    data() {
        return {
            string1: 'Twitter',
            string2: 'Mastodon',
            chart: null,
            chartData1: [],
            chartData2: []
        };
    },
    methods: {
        async getData1() {
            try {
                const response1 = await axios.get('http://172.26.135.65:5000/view5');
                console.log(response1.data);
                this.chartData1 = response1.data;
                this.updateChart1();
                this.updateChart2();
            } catch (error) {
                console.log(error);
            }
        },
        updateChart1() {
            this.chart1.setOption(
                {
                title: {
                    text: '       Twitter:'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'shadow'
                    }
                },
                legend: {},
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis: {
                    type: 'value',
                    boundaryGap: [0, 0.01]
                },
                yAxis: {
                    type: 'category',
                    data: this.chartData1[0][0]
                },
                series: [
                    {
                    name: 'positive',
                    type: 'bar',
                    data: this.chartData1[0][1]
                    },
                    {
                    name: 'negative',
                    type: 'bar',
                    color: '#a90000',
                    data: this.chartData1[0][2]
                    }
                ]
                }
            );
        },
        updateChart2() {
            this.chart2.setOption(
                {
                title: {
                    text: '       Mastodon:'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'shadow'
                    }
                },
                legend: {},
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis: {
                    type: 'value',
                    boundaryGap: [0, 0.01]
                },
                yAxis: {
                    type: 'category',
                    data: this.chartData1[1][0]
                },
                series: [
                    {
                    name: 'positive',
                    type: 'bar',
                    data: this.chartData1[1][2]
                    },
                    {
                    name: 'negative',
                    type: 'bar',
                    color: '#a90000',
                    data: this.chartData1[1][1]
                    }
                ]
                }
            );
        },
    },
    mounted() {
        this.chart1 = echarts.init(this.$refs.chart1);
        this.chart2 = echarts.init(this.$refs.chart2);
        this.getData1();
    },
}
</script>

<style lang="scss" scoped>
.title {
    margin-top: 40px;
}
.c1 {
    margin-top: 40px;
}
.c2 {
    margin-top: 40px;
}
</style>