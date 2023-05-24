<template>
    <div class="title">
        <h3> Scenario 4 - Comparison of infrastructure and frequenct of Tweets </h3>
    </div>
    <div class="c1">
        <div ref="chart1" style="height: 500px"></div>
        <ul>{{string}}</ul>
    </div>
    <div class="c2">
        <div ref="chart2" style="height: 500px"></div>
        <ul>{{string}}</ul>
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
            string: '',
            chart1: null,
            chart2: null,
            chartData: []
        };
    },
    methods: {
        async getData1() {
            try {
                const response = await axios.get('http://172.26.135.65:5000/view7');
                console.log(response.data);
                this.chartData = response.data;
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
                    text: 'Radar Chart of Melbourne'
                },
                legend: {
                    data: ['Percent of infrastructure', 'Percent of tweets']
                },
                radar: {
                    // shape: 'circle',
                    indicator: this.chartData[0][0]
                },
                series: [
                    {
                    name: 'infra vs tweets',
                    type: 'radar',
                    data: [
                        {
                        value: this.chartData[0][1],
                        name: 'Percent of infrastructure'
                        },
                        {
                        value: this.chartData[0][2],
                        name: 'Percent of tweets'
                        }
                    ]
                    }
                ]
                }
            );
        },
        updateChart2() {
            this.chart2.setOption(
                {
                title: {
                    text: 'Radar Chart of Brisbane'
                },
                legend: {
                    data: ['Percent of infrastructure', 'Percent of tweets']
                },
                radar: {
                    // shape: 'circle',
                    indicator: this.chartData[1][0]
                },
                series: [
                    {
                    name: 'infra vs tweets',
                    type: 'radar',
                    data: [
                        {
                        value: this.chartData[1][1],
                        name: 'Percent of infrastructure'
                        },
                        {
                        value: this.chartData[1][2],
                        name: 'Percent of tweets'
                        }
                    ]
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
    margin-left: 40px;
    margin-top: 40px;
}
.c2 {
    margin-left: 40px;
    margin-top: 40px;
}
</style>