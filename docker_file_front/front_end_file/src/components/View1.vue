<template>
    <div class="title">
        <h3> View1 - Tweets by Month </h3>
    </div>
    <div class="tot">
        <div ref="chart1" style="height: 400px;"></div>
        <ul>{{string1}}</ul>
        <div class="char23">
            <div ref="chart2" style="height: 300px;"></div>
            <ul>{{string2}}</ul>
            <div ref="chart3" style="height: 300px;"></div>
            <ul>{{string3}}</ul>
        </div>
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
            string1: 'Tweets by month',
            string2: '# of events in May',
            string3: '# of types in May',
            chart1: null,
            chart2: null,
            chart3: null,
            chartData1: [],
        };
    },
    methods: {
        async getData1() {
            try {
                const response = await axios.get('http://172.26.135.65:5000/view1');
                console.log(response.data);
                this.chartData1 = response.data;
                this.updateChart1();
                this.updateChart2();
                this.updateChart3();
            } catch (error) {
                console.log(error);
            }
        },
        updateChart1() {
            this.chart1.setOption(
                {
                    xAxis: {
                        type: 'category',
                        data: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                        data: [
                            this.chartData1[0][0],
                            this.chartData1[0][1],
                            this.chartData1[0][2],
                            {
                            value: this.chartData1[0][3],
                            itemStyle: {
                                color: '#a90000'
                            }
                            },
                            this.chartData1[0][4],
                            this.chartData1[0][5],
                            this.chartData1[0][6]
                        ],
                        type: 'bar'
                        }
                    ]
                }
            );
        },
        updateChart2() {
            this.chart2.setOption(
                {
                title: {
                },
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    orient: 'vertical',
                    left: 'left'
                },
                series: [
                    {
                    name: 'Access From',
                    type: 'pie',
                    radius: '50%',
                    data: this.chartData1[1],
                    emphasis: {
                        itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                    }
                ]
                }
            );
        },
        updateChart3() {
            this.chart3.setOption(
                {
                title: {
                },
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    orient: 'vertical',
                    left: 'left'
                },
                series: [
                    {
                    name: 'Access From',
                    type: 'pie',
                    radius: '50%',
                    data: this.chartData1[2],
                    emphasis: {
                        itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                    }
                ]
                }
            );
        },
    },
    mounted() {
        this.chart1 = echarts.init(this.$refs.chart1);
        this.chart2 = echarts.init(this.$refs.chart2);
        this.chart3 = echarts.init(this.$refs.chart3);
        this.getData1();
    },
}
</script>

<style lang="scss" scoped>
.char23 {
    margin-top: 40px;
    line-height: 60px;
}
.title {
    margin-top: 40px;
}
</style>
